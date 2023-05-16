from flask_testing import TestCase
from application import app, db
from application.models import Games
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///testgames.db',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):        # Create table schema
        db.create_all()

        # Create test game
        test_game = Games(name="monopoly")
        db.session.add(test_game)
        test_game = Games(name="scrabble")
        db.session.add(test_game)
        test_game = Games(name="bananagrams")
        db.session.add(test_game)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestRoutes(TestBase):
    def test_get_all_games(self):
        response = self.client.get(url_for('display_games'))
        self.assertEqual(200, response.status_code)
        self.assertIn(b'monopoly', response.data)
        self.assertIn(b'scrabble', response.data)
        self.assertIn(b'bananagrams', response.data)

    def test_add_game(self):
        response = self.client.post(url_for('add'),data=dict(name='jenga'))
        self.assertEqual(200, response.status_code)
        self.assertIn(b'jenga has been added successfully to the database', response.data)

        response = self.client.get(url_for('display_games'))
        self.assertIn(b'monopoly', response.data)
        self.assertIn(b'scrabble', response.data)
        self.assertIn(b'bananagrams', response.data)
        self.assertIn(b'jenga', response.data)
        self.assertEqual(4, Games.query.count())

    def test_add_game_with_a_capital_letter_at_start_of_game_name(self):
        response = self.client.post(url_for('add'),data=dict(name='Jenga'))
        self.assertEqual(200, response.status_code)
        self.assertIn(b'jenga has been added successfully to the database', response.data)

        response = self.client.get(url_for('display_games'))
        self.assertIn(b'jenga', response.data)
        self.assertEqual(4, Games.query.count())

    def test_add_game_with_a_capital_letter_at_start_of_two_word_game_name(self):
        response = self.client.post(url_for('add'),data=dict(name='MOUSE Trap'))
        self.assertEqual(200, response.status_code)
        self.assertIn(b'mouse trap has been added successfully to the database', response.data)

        response = self.client.get(url_for('display_games'))
        self.assertIn(b'mouse trap', response.data)
        self.assertEqual(4, Games.query.count())


    def test_add_game_with_no_name(self):
        response = self.client.post(url_for('add'),data=dict(name=''))
        self.assertEqual(200, response.status_code)
        self.assertIn(b'Invalid data. Addition rejected', response.data)

        response = self.client.get(url_for('display_games'))
        self.assertEqual(3, Games.query.count())

    def test_empty_validation(self):
        self.submit_input('')
        self.assertIn(url_for('index'), self.driver.current_url)

        text = self.driver.find_element_by_xpath('<XPath>').text
        self.assertIn("The name field can't be empty!", text)

        entries = Games.query.all()
        self.assertEqual(len(entries), 0) # database should be empty