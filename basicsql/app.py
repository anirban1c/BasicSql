#!/usr/bin/env python3

from IPython import embed
import logging
import os
import sys
from sqlalchemy import create_engine

import model

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def dbconfig():
	engine = create_engine('sqlite:///some.db')
	model.initiliase(engine, model, model.ModelBase)


def shell():
	dbconfig()
	model.create_model(dropFirst=True)
	model.loadDb(loadFile='db.csv')
	embed(header='My awesome app')


if __name__ == '__main__':
	log.info('dropping into ipython shell')
	shell()