try:
  x=int(input("Enter the number  between 10 and 100: "))
  if(str(x)==quit):
   print("quit")
  if(x<10 or x>100):
    raise ValueError("Value should be between 10 and 100")
except ValueError:
  print("You Enter a string")
finally:
   print("done")
  