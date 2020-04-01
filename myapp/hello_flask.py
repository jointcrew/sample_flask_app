from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown


app = Flask(__name__)

@app.route("/")
def hell_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "This is paiza"

# テンプレートを呼び出す
@app.route("/template")
def call_template():
    # テンプレートにデータを残す
    name = "Flask"
    return render_template("index.html", name_value = name)

# リストを渡す
@app.route("/list")
def get_list():
    name = "Flask"
    players = {"勇者", "戦士", "魔法使い"}
    return render_template("index.html", name_value = name, players = players)

# メニューを表示
@app.route("/menu")
def menu():
    return render_template("menu.html", player = player)

# あるく
@app.route("/walk")
def walk():
    message = player + "は荒野を歩いていた。"
    return render_template("action.html", player = player, message = message)

# たたかう
@app.route("/attack")
def attack():
    message = player + "はモンスターと戦った。"
    return render_template("action.html", player = player, message = message)

@app.route("/result", methods=["GET", "POST"])
def result():
    message = "This is paiza"
    if request.method == "POST":
        article = request.form["article"]
        name = request.form["name"]
    else:
        article = request.args.get("article")
        name = request.args.get("name")
    return render_template("form.html", message = message, article = article, name = name)

@app.route("/bbs")
def bbs():
    message = "Hello world"
    file = codecs.open("articles.txt", "r", "utf-8")
    lines = file.readlines()
    file.close()
    return render_template("bbs.html", message = message, lines = lines)
