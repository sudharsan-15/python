print("welcome to python deliveries")
size=input("what size do you want? S, M, or L")
bill=0
if size == "S":
  bill+=15
elif size== "M":
  bill+=20
elif size== "L" :
  bill+=25
else:
  print("wrong size")

add_pepperoni=input("do you want extra pepperoni? Y or N?")
if add_pepperoni == "Y":
  if size == "S" :
    bill+=2
  elif size =="M" or "L":
    bill+=3
extra_cheese=input("do you want extra cheese? Y or N?")
if extra_cheese == "Y":
  bill +=1
print(f"your final bill is {bill}")