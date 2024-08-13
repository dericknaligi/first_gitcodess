 

#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly.


n_hs = input("enter normal  hours")
h = float(n_hs)
hn_2 = input("Enter extra hours")
x_hr = float(hn_2)

r_et = input("normal rate")
R_et = float(r_et)
ext_rae = input("enter working extra rate")
_extpa = float(ext_rae)
gs = R_et * _extpa
_perp = h * R_et + x_hr * gs
print(_perp)
if _perp < 100:
    print("No pay")