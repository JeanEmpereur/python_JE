import sys

liste = []
verbose = False
upper = False
lower = False
strict = False
for arg in sys.argv:
    if (arg == "--verbose") :
        verbose = True
    elif (arg == "--upper") :
        upper = True
    elif (arg == "--lower") :
        lower = True
    elif (arg == "--strict") :
        strict = True
    else :
        liste.append(arg)


if upper and lower :
    print (1)
else :
    for l in liste :
        if verbose :
            print ("# processing file " + l)
        with open(l, 'r') as f :
            data = f.read()

        if upper :
            data = data.upper()
        if lower :
            data = data.lower()

        print (data)
