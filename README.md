# Sweep AI Simulation Using EvaDB

## Overview
This repository simulates the usage of Sweep AI to create new files by using EvaDB. Sweep is an AI tool to help transform feature requests and bug reports into actual code changes. This project uses the power of the OpenAI GPT-3 model for new code generation. Currently, we support two versions. The simple version, by running `main.py`, supports creating and modifying files locally. The advanced version, by running `app.py`, currently supports creating and modifying files both locally and remotely on GitHub repositories.

## Prerequisites
Before running this project on your end, make sure you have the following requirements satisfied on your end:
- OpenAI API Key: You need an OpenAI API key to use the GPT-3 model for code generation and later for code modification. When you have it, put your key in `api_key` in `main.py` file
- Dependencies: You want to make sure you have proper Python libraries installed to run the script properly, including but not limited to `evadb`, `os`, and `openai`.
- Database Setup: The script in this repository assumes using an underlying `postgres SQL` database. If you want to use other databases, you may need to modify the part where we connect the database with the `evadb` library.
Only needed for advanced version:
- GitHub Token: You need to create your own GitHub token to use the version that supports creating and modifying files on GitHub.
- GitHub Username: You need to know your GitHub username
- GitHub Repository Name: You need to know your target Repository name


## Usage
Here are some steps to properly run the scripts on your end:
If you want to run the version that only supports creating and modifying files locally, follow the steps below
- Clone the repository
- Update the necessary variables in `main.py` with your own versions, such as `api_key` and how you want the output to store
- Change the input issues accordingly based on your needs, but make sure to follow certain formats, as we only support creating new files at the moment
- Run the script, you will see output files appear in the main directory, or preferably in the output folder

If you want to run the version that supports creating and modifying files both locally and remotely on GitHub, follow the steps below
- Clone the repository
- Update the necessary variables in `app.py`,`github.py`, and `gpt.py` with your own versions, such as `api_key` and `github_token` and how you want the output to store
- Change the input issues accordingly based on your needs, but make sure to follow certain formats, as we only support creating and modifying new files at the moment
- Run the script in `app.py`, you will see output files appear in the main directory and relevant files created or updated in the target GitHub repository
