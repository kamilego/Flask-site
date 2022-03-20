from flask import Flask, render_template
from my_programs.character import my_character, next_char, wiki_char
from my_programs.open_files import open_func
from my_programs.website_tabs import get_list_of_tabs
import random

app=Flask(__name__)


@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    tabs = get_list_of_tabs("kamil-coding.pl")
    return render_template("index.html", text=text, tabs=tabs)


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
    return "Kocham moją ukochaną Olę\n :**"


@app.route('/kochanaola', methods=['GET', 'POST'])
def mylove(): 
    return render_template('kochanaola.html')


@app.route('/ciekawe-postacie')
def ciekawe_postacie():
    int_character = ["Małysz", "Kopernik", "Maria Skłodowska", "Donald Trump", "Kościuszko", "Mieszko I"]
    rand_chars = random.sample(int_character, 3)
    char_descr = []
    for char in rand_chars:
        description = wiki_char(char)
        char_descr.append([char, description, len(description), len(description.split(" "))])
    char_descr = sorted(char_descr, key=lambda x: x[3], reverse=True)
    return render_template("ciekawe-postacie.html", chars=char_descr)


@app.route('/mypage')
def mypage(): 
    return render_template('mypage.html')


if __name__=="__main__":
    app.run()
