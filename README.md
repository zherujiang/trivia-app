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
- Base URL: Currently this App can only be run locally and is not hosted as a base URL. The backend app is hosted at the default `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application does not require authentication or API keys.

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return these error types when requests fail:
- 400: Bad Request
- 404: Resource Not found
- 422: Unprocessable
- 500: Internal Server Error

### Endpoints

#### GET '/questions'
Fetches all questions or questions by category if a category argument is specified. Questions are paginated in groups of 10. Include the page number argument to choose the page number, starting from 1.
- Request Arguments
  - Use `category=<category_id>` to request questions by category. When omitted, the result returns all questions by default.
  - Use `page=<page_id>` to get questions on the specified page. When omitted, the result returns questions on page 1 by default.
- Returns: A JSON object with a list of questions, success value, total number of questions, all categories, and the current cateogry if exists.
- Sample 1: Get all questions
  `curl http://127.0.0.1:5000/questions`
  
  ```
  {
    "categories": {
      "1": "Science", 
      "2": "Art", 
      "3": "Geography", 
      "4": "History", 
      "5": "Entertainment", 
      "6": "Sports"
    }, 
    "current_category": null, 
    "questions": [
      {
        "answer": "Apollo 13", 
        "category": 5, 
        "difficulty": 4, 
        "id": 2, 
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
      }, 
      {
        "answer": "Tom Cruise", 
        "category": 5, 
        "difficulty": 4, 
        "id": 4, 
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
      }, 
      {
        "answer": "Maya Angelou", 
        "category": 4, 
        "difficulty": 2, 
        "id": 5, 
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      }, 
      {
        "answer": "Edward Scissorhands", 
        "category": 5, 
        "difficulty": 3, 
        "id": 6, 
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
      }, 
      {
        "answer": "Muhammad Ali", 
        "category": 4, 
        "difficulty": 1, 
        "id": 9, 
        "question": "What boxer's original name is Cassius Clay?"
      }, 
      {
        "answer": "Brazil", 
        "category": 6, 
        "difficulty": 3, 
        "id": 10, 
        "question": "Which is the only team to play in every soccer World Cup tournament?"
      }, 
      {
        "answer": "Uruguay", 
        "category": 6, 
        "difficulty": 4, 
        "id": 11, 
        "question": "Which country won the first ever soccer World Cup in 1930?"
      }, 
      {
        "answer": "George Washington Carver", 
        "category": 4, 
        "difficulty": 2, 
        "id": 12, 
        "question": "Who invented Peanut Butter?"
      }, 
      {
        "answer": "Lake Victoria", 
        "category": 3, 
        "difficulty": 2, 
        "id": 13, 
        "question": "What is the largest lake in Africa?"
      }, 
      {
        "answer": "The Palace of Versailles", 
        "category": 3, 
        "difficulty": 3, 
        "id": 14, 
        "question": "In which royal palace would you find the Hall of Mirrors?"
      }
    ], 
    "success": true, 
    "total_questions": 19
  }
  ```
- Sample 2: Get questions by category
  `curl http://127.0.0.1:5000/questions?category=1`
  
  ```
  {
    "categories": {
      "1": "Science", 
      "2": "Art", 
      "3": "Geography", 
      "4": "History", 
      "5": "Entertainment", 
      "6": "Sports"
    }, 
    "current_category": "1", 
    "questions": [
      {
        "answer": "The Liver", 
        "category": 1, 
        "difficulty": 4, 
        "id": 20, 
        "question": "What is the heaviest organ in the human body?"
      }, 
      {
        "answer": "Alexander Fleming", 
        "category": 1, 
        "difficulty": 3, 
        "id": 21, 
        "question": "Who discovered penicillin?"
      }, 
      {
        "answer": "Blood", 
        "category": 1, 
        "difficulty": 4, 
        "id": 22, 
        "question": "Hematology is a branch of medicine involving the study of what?"
      }
    ], 
    "success": true, 
    "total_questions": 3
  }
  ```
- Sample 3: Get questions by category on page 1
  `curl http://127.0.0.1:5000/questions?category=3&page=1`
  
  ```
  {
    "categories": {
      "1": "Science", 
      "2": "Art", 
      "3": "Geography", 
      "4": "History", 
      "5": "Entertainment", 
      "6": "Sports"
    }, 
    "current_category": "3", 
    "questions": [
      {
        "answer": "Lake Victoria", 
        "category": 3, 
        "difficulty": 2, 
        "id": 13, 
        "question": "What is the largest lake in Africa?"
      }, 
      {
        "answer": "The Palace of Versailles", 
        "category": 3, 
        "difficulty": 3, 
        "id": 14, 
        "question": "In which royal palace would you find the Hall of Mirrors?"
      }, 
      {
        "answer": "Agra", 
        "category": 3, 
        "difficulty": 2, 
        "id": 15, 
        "question": "The Taj Mahal is located in which Indian city?"
      }
    ], 
    "success": true, 
    "total_questions": 3
  }
  ```

#### GET '/categories'
Fetches all categories in a dictionary format. The categories object can be accessed with the key `categories`.
- Reqeust Arguments: None
- Returns: A JSON object with a success value, a dictionary object with the key `categories`, where the value contains a dictionary of `id: category_string` key:value pairs.
- Sample: `curl http:///127.0.0.1:5000/categories`
  
  ```
  {
    "categories": {
      "1": "Science", 
      "2": "Art", 
      "3": "Geography", 
      "4": "History", 
      "5": "Entertainment", 
      "6": "Sports"
    }, 
    "success": true
  }
  ```

## Authors
Zheru Jiang
