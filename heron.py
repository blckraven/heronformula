print("Program to use Heron's Formula")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
p = (a+b+c)/2
under_sqrt = p*(p-a)*(p-b)*(p-c)
if under_sqrt > 0:
    field = under_sqrt**0.5
    print("Field equals: ", field, " u^2")
else:
    print("error")