# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import psycopg2

conn= psycopg2.connect(host='127.0.0.1',port='5432',user='postgres',password='9882671591',
                       database='new1')
print("opened database")
cur=conn.cursor()
cur.execute('''
            CREATE TABLE LOGIN
            (NAME TEXT NOT NULL,
            AGE INT NOT NULL);
            ''')
#insert into table

cur.execute('''
            INSERT INTO LOGIN (NAME,AGE)
            VALUES("Dushant",21); 
            ''')
print('values added')
            

conn.commit()
conn.close()

