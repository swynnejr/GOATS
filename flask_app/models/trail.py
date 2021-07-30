from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

class Trail():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.start = data['start']
        self.variation = data['variation']
        self.distance = data['distance']
        self.peak_height = data['peak_height']
        self.vertical_gain = data['vertical_gain']
        self.country = data['country']
        self.state = data['state']
        self.category1 = data['category1']
        self.category2 = data['category2']
        self.category3 = data['category3']
        self.user_id = session['user_id']
        # self.user = None
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_trails(cls):

        query = "SELECT * FROM trails ORDER BY variation;"

        results = connectToMySQL('goats_schema').query_db(query)

        trails = []

        for item in results:
            trails.append(cls(item))

        return trails

    @classmethod
    def get_one_trail(cls, data):
        query = 'SELECT * FROM trails WHERE id = %(id)s;'

        results = connectToMySQL('goats_schema').query_db(query,data)
        trail = Trail(results[0])
        return trail


# ADMIN SECTION BELOW

    @classmethod
    def create_trail(cls, data):

        query = 'INSERT INTO trails (name, start, variation, distance, peak_height, vertical_gain, country, state, user_id, category1, category2, category3) VALUES (%(name)s, %(start)s, %(variation)s, %(distance)s, %(peak_height)s, %(vertical_gain)s, %(country)s, %(state)s, %(user_id)s, %(category1)s, %(category2)s, %(category3)s);'

        result = connectToMySQL('goats_schema').query_db(query, data)

        return result

    @staticmethod
    def validate_trail(data):

        is_valid = True

        if len(data['name']) < 1:
            flash("Trail should have a name.")
            is_valid = False

        if len(data['start']) < 1:
            flash("Trail should have a start.")
            is_valid = False

        # if len(data['peak_height']) < 1:
        #     flash("Please fill out all fields")
        #     is_valid = False

        # if len(data['vertical_gain']) < 1:
        #     flash("Please fill out all fields")
        #     is_valid = False

        if len(data['country']) < 1:
                    flash("Trail should have a country.")
                    is_valid = False

        return is_valid