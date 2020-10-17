#!/usr/bin/env python3
import cgi

requests = cgi.FieldStorage()
print("Content-Type: application/json")
print()

if requests.getfirst("city") == None and requests.getfirst("sex") == None:
    print({
        "message": "some param is empty"
    })
else:
    _city = requests.getfirst("city")
    _sex = requests.getfirst("sex")
    # some code...