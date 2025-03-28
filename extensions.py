from flask_sqlalchemy import SQLAlchemy

# ORM - Object Relational Mapping
# allows you to connect to Multiple DBs
# only thing that changes is connection string
# No RAW-SQL -> SELECT statements, etc.
# Advantages of using SQLMethods?
# # Autocomplete
# # SQLAlchemy (Python) - Since it is Python, can use all Python Methods
# Layer between Python & SQL World

db = SQLAlchemy()

# Driver - middle man (conversion of python to SQL and vice versa)
# Python data -> converts into SQL -> converts back into Python
# who does this conversion ? pyodbc
# python sends data to driver (pyodbc) -> sends query to SQL => sent back to driver -> ends at Python
