def calci(n1, n2, operations):
    if operations == '+':
     return n1 + n2
    elif operations == '-':
     return n1 - n2
    elif operations == '/':
     return n1 / n2
    elif operations == '*':
     return n1 * n2
    else:
      return "invalid Operations"
    
n1 = int(input("Enter The First Number"))
n2 = int(input("Enter The Second Number"))
operations = input("Enter An operations (+, -, /, *)")

Result = calci(n1,n2,operations)

print("The Result is", Result)    
