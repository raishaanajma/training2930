try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")

try:
    #incorrect type operation
    res = "100" / 20
    
except ArithmeticError:
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")