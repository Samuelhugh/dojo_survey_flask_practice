from flask_app.config.mysqlconnection import connectToMySQL


from flask import flash


class Dojo:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.location = db_data['location']
        self.language = db_data['language']
        self.comment = db_data['comment']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']


    @classmethod
    def save(cls, form_data):
        query = 'INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());'
        return connectToMySQL('dojo_survey_scehma').query_db(query, form_data)


    @classmethod
    def get_one_dojo(cls, form_data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = connectToMySQL('dojo_survey_scehma').query_db(query, form_data)
        return cls(results[0])


    @staticmethod
    def is_valid(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 1:
            flash("Must choose Dojo Location.")
            is_valid = False
        if len(dojo['language']) < 1:
            flash("Must choose a Language.")
            is_valid = False
        if len(dojo['comment']) < 20:
            flash("Comments must be 20 characters or Greater.")
            is_valid = False
        return is_valid