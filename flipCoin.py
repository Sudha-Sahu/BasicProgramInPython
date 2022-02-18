# Calculating percentage of number of head and tail

import random

no_of_flip = int(input("Enter the number of times to flip the coin : "))
total_heads = 0
total_tails = 0
cnt = 0
while cnt < no_of_flip:
    coin = random.randint(0, 1)
    if coin < 0.5:
        total_tails += 1
    else:
        total_heads += 1
    cnt += 1
print("Heads came up", total_heads, "times")
print("Tails came up", total_tails, "times")

calc_per_head = (total_heads/no_of_flip)*100
print("Percentage of Head is : ", calc_per_head, "%")
calc_per_tail = (total_tails/no_of_flip)*100
print("Percentage of Tail is : ", calc_per_tail, "%")
