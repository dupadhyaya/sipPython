# -*- coding: utf-8 -*-
#date

import datetime

x1 = datetime.datetime.now()
print(x1)

print(x1.year)
print(x1.strftime("%A"))


x2 = datetime.datetime(2019,6,12)
print(x2.year)
print(x2)

print(x2.strftime("%B"))

#Other codes
#%a, %A, %w, %d, %b, %B, %m, %y, %Y, %H, %H, %i, %p, %p, %M, %S
#%f, %z, %Z, %j, %U, %W, %C, %x, %X, %%

print(x1.strftime("%a %A %b %B"))
