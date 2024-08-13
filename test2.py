instr = input("Enter Clock in Time")
 try:
      amnt = float(instr)
except:
        amnt = -1
    if amnt <= 67.777:
        print("YOUR LATE")
        print("This is last Warning")
    else:
        print("WELLDONE")

        