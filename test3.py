rwast = input("ENTER YOUR AGE IN WORDS")
try:
    stre = int(rwast)
except:
    stre = -1
if stre > 0:
    print("FAIL PLEASE REPEAT")
else:
    print("WELCOME ON BOARD")






    mach = input("PLEASE ENTER YOUR PIN IN WORDS ")
    try:
        amon_t = int(mach)
    except:
        amon_t = -1
    if amon_t > 20:
        print("INCORRECT PIN")
    else: 
        print("DO YOU WANT TO PROCEED")
        print("YES")
    
    instr = input("Enter Clock in Time")
    try:
        amnt = float(instr)
    except:
        amnt = -1
    if amnt <= 8.00:
        print("YOUR LATE")
        print("This is last Warning")
    else:
        print("WELLDONE")

        
