nums =[]
for x in range(5):
    try:
        user_in = int(input("Enter int #" + str(x+1) + ": "))
    except:
        print('Invalid input. Please enter an int.')
        user_in = int(input("Enter int #" + str(x+1) + ": "))
        nums.append(user_in)
    else:
     nums.append(user_in)
total = 0
for num in nums:
   total = total + num
print('Your sum is', total)