from sqlalchemy import Column, types
from sqlalchemy.ext.declarative import declarative_base
import sys
import simplejson as json

from sqlalchemy import MetaData
from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.exc import DetachedInstanceError
from sqlalchemy.orm.properties import RelationshipProperty

REPR_TRUNCATE = 40
Base = declarative_base()

class ClassProperty(property):

	def __get__(self, instance, cls):
		return self.fget.__get__(instance, cls)()

class ModelBase(Base):

	_decl_class_registry = dict()
	metadata = MetaData()
	DBSession = scoped_session(sessionmaker(autocommit=True))

	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			if not self.__mapper__.has_property(key):
				raise TypeError("Invalid __init__ argument: '%s'" % key)
			if value == "":
				value = None
				kwargs[key] = value
			setattr(self, key, value)


	@ClassProperty
	@classmethod
	def query(cls):
		query =  cls.DBSession.query(cls)
		return query


	@ClassProperty
	@classmethod
	def cquery(cls):
		_q =  cls.DBSession.query(cls)
		query = _q.filter(cls.ord_id == cls.ord_original_ord_id).order_by(cls.ord_update_date_time)
		return query




	@property
	def _atts(self):
		"""
		Return object representation as <ClassName attr=value, ...> showing all
		fields that are not None and ignoring private fields

		:rtype: str
		"""
		exc_info = sys.exc_info()[0]
		atts = {}

		for prop in self.__mapper__.iterate_properties:
			key = prop.key

			try:
				if isinstance(prop, RelationshipProperty) and prop.lazy:
					# do not force lazy properties to load
					continue
				value = getattr(self, key)
				if value is None or value == "":
					continue
				# do not recurse into related lists just give a count
				if isinstance(value, InstrumentedList):
					if not value:
						continue
					key = "{}".format(key)
					if sys._getframe(1).f_globals.get("__name__") == __name__ \
							and "value" in sys._getframe(1).f_locals:
						value = "..."
				else:
					value = str(value)
				if len(value) > REPR_TRUNCATE:
					value = value[:REPR_TRUNCATE - 3] + "..."
					if value.startswith("'"):
						value += "'"
					elif value.startswith("<"):
						value += ">"
				atts[key] = value
			except DetachedInstanceError:
				pass
			except:
				if exc_info is None:
					# if we weren't handling an exception when we started to repr
					# then raise it otherwise we swallow the exception so that
					# the real error is not masked
					raise
		return atts

	def __repr__(self):
		return json.dumps(self._atts, ensure_ascii=True)



class ImageModel(ModelBase):

	__tablename__ = 'imag_code_test'

	ord_status = Column('ord_status', types.String(10))
	ord_id = Column('ord_id', types.Integer, primary_key=True)
	ord_original_ord_id = Column('ord_original_ord_id', types.Integer)
	ord_quantity = Column('ord_quantity', types.Integer)
	ord_trader = Column('ord_trader', types.VARCHAR)
	ord_update_date_time = Column('ord_update_date_time', types.DateTime)
