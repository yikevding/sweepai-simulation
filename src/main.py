import os
import evadb
import requests
import openai
import re


api_key = "your_openai_key"


def extract_code(db):
    index = 1
    for response in db["response"]:
        code = re.findall(r'```(.*?)```', response, re.DOTALL)
        code = code[0]
        code = '\n'.join(code.splitlines()[1:])
        suffix = ".py"
        prefix = "issue-"
        file_name = prefix+str(index)+suffix
        index += 1
        with open(file_name, "w") as file:
            file.write(code)


cursor = evadb.connect().cursor()


username = "your_username"
password = "your_password"
params = {
    "user": username,
    "password": password,
    "host": "localhost",
    "port": "5432",
    "database": "evadb",
}
query = f"CREATE DATABASE postgres_data WITH ENGINE = 'postgres', PARAMETERS = {params};"
cursor.query(query).df()


# create database table
cursor.query("""
USE postgres_data {
  DROP TABLE IF EXISTS issue_table
}
""").df()


cursor.query("""
USE postgres_data {
  CREATE TABLE issue_table (name VARCHAR(10), issue VARCHAR(1000))
}
""").df()


# insert issues into database
query = """
USE postgres_data {
  INSERT INTO issue_table (name, issue) VALUES ('issue-1',
  'Write a python function that checks if the given string is a palindrome. The function
  takes in one parameter, which is the input word.')
}
"""
cursor.query(query).df()


query = """
USE postgres_data {
  INSERT INTO issue_table (name, issue) VALUES ('issue-2',
  'Write a python function that checks if a given integer can be divisble by both 3 and 5.
  The function takes in one parameter, which is the input integer.')
}
"""
cursor.query(query).df()


query = """
USE postgres_data {
  INSERT INTO issue_table (name, issue) VALUES ('issue-3',
  'Write a python function that checks if a given list of integers is strictly increasing. The function
  takes in one parameter, which is the input list.')
}
"""
cursor.query(query).df()

cursor.query("SELECT * FROM postgres_data.issue_table;").df()


# connect to open ai and simulate how sweep ai works
os.environ["OPENAI_KEY"] = api_key

response_df = cursor.query("""
SELECT ChatGPT(
  "Only reply the python code.",
  issue
)
FROM postgres_data.issue_table;
""").df()


extract_code(db=response_df)
