from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models.user import User

class Trail():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.peak_height = data['peak_height']
        self.vertical_gain = data['vertical_gain']
        self.technical = data['technical']
        self.beginner = data['beginner']
        self.facilities = data['facilities']
        self.category1 = data['category1']
        self.category2 = data['category2']
        self.category3 = data['category3']
        self.user_id = session['user_id']
        # self.user = None
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_trail(cls, data):

        query = 'INSERT INTO trails (name, peak_height, vertical_gain, technical, difficulty, facilities, user_id, category1, category2, category3) VALUES (%(name)s, %(peak_height)s, %(vertical_gain)s, %(technical)s, %(difficulty)s, %(facilities)s, %(user_id)s, %(category1)s, %(category2)s, %(category3)s);'

        result = connectToMySQL('goats_schema').query_db(query, data)

        return result

    @staticmethod
    def validate_trail(data):

        is_valid = True

        if len(data['name']) < 1:
            flash("Trail should have a name.")
            is_valid = False

        # if len(data['peak_height']) < 1:
        #     flash("Please fill out all fields")
        #     is_valid = False

        # if len(data['vertical_gain']) < 1:
        #     flash("Please fill out all fields")
        #     is_valid = False

        if len(data['technical']) < 1:
            flash("Please fill out all fields")
            is_valid = False

        if len(data['difficulty']) < 1:
            flash("Please fill out all fields")
            is_valid = False

        if len(data['facilities']) < 1:
            flash("Please fill out all fields")
            is_valid = False

        return is_valid