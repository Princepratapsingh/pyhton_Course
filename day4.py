numbers=[]
try:
 size=int(input("Enter the size: "))
 for i in range(0,size):
  item=int(input("Enter the Number at index {} ".format(i)))
  numbers.append(item)
  numbers.sort()
 print(numbers)
 if numbers[0]==numbers[1]:
   print(numbers[-1])
 else:
   print(numbers[0])
except ValueError:
    print("Wrong input")
    
