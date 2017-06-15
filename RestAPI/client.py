#!/usr/bin/env python

import logging
import sys
import simplejson as json
import os
import requests
import csv

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

OUT_FILE='OUTPUT.csv'
REST_URL='http://localhost:8000'

def processLogFiles():
	_files = sys.argv[1:]
	log.info(' Files list {} '.format(_files))
	_headers = []
	_row = []

	for _file in _files[1:]:
			_json = json.loads(requests.get('{}/{}/{}'.format(REST_URL, 'log', _file)).content)
			log.info(' ---> resp -- {} -- '.format(list(_json.keys())))
			_headers.append(list(_json.keys()))
			for k, v in _json.items():
				log.info(' ---> item -- {} -- '.format(_json[k]))
				if 'portfolios_loaded' in k :
					log.info(' ---> port  -- {} -- '.format(v[0]))
					if not v :
						p = '|'.join(v[0][0])
						_row.append(p)
				else:
					_row.append(''.join(str(v[0])))


	log.info(' ---> headers  -- {} -- '.format(_headers))
	with open(OUT_FILE, 'w', newline='') as fo :
		writer = csv.DictWriter(fo, fieldnames = _headers, delimiter = ',')
		writer.writeheader()
		writer.writerows(_row)




if __name__ == '__main__':
	processLogFiles()



