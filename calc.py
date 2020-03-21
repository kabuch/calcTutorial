import re

prev = ""
run = True
print ("calc by kabuch")

def math():
    global run
    global prev
    equal = ""
    if prev == "":
        equal = input("Enter equation: \n")
    else:
        equal = input(str(prev))

    if equal == 'quit':
        run = False
        print("cya")
    else:
        equal=re.sub('[a-zA-Z,.:()"]','',equal)
        if prev == "":
            prev = eval(equal)
        else:
            prev = eval(str(prev)+equal)

while run:
    math()