print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
                      
''')
print("welcome to the treasure island\nyour mission is to find the treasure get ready!")
cross = input('you are at a crossroad where do you want to go type "left" or "right" \n')
cross_road = cross.lower()
if cross == "left":
    choice = input("you have reached the ocean type 'wait' to wait for a boat type 'swim' to swim across the ocean\n")
    if choice == "wait":
      house = input(" you have arrived at the island unharmed there is a house with 3 doors : 'red' 'yellow' 'blue' choose either of them\n")
      if house == "yellow":
        print("you win the treasure congrats now go home and sleep")
      else:
        print("you entered a room full of beasts who ate you game over")
    else:
      print("you were eaten by sharks game over")
    
    
else:
  print("you fell into a volcano game over")