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


	_json = json.loads(requests.get('{}/{}/{}'.format(REST_URL, 'log', _files[0])).content)
	log.info(' ---> headers  -- {} -- '.format(_headers))
	with open(OUT_FILE, 'w', newline='') as fo :
		_headers = list(_json.keys())
		writer = csv.DictWriter(fo, fieldnames = _headers, delimiter = ',')
		writer.writeheader()

	with open(OUT_FILE, 'a', newline='') as fr :
		_rwriter = csv.writer(fr, delimiter = ',')
		for _file in _files:
				_row = []
				_json = json.loads(requests.get('{}/{}/{}'.format(REST_URL, 'log', _file)).content)
				log.info(' ---> resp -- {} -- '.format(list(_json.keys())))
				for k in _headers:
					log.info(' ---> item -- {} -- '.format(_json[k]))
					'''
					if 'portfolios_loaded' in k :

						if not _json[k]:
							log.info(' ---> port  -- {} -- '.format(_json[k][0]))
							p = '|'.join(_json[k][0])
							_row.append(p)
					else:
					'''
					_row.append(''.join(str(_json[k][0])))
				_rwriter.writerow(_row)







if __name__ == '__main__':
	processLogFiles()



