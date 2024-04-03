class MyZeroDivisionError(ZeroDivisionError):
    pass

def do_the_division(mine):
    if mine :
        raise MyZeroDivisionError("Some Worse News")
    else :
        raise ZeroDivisionError("Some Worse news")
    
for mode in [False, True]:
    try :
        do_the_division(mode)
    except ZeroDivisionError : 
        print("Division By Zero")

for mode in [False, True]:
    try : 
        do_the_division(mode)
    except MyZeroDivisionError:
        print("My Zero Div Error")
    except ZeroDivisionError:
        print("General Division Error")
        