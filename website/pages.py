from flask import Blueprint, request, current_app
from flask.templating import render_template
from flask_login import logout_user, current_user
#from data_analysis import recommendation

lines = []
pages = Blueprint("pages", __name__)


@pages.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        calories = request.form.get('calories')
        health = request.form.get('health')
        ingredient_choice = request.form.getlist('ingredient_choice')
        #recommendations = recommendation(ingredient_choice, calories, health)
        return render_template("recommendation.html", user=current_user, data=[[8501,
  'Omelets',
  'www.cookbooks.com/Recipe-Details.aspx?id=577824',
  '["Egg Beaters"]'],
 [33656,
  'Fluffy Brioche (3 Types)',
  'cookpad.com/us/recipes/144468-fluffy-brioche-3-types',
  '["Super", "Egg"]'],
 [23520,
  '1-2-3 Cranberry Fluff ',
  'www.epicurious.com/recipes/member/views/1-2-3-cranberry-fluff-50087277',
  '["cranberries", "Sugar", "egg"]'],
 [30862,
  'Quinoa Patties',
  'www.food.com/recipe/quinoa-patties-474130',
  '["tuna", "quinoa", "egg"]'],
 [20145,
  'Berry Fluff',
  'www.food.com/recipe/berry-fluff-228596',
  '["raspberries", "sugar", "egg", "salt", "berries"]'],
 [23166,
  'Simple Fried Egg ',
  'www.epicurious.com/recipes/member/views/simple-fried-egg-50025786',
  '["egg salt"]']])

    with open('website/ingredients.txt', 'r') as f:
        lines = f.readlines()
        f.close()
    return render_template("home.html", user=current_user, data=lines)
