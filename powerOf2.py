# Calculating power of 2

num = int(input("enter any number to calculate power of two : "))
i = 1
power = 1
while i <= num:
    power = power * 2
    i = i+1
print("power of two upto ", num, " is : ", power)
