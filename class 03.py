#Concatenation

f_name = "Usman" # string
l_name = "Hussain" #string
age = 15 #int
weight = 60.6 #float
is_trainer = True #bool

#Method01
print (f"Student name is {f_name} {l_name}")

#Method02, format() takes variable to be concatenate according to index 0
print ("Student name is {0} {1}".format(f_name, l_name))


#Condition Statement
result = "tie"  #"win"/"lose"/"tie"

if result == "win":
    print ("Pakistan's will celebrate")

elif result == "tie":
    print('Nothin happens')

else:
    print ("Pakistan's will sad")


#Condition practice
vehicle = input("Enter Vehicle name ")

if vehicle == "mehran":
  print(f"{vehicle} is small car")

elif vehicle == "corolla":
  print(f"{vehicle} is average car")

elif vehicle == "audi":
  print(f"{vehicle} is comfortable car")

else:
  print(f"{vehicle} is best car") 

#part
species = "cat"

if species == "cat":
  status = "ok"
  kingdom = "animal"
  print(f"Yes, it's a cat of kingdom {kingdom}")


#Greater >=
#Lesser <=
#equalto ==
#notequalto !=
#comparision ||

marks = float(input("Enter your marks "))

if marks >= 200.2:
  print(f"You have a Good marks, which is {marks}")

elif marks >= 100:
  print(f"You have a average marks,which is {marks}")

elif marks >= 50:
  print(f"You have a low marks,which is {marks}")

else:
  print(f"You are fail,your marks is {marks}")

#Increment
buy_score = 0
all_available = input("All fruits is Available  ")
fresh = input("Food is ")
fruit_price = input("Price is ")

if all_available == "Yes":
    buy_score += 10
if fruit_price == "low":
    buy_score += 5
if fresh == "Fresh":
    buy_score += 5
else:
    buy_score = 0

print(buy_score)

#and if both are true then answer true
#or if any one are true then answer true

percentage_inter  = int(input("Enter a percentage "))
age_limit = int(input("Enter a age "))

if (percentage_inter <= 60) or (age_limit <= 18):
  print("Eligible")

else:
  print("Not Eligible")

