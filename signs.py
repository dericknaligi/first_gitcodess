hr_s = input("Hours")
h_s = float(hr_s)
ra_t = input("Rate")
r_e = float(ra_t)
x_te = input("xtra hours")
xr = float(x_te)
x_rat = input("xtra rate")
_rate = float(x_rat)

_pa_y = h_s * r_e + r_e * _rate * xr
print(_pa_y)