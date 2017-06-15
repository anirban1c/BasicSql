
Run unittests
py3venv)anirbans-MacBook-Pro:RestAPI anirban$ nosetests -vv
nose.config: INFO: Ignoring files matching ['^\\.', '^_', '^setup\\.py$']
test_get_log1_data (tests.TestRestUris) ... ok
test_get_log1_resp (tests.TestRestUris) ... ok
test_get_log2 (tests.TestRestUris) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.275s


Start Server
    gunicorn --reload server:app



Test initial response
(py3venv)anirbans-MacBook-Pro:RestAPI anirban$ http localhost:8000/log/log_sample_1.log
HTTP/1.1 200 OK
Connection: close
Date: Wed, 14 Jun 2017 12:48:31 GMT
Server: gunicorn/19.6.0
content-length: 329
content-type: application/json; charset=UTF-8

{
    "client_version": [
        "jfe"
    ],
    "end_time_est": [
        "02/14/2014 23:14:23:324287"
    ],
    "error_count": [
        8
    ],
    "log_file_name": [
        "log_sample_1.log"
    ],
    "portfolios_loaded": [
        [
            "~PM_TEST",
            "PM_TESTXYZ"
        ]
    ],
    "session_length": [
        "log_sample_1.log"
    ],
    "start_time_est": [
        "02/14/2014 11:39:52:835039"
    ],
    "time_zone": [
        "Singapore"
    ],
    "user_name": [
        "janedoe"
    ]
}
