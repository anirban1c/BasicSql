import logging
import copy
import datetime
from .imagemodel import ModelBase
from .imagemodel import ImageModel

log = logging.getLogger(__name__)

def initiliase(engine, module, base):

	base.DBSession.configure(bind=engine)
	base.metadata.bind = engine
	_url = copy.deepcopy(engine.url)
	log.info('Model {} initliased  from {} '.format(module.__name__, _url))


def create_model(dropFirst=False):
	ModelBase.DBSession.begin(subtransactions=True)
	if dropFirst:
		log.info('Dropping model')
		ModelBase.metadata.drop_all(checkfirst=True)
	ModelBase.metadata.create_all(checkfirst=not dropFirst)
	ModelBase.DBSession.commit()
	log.info('Model Created')


def loadDb(loadFile=None):
	_fmt = '%m/%d/%Y %H:%M'
	if not loadFile:
		log.error('Need a file to load data from loadDb(loadFile=...)')
	else:

		with open(loadFile) as fi:
			_lines = fi.readlines()

			_cols = _lines[0].split(',')

			for _lin in _lines[1:]:
				ImageModel.DBSession.begin(subtransactions=True)
				_ins = ImageModel()
				_line = _lin.split(',')
				log.info('inserting {} '.format(_line))
				log.info('0  %s ' % _line[0])
				_ins.ord_status = '%s' % _line[0]
				_ins.ord_id = '%s' % _line[1]
				_ins.ord_original_ord_id = '%s' % _line[2]
				_ins.ord_quantity = '%s' % _line[3]
				_ins.ord_trader = '%s' % _line[4]
				_ins.ord_update_date_time = datetime.datetime.strptime(_line[5].strip(' \n'), _fmt)
				'''
				setattr(_ins, _cols[0], '%s

				' % _line[0])
				setattr(_ins, _cols[1], '%s' % _line[1])
				setattr(_ins, _cols[2], '%s' % _line[2])
				setattr(_ins, _cols[3], '%s' % _line[3])
				setattr(_ins, _cols[4], '%s' % _line[4])
				'''

				log.info(' date - str - %r' % _line[5].strip(' \n'))
				#setattr(_ins, _cols[5], datetime.datetime.strptime(_line[5].strip(' \n'), _fmt))
				ImageModel.DBSession.add(_ins)
				ImageModel.DBSession.commit()
				log.info('row committed')







