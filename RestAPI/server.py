import sys
import os
import logging
import datetime
import simplejson as json
import falcon
import shutil
from collections import  OrderedDict, defaultdict


LOGS_DIR = '/Users/anirban/Downloads/millenium/codetest/logs'

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class LogsResource(object):
	def on_get(self, req, resp, logname):

		respBody = defaultdict(list)


		try:
			if os.path.exists(os.path.join(LOGS_DIR, logname)):
				log.info('opening file {} '.format(os.path.join(LOGS_DIR, logname)))
				with open(os.path.join(LOGS_DIR, logname), 'r') as fi:
					_lines = fi.readlines()
					respBody['log_file_name'].append(logname)
					respBody['error_count'].append(len([x for x in _lines if ' -E- ' in x]))
					respBody['end_time_est'].append(_lines[-1].split(' -I- ')[0])

					respBody['start_time_est'].append([_lines[_lines.index(x) + 1] for x in _lines if '-I- Setting Timezone' in x][-1].split(' -I- ')[0])
					respBody['session_length'].append(logname)
					respBody['user_name'].append([x.strip('\n') for x in _lines if ' -I- cpt_server started with ' in x][-1].split('/users/')[1].split('/')[0])
					respBody['client_version'].append('cmlib/' + [x for x in _lines if ' USER_AGENT ' in x][-1].split('cmlib/')[1].split(' ')[0])
					respBody['portfolios_loaded'].append([x.strip('\n').split(' -I- Gathering Portfolio View ')[1][1:-1] for x in _lines if ' -I- Gathering Portfolio View ' in x] or None)
					respBody['time_zone'].append([x.strip('\n') for x in _lines if ' -I- Setting Timezone to ' in x][-1].split(' -I- Setting Timezone to ')[1])

				resp.status = falcon.HTTP_200
				resp.body = json.dumps(respBody)

			else:
				resp.status = falcon.HTTP_404
				resp.body = json.dumps('Log name {} passed is Not Found in Dir {} '.format(logname, LOGS_DIR))
		except Exception as e:
			#raise
			raise falcon.HTTPBadRequest(
				'Something went horribly wrong',
				'Error {} '.format(e)
			)




def create_app():
	app = falcon.API()
	logs = LogsResource()
	app.add_route('/log/{logname}', logs)
	return app

app = create_app()

