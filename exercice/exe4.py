import os

def creator(filename):
    if not os.path.isfile(filename):
        f = open(filename, 'w')
        f.close()
        return filename
    else :
        f = open(filename, 'r')
        data = f.read()
        if data == "" :
            f.close()
            print("old")
            return filename
        f.close()
    print("exist deja !!")
    return filename

def writer(opened, data):
    nb = 0
    with open(opened, 'w') as f :
        for d in data :
            nb += len(d)
            f.write(d + "\n")
        f.close()
    return nb 

def closer(opened):
    
    return 0


opened = creator("alpha.txt")
print(writer(opened, ["alpha","beta"]))
