# local

def func1():
    x = 1 
    print(x)

def func2():
    x = 2 
    print(x)

func1()
func2()

# enclosed

def func1():
    x = 1 
    def func2():
        print(x)
    func2()

func1()

# global

def func1():
    print(x)

def func2():
    print(x)

x = 3 #global

func1()
func2()

# built-in

from math import e 

def func1():
    print(e)

func1()