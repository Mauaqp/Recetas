from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    #Metodo de creación de usuarios
    @classmethod
    def addUser( cls, data ):
        query = "INSERT INTO users (first_name, last_name, email,password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL( "users_session" ).query_db( query, data )


    #Get all
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        resultados = connectToMySQL("users_session").query_db( query)
        listaUsuarios = []
        for u in resultados:
            listaUsuarios.append(cls(u))
        return listaUsuarios

    #Get por email
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("users_session").query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    #Get por id
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        resultado = connectToMySQL("users_session").query_db(query,data)
        return cls(resultado[0])

    #Validation con re
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        resultado = connectToMySQL("users_session").query_db(query,user)
        if len(resultado) >= 1:
            flash("El email ya ha sido registrado antes", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("Email inválido", "register")
            is_valid = False
        if len(user["first_name"]) < 3:
            flash ("Tu nombre debe tener al menos 3 carácteres", "register")
            is_valid = False
        if len(user["last_name"]) < 3:
            flash("Tu apellido debe tener al menos 3 carácteres" "register")
            is_valid = False
        if len(user["password"]) < 8 :
            flash ("La contraseña debe tener al menos 8 carácteres", "register")
            is_valid = False
        if user["password"] != user["confirm"]:
            flash("Las contraseñas no coinciden", "register")
        return is_valid