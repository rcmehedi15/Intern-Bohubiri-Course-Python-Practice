sum = 0
for i in range(1,5):
    sum = sum + i
    print(sum)

print("----------")
sum = 0
for i in range(1,5):
    sum = sum + i*i
    print(sum)

print("----------")

#odd sum

odd_sum = 0
for i in range(1,10,2):
    odd_sum = odd_sum + i
    print(odd_sum)

# even sum

print("----------")

even_sum = 0
for i in range(2,10,2):
    even_sum = even_sum + i
    print(even_sum)

# complex series = 1+(1+2) + (1+2+3) + (1+2+3+4)

C_Sum = 0
for i in range(1,5):
    for j in range(1,i+1):
        C_Sum = C_Sum + j