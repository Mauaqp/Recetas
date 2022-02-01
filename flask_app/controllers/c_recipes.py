from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.m_recipe import Recipe
from flask_app.models.m_user import User

@app.route('/recipes/new', methods=["POST"])
def createRecipe ():
    Recipe.addRecipe(request.form)
    return redirect('/dashboard')