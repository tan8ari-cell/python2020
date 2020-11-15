def foo(name):
    return "Hi %s" % name


def foof(x, m):
    return "Hi %s %s" % (x, m)
#print(foof("Marry", "John"))


def foor(n, m):
    return "Hi %s %s" % (n.title(), m.title())
#print(foor("marry", "john"))


name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
