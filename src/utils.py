

def write_file(name, content):
    fname = name+".py"
    content = content
    with open(fname, "w") as file:
        file.write(content)
