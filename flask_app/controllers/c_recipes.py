from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.m_recipe import Recipe
from flask_app.models.m_user import User

@app.route('/recipes/new', methods=["POST"])
def createRecipe ():

    data = {
        "name_recipe" : request.form["name_recipe"],
        "description" : request.form["description"],
        "preparation_time" : request.form["preparation_time"],
        "instructions" : request.form["instructions"],
        "created_at" : request.form["created_at"],
        "user_id" : session["user_id"]
    }
    Recipe.addRecipe(data)
    return redirect('/dashboard')

#Ruta para Editar receta (GET)
@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_recipe.html",edit=Recipe.get_one(data), user=User.get_by_id(user_data))

@app.route('/update/recipe', methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes')
    data = {
        "name_recipe": request.form["name_recipe"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "preparation_time": int(request.form["preparation_time"]),
        "created_at": request.form["created_at"],
        "id": request.form["id"]
    }
    Recipe.update(data)
    return redirect('/dashboard')

#Mostrar receteas
@app.route('/recipe/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_recipe.html",recipe=Recipe.get_one(data),user=User.get_by_id(user_data))

#Eliminar receta
@app.route('/delete/recipe/<int:id>')
def destroy_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Recipe.delete(data)
    return redirect('/dashboard')