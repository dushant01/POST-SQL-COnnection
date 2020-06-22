# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:14:33 2020

@author: HP
"""


import mysql.connect

data_obj=mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="MachineLearning"
)

a = int(input("enter the student id : "))
b = input("enter user name : ")
c = input("enter email id : ")
d = input("enter Phone number : ")
cursor=data_obj.cursor()
query1="CREATE TABLE INFO(stuent name VARCHAR(30),username VARCHAR(20),email_id VARCHAR(20),phone_number INT)";
query2 = "INSERT INTO ML (student id,username,email id,phone number) VALUES ('.format(a)','.format(b)','.format(c)','format(d)')"
query="select * from ML"
cursor.execute(query1,query2,query)
data =cursor.fetchall()
for i,j,k in data:
print('''\
2
student id:{}
username :{}
Email:{}
Phone Number:{}''')

data_obj.close()
print("data updated")