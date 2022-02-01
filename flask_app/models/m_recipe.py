from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name_recipe = data["name_recipe"]
        self.description = data["description"]
        self.preparation_time = data["preparation_time"]
        self.instructions = data["instructions"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def addRecipe(cls,data):
        query = "INSERT INTO recipes (name_recipe, description, preparation_time, created_at, updated_at , user_id) VALUES(%(name_recipe)s, %(description)s, %(preparation_time)s, NOW(),NOW(), %(user_id)s);"
        return connectToMySQL("users_session").query_db( query, data )

