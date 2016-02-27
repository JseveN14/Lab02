#Neves Project 2
#Simple Calculator

expr = None #variable empty to start while loop
memory_bank = [] #empty list to store past expressions
input("Press any key to start the calculator.")
print("Type 'end' to exit.")

while expr != "end":
    expr = str(input("\nEnter an expression: "))
    while expr == "" or expr == " " or expr.find(" ") >= 0:
        print("\nInvalid Expression!")
        expr = str(input("\nEnter an expression: "))

    #while loop for parentheses
    while (((0 < expr.find("(") < len(expr)-1)
        or (0 < expr.find(")") < len(expr)-1))
        or ((expr[0] == "(") and (expr[-1] != ")")) #open parentheses
        or ((expr[0] != "(") and (expr[-1] == ")")) #open parentheses
        or (0 < expr.find("(") < len(expr)-1) #for parentheses inside expr
        or (0 < expr.find(")") < len(expr)-1) #for parentheses inside expr
        or (expr[0] == "(" and expr[1] == ")")
        or (expr[0] == ")" and expr[1] == "(")
        or (expr[0] == ")") or (expr[-1] == "(")
        or (expr.find(" ") > 0)):
        print("\nInvalid Expression!")
        expr = str(input("\nEnter an expression: "))
    if ((expr[0] == "(") and (expr[-1] == ")")):
        expr = expr[1:-1]#expr is assigned to index between parentheses

    #memory bank commands    
    if expr == "last":
        print(memory_bank)
    elif expr == "last 2":
        print(memory_bank[0:2])
    elif expr == "last 1":
        print(memory_bank[0])

    #exit command    
    elif expr == "end":
        input("\nPress any key to exit.")
        
    #addition
    elif (expr[0] != "+" and expr[-1] != "+"):
        first_number = expr[0:expr.find("+")]
        second_number = expr[expr.find("+")+1: ]

        first_number = int(first_number)
        second_number = int(second_number)
        calculation = first_number + second_number
        answer = expr + " = " + str(calculation)
        print(answer)
        memory_bank.insert(0, answer) #adds value to [0] of empty list
        memory_bank = memory_bank[:3] #lists up to 3 list elements

    #subtraction
    elif (expr[0] != "-" and expr[-1] != "-"):
        first_number = expr[0:expr.find("-")]
        second_number = expr[expr.find("-")+1: ]

        first_number = int(first_number)
        second_number = int(second_number)
        calculation = first_number - second_number
        answer = expr + " = " + str(calculation)
        print(answer)
        memory_bank.insert(0, answer)
        memory_bank = memory_bank[:3]

    #multiplication
    elif (expr[0] != "*" and expr[-1] != "*"):
        first_number = expr[0:expr.find("*")]
        second_number = expr[expr.find("*")+1: ]

        first_number = int(first_number)
        second_number = int(second_number)
        calculation = first_number * second_number
        answer = expr + " = " + str(calculation)
        print(answer)
        memory_bank.insert(0, answer)
        memory_bank = memory_bank[:3]

    #division
    elif (expr[0] != "/" and expr[-1] != "/"):
        first_number = expr[0:expr.find("/")]
        second_number = expr[expr.find("/")+1: ]

        first_number = int(first_number)
        second_number = int(second_number)
        calculation = first_number / second_number
        answer = expr + " = " + str(calculation)
        print(answer)
        memory_bank.insert(0, answer)
        memory_bank = memory_bank[:3]
            
    else:
        print("\nInvalid Expression!")
