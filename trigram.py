import re

email = str(input("what email do you want: "))
f = open(email, "r").readline()

split = re.findall('...', f)
for tri in split:
    print(tri)
    if tri in split == True:
        print tri
    else:
        continue
print(split)
