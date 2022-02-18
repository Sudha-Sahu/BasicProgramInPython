# Calculating Harmonic number upto nth term

harmonic = int(input("Enter number for nth Harmonic number : "))
i = 1
sumOf_nth_HarmonicNumber = 0
while i <= harmonic:
    if i != harmonic:
        print("1 /", i, "+", end=" ")
        sumOf_nth_HarmonicNumber += 1/i
    else:
        print("1 /", i)
        sumOf_nth_HarmonicNumber += 1 / i
    i = i+1
print("Sum of nth Harmonic number : ", sumOf_nth_HarmonicNumber)
