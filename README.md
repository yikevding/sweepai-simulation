# Sweep AI Simulation Using EvaDB

## Overview
This repository simulates the usage of Sweep AI to create new files by using EvaDB. Sweep is an AI tool to help transform feature requests and bug reports into actual code changes. This project uses the power of the OpenAI GPT-3 model for new code generation. Currently, we only support the feature of creating new files locally. we will support more features, such as modifying the existing codebase and working with files stored online, a bit later.

## Prerequisites
Before running this project on your end, make sure you have the following requirements satisfied on your end:
- OpenAI API Key: You need an OpenAI API key to use the GPT-3 model for code generation and later for code modification. When you have it, put your key in `api_key` in `main.py` file
- Dependencies: You want to make sure you have proper Python libraries installed to run the script properly, including but not limited to `evadb`, `os`, and `openai`.
- Database Setup: The script in this repository assumes using an underlying `postgres SQL` database. If you want to use other databases, you may need to modify the part where we connect the database with the `evadb` library.


## Usage
Here are some steps to properly run the scripts on your end:
- Clone the repository
- Update the necessary variables in `main.py` with your own versions, such as `api_key` and how you want the output to store
- Change the input issues accordingly based on your needs, but make sure to follow certain formats, as we only support creating new files at the moment
- Run the script, you will see output files appear in the main directory, or preferably in the output folder
