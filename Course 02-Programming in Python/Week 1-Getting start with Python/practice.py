num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
count = 0;
for index, num in enumerate(num_list):
    count+=1;
    if num > 45:
        print(index,f"The number {num} is over 45")
    else:
        print(index,f"The number {num} is smaller than 45")  
    if num == 36:
        print(f"The number is found on {index}th index")
        break
print(count) 