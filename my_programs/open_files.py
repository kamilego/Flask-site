def open_func(file):
    with open(f"dane/{file}", "r") as f:
        text = f.readlines()
        text = [elem.replace("\n", "") for elem in text if elem != "\n"]
    return text

a = open_func("poem.txt")
print(a)