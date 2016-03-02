expr = None #set expression empty for while loop to function
memory_bank = [] #empty list to store past expressions

#directions
input("Press the Enter key to start the calculator.")
print("Type 'end' to exit the calculator.")
print("Type 'last' to retrieve the last 3 entries in the memory bank.")
print("Type 'last 2' to retrieve the last 2 entries in the memory bank.")
print("Type 'last 1' to retrieve the last entry in the memory bank.")

#while loop to keep calculator on
while expr != "end":
    expr = str(input("\nEnter an expression: "))
    if expr == "end": #ends calculator
        input("Press Enter to exit the calculator.")
    elif expr == "" or expr == " ":#invalid if input blank
        print("\nInvalid expression")

    #elif statements for memory bank
    elif expr == "last":
        if memory_bank == []:
            print("There are past expressions to display.")
        else:
            print(memory_bank)
            
    elif expr == "last 2":
        if memory_bank == []:
            print("There are past expressions to display.")
        else:
            print(memory_bank[0:2])
        
    elif expr == "last 1":
        if memory_bank == []:
            print("There are past expressions to display.")
        else:
            print(memory_bank[0])

    #elif for invalid symbols
    elif ((0<=expr.find("["))or(0<=expr.find("]"))or(0<=expr.find("{"))
        or(0<=expr.find("}"))or(0<=expr.find("|"))or(0<=expr.find("_"))
        or(0<=expr.find("&"))or(0<=expr.find("^"))or(0<=expr.find("%"))
        or(0<=expr.find("$"))or(0<=expr.find("#"))or(0<=expr.find("@"))
        or(0<=expr.find("!"))or(0<=expr.find("`"))or(0<=expr.find("~"))
        or(0<=expr.find("<"))or(0<=expr.find(">"))or(0<=expr.find("="))
        or(0<=expr.find(","))or(0<=expr.find("?"))or(0<=expr.find(":"))
        or(0<=expr.find(";"))or(0<=expr.find(" "))):
        print("\nInvalid expression")

    #elif for invalid lowercase letters
    elif ((0<=expr.find("a"))or(0<=expr.find("b"))or(0<=expr.find("c"))
        or(0<=expr.find("d"))or(0<=expr.find("e"))or(0<=expr.find("f"))
        or(0<=expr.find("g"))or(0<=expr.find("h"))or(0<=expr.find("i"))
        or(0<=expr.find("j"))or(0<=expr.find("k"))or(0<=expr.find("l"))
        or(0<=expr.find("m"))or(0<=expr.find("n"))or(0<=expr.find("o"))
        or(0<=expr.find("p"))or(0<=expr.find("q"))or(0<=expr.find("r"))
        or(0<=expr.find("s"))or(0<=expr.find("t"))or(0<=expr.find("u"))
        or(0<=expr.find("v"))or(0<=expr.find("w"))or(0<=expr.find("x"))
        or(0<=expr.find("y"))or(0<=expr.find("z"))):
        print("\nInvalid expression")

    #elif for invalid uppercase letters
    elif ((0<=expr.find("A"))or(0<=expr.find("B"))or(0<=expr.find("C"))
        or(0<=expr.find("D"))or(0<=expr.find("E"))or(0<=expr.find("F"))
        or(0<=expr.find("G"))or(0<=expr.find("H"))or(0<=expr.find("I"))
        or(0<=expr.find("J"))or(0<=expr.find("K"))or(0<=expr.find("L"))
        or(0<=expr.find("M"))or(0<=expr.find("N"))or(0<=expr.find("O"))
        or(0<=expr.find("P"))or(0<=expr.find("Q"))or(0<=expr.find("R"))
        or(0<=expr.find("S"))or(0<=expr.find("T"))or(0<=expr.find("U"))
        or(0<=expr.find("V"))or(0<=expr.find("W"))or(0<=expr.find("X"))
        or(0<=expr.find("Y"))or(0<=expr.find("Z"))):
        print("\nInvalid expression")

    #elif statements for parentheses
    elif ((0 < expr.find("(") < len(expr)-1)#parentheses in expression
        or (0 < expr.find(")") < len(expr)-1)):
        print("\nInvalid expression")
    elif (expr[-1] == ")" and expr[0] != "("):#parentheses not closed
        print("\nInvalid expression")
    elif (expr[0] == "(" and expr[-1] != ")"):#parentheses not closed
        print("\nInvalid expression")
    elif (expr[0] == ")" or expr[-1] == "("):#parentheses reversed
        print("\nInvalid expression")
    elif (expr[0] == "(" and expr[len(expr)-1] == ")"):#() around expression
        expr = expr[1:-1]#expr reassigned between parentheses
        
        #if-elif statements for expressions with parentheses
        if expr == "" or expr == " ":#if parentheses are empty
            print("\nInvalid expression")
        #Invalid if expressions ends with operator
        elif ((expr[-1] == "+")
            or (expr[-1] == "-")
            or (expr[-1] == "*")
            or (expr[-1] == "/")):
                print("\nInvalid expression")
                
        #if statement for addition
        elif (len(expr)-1 > expr.find("+") > 0):#if operator inside expression
            first_number = expr[0:expr.find("+")]
            if first_number != "." and first_number[-1] != ".":
                second_number = expr[expr.find("+")+1: ]
                if (second_number != "." and second_number[-1] != "."
                    #more than one operator in expr appears in second_number
                    and second_number.find("+") < 0
                    and second_number.find("-") < 0
                    and second_number.find("*") < 0
                    and second_number.find("/") < 0):
                    first_number = float(first_number)
                    second_number = float(second_number)
                    calculation = first_number + second_number
                    answer = expr + " = " + str(calculation)
                    print(answer)
                    #inserts answer to [0] position
                    memory_bank.insert(0, answer)
                    #displays up to the 3rd expression
                    memory_bank = memory_bank[:3]
                else:
                    print("\nInvalid expression")
            else:
                print("\nInvalid expression")

        #elif statement for subtraction
        elif (len(expr)-1 > expr.find("-") > 0):
            first_number = expr[0:expr.find("-")]
            if first_number != "." and first_number[-1] != ".":
                second_number = expr[expr.find("-")+1: ]
                if (second_number != "." and second_number[-1] != "."
                    and second_number.find("+") < 0
                    and second_number.find("-") < 0
                    and second_number.find("*") < 0
                    and second_number.find("/") < 0):
                    first_number = float(first_number)
                    second_number = float(second_number)
                    calculation = first_number - second_number
                    answer = expr + " = " + str(calculation)
                    print(answer)
                    memory_bank.insert(0, answer)
                    memory_bank = memory_bank[:3]
                else:
                    print("\nInvalid expression")
            else:
                print("\nInvalid expression")

        #elif statement for multiplication
        elif (len(expr)-1 > expr.find("*") > 0):
            first_number = expr[0:expr.find("*")]
            if first_number != "." and first_number[-1] != ".":
                second_number = expr[expr.find("*")+1: ]
                if (second_number != "." and second_number[-1] != "."
                    and second_number.find("+") < 0
                    and second_number.find("-") < 0
                    and second_number.find("*") < 0
                    and second_number.find("/") < 0):
                    first_number = float(first_number)
                    second_number = float(second_number)
                    calculation = first_number * second_number
                    answer = expr + " = " + str(calculation)
                    print(answer)
                    memory_bank.insert(0, answer)
                    memory_bank = memory_bank[:3]
                else:
                    print("\nInvalid expression")
            else:
                print("\nInvalid expression")

        #elif statement for division
        elif (len(expr)-1 > expr.find("/") > 0):
            first_number = expr[0:expr.find("/")]
            if first_number != "." and first_number[-1] != ".":
                second_number = expr[expr.find("/")+1: ]
                if (second_number != "." and second_number[-1] != "."
                    and second_number.find("+") < 0
                    and second_number.find("-") < 0
                    and second_number.find("*") < 0
                    and second_number.find("/") < 0):
                    first_number = float(first_number)
                    second_number = float(second_number)
                    calculation = first_number / second_number
                    answer = expr + " = " + str(calculation)
                    print(answer)
                    memory_bank.insert(0, answer)
                    memory_bank = memory_bank[:3]
                else:
                    print("\nInvalid expression")
            else:
                print("\nInvalid expression")
                    
        else:
            print("\nInvalid expression")

    #elif statements for expressions without parentheses
    #if statement for expressions that end with an operator
    elif ((expr[len(expr)-1] == "+")
        or (expr[len(expr)-1] == "-")
        or (expr[len(expr)-1] == "*")
        or (expr[len(expr)-1] == "/")):
            print("\nInvalid expression")
    
    #elif statement for addition
    elif (len(expr)-1 > expr.find("+") > 0):
        first_number = expr[0:expr.find("+")]
        if first_number != "." and first_number[-1] != ".":
            second_number = expr[expr.find("+")+1: ]
            if (second_number != "." and second_number[-1] != "."
                and second_number.find("+") < 0
                and second_number.find("-") < 0
                and second_number.find("*") < 0
                and second_number.find("/") < 0):
                first_number = float(first_number)
                second_number = float(second_number)
                calculation = first_number + second_number
                answer = expr + " = " + str(calculation)
                print(answer)
                #inserts answer to [0] position
                memory_bank.insert(0, answer)
                #displays up to the 3rd expression
                memory_bank = memory_bank[:3]
            else:
                print("\nInvalid expression")
        else:
            print("\nInvalid expression")
    #elif statement for subtraction
    elif (len(expr)-1 > expr.find("-") > 0):
        first_number = expr[0:expr.find("-")]
        if first_number != "." and first_number[-1] != ".":
            second_number = expr[expr.find("-")+1: ]
            if (second_number != "." and second_number[-1] != "."
                and second_number.find("+") < 0
                and second_number.find("-") < 0
                and second_number.find("*") < 0
                and second_number.find("/") < 0):
                first_number = float(first_number)
                second_number = float(second_number)
                calculation = first_number - second_number
                answer = expr + " = " + str(calculation)
                print(answer)
                memory_bank.insert(0, answer)
                memory_bank = memory_bank[:3]
            else:
                print("\nInvalid expression")
        else:
            print("\nInvalid expression")

    #elif statement for multiplication
    elif (len(expr)-1 > expr.find("*") > 0):
        first_number = expr[0:expr.find("*")]
        if first_number != "." and first_number[-1] != ".":
            second_number = expr[expr.find("*")+1: ]
            if (second_number != "." and second_number[-1] != "."
                and second_number.find("+") < 0
                and second_number.find("-") < 0
                and second_number.find("*") < 0
                and second_number.find("/") < 0):
                first_number = float(first_number)
                second_number = float(second_number)
                calculation = first_number * second_number
                answer = expr + " = " + str(calculation)
                print(answer)
                memory_bank.insert(0, answer)
                memory_bank = memory_bank[:3]
            else:
                print("\nInvalid expression")
        else:
            print("\nInvalid expression")

    #elif statement for division
    elif (len(expr)-1 > expr.find("/") > 0):
        first_number = expr[0:expr.find("/")]
        if first_number != "." and first_number[-1] != ".":
            second_number = expr[expr.find("/")+1: ]
            if (second_number != "." and second_number[-1] != "."
                and second_number.find("+") < 0
                and second_number.find("-") < 0
                and second_number.find("*") < 0
                and second_number.find("/") < 0):
                first_number = float(first_number)
                second_number = float(second_number)
                calculation = first_number / second_number
                answer = expr + " = " + str(calculation)
                print(answer)
                memory_bank.insert(0, answer)
                memory_bank = memory_bank[:3]
            else:
                print("\nInvalid expression")
        else:
            print("\nInvalid expression")
                
    else:
        print("\nInvalid expression")
