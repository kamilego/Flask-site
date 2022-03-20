import os 

def get_list_of_tabs():
    tabs = os.listdir("../templates")
    tabs = [elem.split(".")[0] for elem in tabs if "index" not in elem]
    return tabs

print(get_list_of_tabs())