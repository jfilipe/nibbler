Instructions
===========

```
$ git clone https://github.com/jfilipe/nibbler.git
$ cd nibbler
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py syncdb
```

Update `nibbler/settings.py` with correct values for the following:

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_STORAGE_BUCKET_NAME`

```
$ python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` and log in using the credentials you setup during `syncdb`.
