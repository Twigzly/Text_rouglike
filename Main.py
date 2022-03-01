#Welcome to this text based rouglike, i will try to implement inventory,health,damage,defence, and armour 
#maybe bosses every 10 levels.if you die of course then you lose
#i would also like to add like enemies that are randomnly generated depending on what are you are in
# i would like to add

#game name is arcanegate, arcane meaing, mystery, know by few.
#There will be a couple of enemies

# ENEMY ONE
# will be named porgy
#
# 
# 
# 
# 
# 
# 
# 
#

print("IF YOU HAVE ANY SUGGESTIONS FOR BETTER CODE JUST LET ME KNOW!")
while True :
      
    tutorial_0 = input("Welcome to Arcanegate, a text based, rougelike game.|press enter|s to skip the intro")
    if tutorial_0 == "s":
        print("skipped!")
        break
    
    tutorial_2 = input("Your quest is to go to planet glacio, and free the planet from the command of general Creng.|press enter|")
    print("To see your stats you will type s")
    print("if no instructions are printed press the enter button")
    
    if tutorial_0 == "":
        print("Perfect!, your getting the hang of it")
        break
    else:
        print("Just press the enter button!")
        continue

tutorial_1 = print("As time goes by everything will make more sense, but for now, just keep progressing and Have fun! Don't worry about anything because it will all be explained to you later on in the game.")
  
    
while True:
    name = input("what will your name be,|NOTE:you can not change this later!|might try to add this later on but for now this will have to do| ")
    
    confirm = input(name + " will be your name, is it correct?|y,n| ")
    if confirm == "y":
            print("ok Soon you will be the owner of a nice ship cruising around space!")
            break
    else:
            print("Ok lets try that again shall we?")
            continue
            
max_health = 1000
max_defence = 1000
max_accuracy = 1000
max_damage = 10000
#variables
health = 0
damage = 0
defence = 0
accuracy = 0
#warrior stats
w_health = 100
w_damage = 50
w_defence = 10
w_accuracy = 10
#mage state
m_health = 0
m_damage = 0
m_defence = 0
m_accuracy = 0
#archer stats
a_health = 0
a_damage = 0
a_defence = 0
a_accuracy = 0
a_magic = 0
#tank stats
t_health = 0
t_damage = 0
t_defence = 0
t_accuracy = 0
t_magic = 0
#choosing your class
class hello (object):
    t = 0
    e = 0
print (hello)

while True:      
    print("What type do you want to be?")
    clas = input("""
          [1]Warrior
          damage =
          health =
          damage = 
          
          [2]Mage
          damage =
          health =
          damage =
           
          [3]Archer
          damage =
          health =
          damage = 
          
          [4]Tank
          damage =
          health =
          damage = 
          """)
    
            #1st class
    
    if clas == "1":
        health = w_health
        defence = w_defence
        damage = w_damage
        accuracy= w_accuracy
        
        warrior_confirm = input("you will be a warrior correct?|y or n").lower()
        if warrior_confirm == "y":
            print("You are now a warrior, congrats!")
            break
        else:
            print("")
            continue
            
            #2nd class
            
    if clas == "2":
        health = m_health
        defence = m_defence
        damage = m_damage
        accuracy= m_accuracy
        mage_confirm = input("you will be a mage correct?|y or n").lower()
        if mage_confirm == "y":
            print("You are now a mage, congrats!")
            break
        else:
            print("")
            continue
            
            #3rd class
            
    if clas == "3":
        health = a_health
        defence = a_defence
        damage = a_damage
        accuracy= a_accuracy
        archer_confirm = input("you will be a archer correct?|y or n").lower()
        if archer_confirm == "y":
            print("You are now a archer, congrats!")
            break
        else:
            print("")
            continue
            
            #4th class
            
    if clas == "4":
        health = t_health
        defence = t_defence
        damage = t_damage
        accuracy= t_accuracy
        tank_confirm = input("you will be a tank correct?|y or n").lower()
        if tank_confirm == "y":
            print("You are now a tank, congrats!")
            break
        else:
            print("")
            continue            
            
#letting the player know what there stats will be
            
print("These will be your stats for now.")
print (health)
print(damage)
print(defence)
print(accuracy)



print("This is how much money you will have")
money = 100
print(money)
print("im not sure how to add armour and stuff so their can only be stat boosters and temp stuff(sorry)")


