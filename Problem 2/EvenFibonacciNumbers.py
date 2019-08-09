def is_even(num):
    is_even = False
    if (num%2)==0:
        is_even = True
    return is_even

Total = 0
Num1 = 1
Num2 = 2
while Num2 < 4000000:
    if is_even(Num2):
        Total += Num2
    Temp = Num2 + Num1
    Num1 = Num2
    Num2 = Temp
