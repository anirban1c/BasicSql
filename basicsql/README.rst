activate python virtual environment, dropping into ipython shell

py3venv)anirbans-MacBook-Pro:basicsql anirban$ ./app.py
INFO:__main__:dropping into ipython shell
INFO:model:Model model initliased  from sqlite:///some.db
INFO:model:Dropping model
INFO:model:Model Created

model can be accessed via


In [4]: from model import ImageModel

In [6]: ImageModel.query.filter(ImageModel.ord_original_ord_id == 1250).all()
Out[6]:
[{"ord_quantity": "-25", "ord_update_date_time": "2014-01-29 05:05:00", "ord_id": "1250", "ord_status": "active ", "ord_original_ord_id": "1250", "ord_trader": "A "},
 {"ord_quantity": "-25", "ord_update_date_time": "2014-01-09 01:45:00", "ord_id": "1251", "ord_status": "audit ", "ord_original_ord_id": "1250", "ord_trader": "B "}]


In [18]: ImageModel.DBSession.query(ImageModel).order_by(ImageModel.ord_quantity).all()[-2:]
Out[18]:
[{"ord_quantity": "225", "ord_update_date_time": "2014-01-19 01:05:00", "ord_id": "1222", "ord_status": "audit ", "ord_original_ord_id": "1245", "ord_trader": "B "},
 {"ord_quantity": "225", "ord_update_date_time": "2014-01-19 03:33:00", "ord_id": "1245", "ord_status": "active ", "ord_original_ord_id": "1245", "ord_trader": "B "}]

In [19]: ImageModel.query.filter(ImageModel.ord_status.in_(['audit '])).all()
Out[19]:
[{"ord_quantity": "125", "ord_update_date_time": "2014-01-28 11:05:00", "ord_id": "1205", "ord_status": "audit ", "ord_original_ord_id": "1200", "ord_trader": "B "},
 {"ord_quantity": "-122", "ord_update_date_time": "2014-01-29 04:25:00", "ord_id": "1214", "ord_status": "audit ", "ord_original_ord_id": "1200", "ord_trader": "A "},
 {"ord_quantity": "225", "ord_update_date_time": "2014-01-19 01:05:00", "ord_id": "1222", "ord_status": "audit ", "ord_original_ord_id": "1245", "ord_trader": "B "},
 {"ord_quantity": "-25", "ord_update_date_time": "2014-01-09 01:45:00", "ord_id": "1251", "ord_status": "audit ", "ord_original_ord_id": "1250", "ord_trader": "B "},
 {"ord_quantity": "-66", "ord_update_date_time": "2014-01-29 04:05:00", "ord_id": "1285", "ord_status": "audit ", "ord_original_ord_id": "1275", "ord_trader": "A "},
 {"ord_quantity": "99", "ord_update_date_time": "2014-01-11 05:05:00", "ord_id": "1289", "ord_status": "audit ", "ord_original_ord_id": "1288", "ord_trader": "C "},
 {"ord_quantity": "90", "ord_update_date_time": "2014-01-13 05:05:00", "ord_id": "1291", "ord_status": "audit ", "ord_original_ord_id": "1288", "ord_trader": "C"},
 {"ord_quantity": "90", "ord_update_date_time": "2014-01-15 05:05:00", "ord_id": "1294", "ord_status": "audit ", "ord_original_ord_id": "1288", "ord_trader": "A "}]

