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

If you want to run tests, there is a test file already wrriten for the backend. First, run the following command to create a test database. You can omit the dropdb command when running the tests for the first time.

```
dropdb trivia_test
createdb trivia_test
```

Navigate to the backend folder and run the following commands:

```
psql -f trivia.psql -d trivia_test
python test_flaskr.py
```

This creates test data tables from the trivia.psql file located in the `./backend` directory. Then it executes tests written in the test_flaskr.py.

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
- 405: Method not allowed
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
- Sample: `curl http://127.0.0.1:5000/categories`
  
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

#### DELETE '/questions/{question_id}'
Delete the question with the given ID if exists.
- Request Arguments: None
- Returns: The ID of the deleted question and success value.
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/20`
    ```
    {
        "deleted": 20,
        "success": true
    }
    ```

#### POST '/questions'
Add a new question or search questions by the title. Send request data in the request body. If "searchTerm" is included in the request body, the request will be parsed as a search question request, otherwise, the API will try to create a new question with the request data.
- Request Data
    - To add a new question, send the question data as a JSON object. Include key:value pairs for each of the following: question, answer, category and difficulty.
    - To search questions, send the search term as a JSON object. Use "searchTerm" as the key and put your search term in the value.
- Returns
    - When adding a new question, the API returns a success value and the ID of the inserted new question.
    - When searching questions, the API returns a list of the matching questions, a success value, total number of questions that match the search term, and the current category if exists.
- Sample 1: Add a new question
    `curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"question":"some new question", "answer":"this is the answer", "difficulty":1, "category":2}'`

    ```
    {
        'inserted': 24
        'success': true,
    }
    ```
- Sample 2: Search questions
    `curl -X POST -H "Content-Type: application/json" -d '{"searchTerm":"actor"}' http://127.0.0.1:5000/questions`
    
    ```
    {
      "currentCategory": null, 
      "questions": [
        {
          "answer": "Tom Cruise", 
          "category": 5, 
          "difficulty": 4, 
          "id": 4, 
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }
      ], 
      "success": true, 
      "totalQuestions": 1
    }

    ```

#### POST '/quizzes'
Fetch the next question to play the quiz. This will get one question at a time, that was not shown before in the same quiz. You can get questions by category if the quiz category is specified.

- Request Data
    - Send the list of ids of the previous questions that were shown before in the current quiz (questions per quiz set to 5 in the QuizView.js)
    - The quiz category as a dictionary, include the id of the category. Use `{"id":0}` when getting questions from all categories.
- Returns: A success value and a random question that was not shown previously in the same quiz. If there is no remaining question from the specified category, the returned question will be None. The questions is returned in a dictionary format which contains key:value pairs of these parameters: id, question, answer, category, difficulty.
- Sample: `curl -X POST -H "Content-Type: application/json" -d '{"previous_questions":[2], "quiz_category":{"id":5, "type":"Entertainment"}}' http://127.0.0.1:5000/quizzes`

    ```
    {
      "question": {
        "answer": "Tom Cruise", 
        "category": 5, 
        "difficulty": 4, 
        "id": 4, 
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
      }, 
      "success": true
    }

    ```

## Author
Zheru Jiang
