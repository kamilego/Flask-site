import random
import wikipedia as wiki

wiki.set_lang("pl")

def wiki_char(name):
    content = wiki.summary(name, sentences=6)
    return content

def my_character(name):
    return name*3

def next_char(elem):
    return f"{elem} to kozak"

a = wiki_char("Bruce Lee")
print(a)