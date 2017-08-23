def add(a, b):
    print "xxx"
    return a + b

def minus(a, b):
    print "yyy"
    return a - b

def main(mod,x):
    return {
        "add": add,
        "minus": minus
        }.get(mod, None)(1, x)  # default return is "None", when there is no answer is dict.

x = ["add_1", "minus_2"]
for i in x:
    a1 = i.split("_")
    main(a1[0], int(a1[1]))
    # print main(a1[0], int(a1[1]))