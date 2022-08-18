import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {'question': 'What is my favorite color?', 'answer': 'blue', 'category': '4', 'difficulty': '1'}
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    ## test get questions
    def test_get_questions(self):
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['categories'])
        self.assertFalse(data['current_category'])
    
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')
        
    ## test get questions by category
    def test_get_question_by_category(self):
        res = self.client().get('/questions?category=1')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['categories'])
        self.assertTrue(data['current_category'])
    
    ## test delete questions
    def test_delete_question(self):
        res = self.client().delete('/questions/22')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 22)
    
    def test_404_deleting_question_not_exist(self):
        res = self.client().delete('/questions/100')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        
    ## test add questions
    def test_add_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['inserted'])
        
    def test_405_question_not_created(self):
        res = self.client().post('/questions/1', json=self.new_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')
    
    ## test search questions
    def test_search_questions(self):
        res = self.client().post('/questions', json={'searchTerm': 'actor'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(data['totalQuestions'], 1)
    
    def test_search_question_no_result(self):
        res = self.client().post('/questions', json={'searchTerm': 'nothing in trivia like this'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertFalse(data['questions'])
        self.assertEqual(data['totalQuestions'], 0)
    
    ## test get questions to play the quiz
    def test_get_quiz_question(self):
        res = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category': {'id': 0}})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
    
    def test_fail_processing_get_quiz(self):
        res = self.client().post('/quizzes', json={'previous_questions': []})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'internal server error')
    
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()