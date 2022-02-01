from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name_recipe = data["name_recipe"]
        self.description = data["description"]
        self.preparation_time = data["preparation_time"]
        self.instructions = data["instructions"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
    
    #Agregar receta
    @classmethod
    def addRecipe(cls,data):
        query = "INSERT INTO recipes (name_recipe, description, preparation_time,instructions, created_at, updated_at , user_id) VALUES(%(name_recipe)s, %(description)s, %(preparation_time)s, %(instructions)s, NOW(),NOW(), %(user_id)s);"
        return connectToMySQL("users_session").query_db( query, data )
    
    #Get all
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        resultado = connectToMySQL("users_session").query_db(query)
        all_recipes=[]
        for r in resultado:
            all_recipes.append(cls(r))
        return all_recipes

    #Get one
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        resultado = connectToMySQL("users_session").query_db(query, data)
        return cls(resultado[0])
    
    #Editar
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name_recipe=%(name_recipe)s, description=%(description)s, instructions=%(instructions)s, preparation_time=%(preparation_time)s, created_at=%(created_at)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("users_session").query_db(query,data)
    
    #Validación de recetas
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name_recipe']) < 3:
            is_valid = False
            flash("El nombre de la receta debe tener al menos 3 carácteres","recipe")
        if len(recipe['instructions']) < 10:
            is_valid = False
            flash("Las instrucciones deben tener al menos 10 carácteres","recipe")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("La descripción debe tener al menos 3 carácteres","recipe")
        if recipe['created_at'] == "":
            is_valid = False
            flash("Por favor ingresa una fecha","recipe")
        return is_valid

    #Borrar receta
    @classmethod
    def delete (cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL("users_session").query_db(query,data)
