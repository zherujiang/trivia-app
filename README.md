# Trivia App
A trivia game app for fun. This project is built from the Udacity Fullstack Development degree program. It allows users to view lists of trivia questions, filter questions by category, search questions, add new questions, delete questions, and play the trivia quiz game.
All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

## Getting Started

### Pre-requisites

The project backend is written in Python. Frontend is built with React.js.
Developers using this project should already have Python3, pip and node installed on their local machines.

### Backend

From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file. 

To run the application run the following commands: 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
These commands put the application in development and directs our application to use the `__init__.py` file in the flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

### Frontend

To start the frontend, from the frontend folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```
By default, the frontend will run on localhost:3000.

### Tests

If you want to run tests, there is a test file already wrriten for the backend. Navigate to the backend folder and run the following commands:
```
dropdb trivia_test
createdb trivia_test
psql -f trivia.psql -d trivia_test
python test_flaskr.py
```
You can omit the dropdb command when running the tests for the first time.

## API Reference

### Getting Started

### Error Handling

### Endpoints

## Authors
Zheru Jiang
