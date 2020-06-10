#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "java_conn_learn")
cursor = db.cursor()
cursor.execute("SELECT * FROM ACCOUNT")

data = cursor.fetchone()
while data:
    print(data)
    data = cursor.fetchone()

print(list(data))
db.close()
