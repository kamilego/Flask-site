from flask import Flask, render_template
from my_programs.character import my_character, next_char, wiki_char
from my_programs.open_files import open_func
import random

app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/brudnopis')
def brudnopis():
    new_hero = my_character("Kamil to byczek ")
    hero2 = next_char("Byczek")
    a = [new_hero, hero2]
    champ_choice = random.choice(a)
    poem = open_func("poem.txt")
    bruce = wiki_char("Mikołaj Kopernik")
    return render_template("brudnopis.html", hero1=new_hero, hero2=hero2, hero3=champ_choice, a=a, poem=poem, bruce=bruce)

@app.route('/byczek')
def byczek():
    return render_template("byczek.html")

@app.route('/kamilek')
def kamilek():
    return "Kocham moją ukochaną Olę :**"

if __name__=="__main__":
    app.run()
