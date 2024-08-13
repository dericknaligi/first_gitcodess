def computepay(h,r):
    if h>40:
        norm = 40 * r
        e_p = (h - 40.0) * 1.5 * r
        mone = norm + e_p
    else:
        mone = h * r
    return mone
h_  = input("enter total  hours")
rt = input("enter regular rate")
fe_h = float(h_)
nrat = float(rt)
gro_s_ = computepay(fe_h,nrat)
print("mone", gro_s_)


def computepay(h,r):
    if h>40:
        norm = 40 * r
        e_p = (h - 40.0) * 1.5 * r
        mone = norm + e_p
    else:
        mone = h * r
    return mone
h_  = input("enter total  hours")
rt = input("enter regular rate")
fe_h = float(h_)
nrat = float(rt)
gro_s_ = computepay(fe_h,nrat)
print("mone", gro_s_)