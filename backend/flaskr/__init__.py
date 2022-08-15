import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(selection, page):
    questions = [question.format() for question in selection]
    start = (int(page) - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    current_questions = questions[start:end]
    return current_questions
    
    
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app)

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization, true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods', 'Get, PUT, POST, PATCHT, DELETE, OPTIONS'
        )
        return response

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    this would respond to the GET request from QuizView.js, expecting a dictionary object
    """
    @app.route('/categories')
    def get_categories():
        categories_query = Category.query.order_by(Category.id).all()
        categories = {}
        for category in categories_query:
            categories[category.id] = category.type
        print('all categories:', categories)
        return jsonify({
            'success': True,
            'categories': categories
        })
        
    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions')
    def get_questions():
        print(request)
        current_category = request.args.get('category', None)
        current_page = request.args.get('page', 1)
        print('category', current_category)
        # print('page', current_page)
        try:
            print('test')
            if current_category is not None and current_category != 'null':
                # get questions by category
                questions_query = Question.query.filter(Question.category==current_category).order_by(Question.id).all()
                current_questions = paginate_questions(questions_query, 1)
            else:
                # get all questions
                print('get all questions')
                questions_query = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(questions_query, current_page)
            
            question_num = len(questions_query)

            if question_num == 0:
                abort(404)
            
            categories_query = Category.query.order_by(Category.id).all()
            categories = {}
            for category in categories_query:
                categories[category.id] = category.type
            
            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': question_num,
                'categories': categories,
                'current_category': current_category,
            })
        except:
            abort(400)

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    # combined get_question_by_category with get_questions
    # @app.route('/categories/<int:category_id>/questions')
    # def get_questions_by_category(category_id):
    #     try:
    #         category = Category.query.filter(Category.id==category_id).one_or_none()
    #         print('getting category:', category, category.type)
    #         questions_query = Question.query.filter(Question.category==category_id).order_by(Question.id).all()
    #         current_questions = paginate_questions(questions_query, 1)
    #         return jsonify({
    #             'questions': current_questions,
    #             'total_questions': len(questions_query),
    #             'current_category': category.type
    #         })
    #     except:
    #         abort(404)

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app

