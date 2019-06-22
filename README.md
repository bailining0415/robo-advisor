# "robo-advisor" Project

A solution for the ["Robo Advisor" project] (https://github.com/prof-rossetti/nyu-info-2335-201905/tree/master/projects/robo-advisor)


Issues requests to the [AphaVantage Stock Market API](https://www.alphavantage.co) in order t oprovide automated stock or cryptocurrency trading recommendations



## Prerequisites

 Anaconda 3.7
 Python 3.7
 Pip

 ##Repo Setup

+create a new remote project repository(https://github.com/YOUR_USERNAME/robo-advisor)

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer.


+create "requirements.txt" with a following contents inside:
requests
python-dotenv

## Environment Setup

Create and activate a new Anaconda virtual environment with below command:

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)


## Run Python 

+run below code in command line to get the result

python robo_advisor.py
