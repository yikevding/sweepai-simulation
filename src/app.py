import os
import evadb
import re
from gpt import chatGPT
from utils import write_file
from github import make_commit

user = "PUT YOUR USERNAME HERE"
password = "PUT YOUR PASSWORD HERE"
database = "NAME YOUR DATABASE HERE"

cursor = evadb.connect().cursor()
params = {
    "user": user,
    "password": password,
    "host": "localhost",  # by default using local host
    "port": 5432,
    "database": database
}


# I deault the table name to be github, you can change to whatever you want
cursor.query("""USE postgres_data{
  DROP TABLE IF EXISTS github
}""").df()

cursor.query("""USE postgres_data{
  CREATE TABLE github(
    name VARCHAR(10),
    request VARCHAR(200)
  )
}""").df()


# insert example requests, you can change requests based on your need
query = """
USE postgres_data {
  INSERT INTO github (name, request) VALUES ('request-1',
  'Write a python function that checks if the given string is a palindrome. The function
  takes in one parameter, which is the input word.')
}
"""
cursor.query(query).df()

query = """
USE postgres_data {
  INSERT INTO github (name, request) VALUES ('request-2',
  'Write a python function that checks if a given integer can be divisble by both 3 and 5.
  The function takes in one parameter, which is the input integer.')
}
"""
cursor.query(query).df()

requests = cursor.query("SELECT * FROM postgres_data.github;").df()
file_names = requests["name"]
prompts = requests["request"]
code = []

for i in range(0, len(prompts)):
    code.append(chatGPT(prompts[i]))


for i in range(0, len(prompts)):
    write_file(file_names[i], code[i])


# make new commits on github
for i in range(0, len(prompts)):
    file_path = file_names[i]+".py"
    new_content = code[i]
    commit_message = "Finish executing "+file_names[i]
    make_commit(file_path=file_path, new_content=new_content,
                commit_message=commit_message)
