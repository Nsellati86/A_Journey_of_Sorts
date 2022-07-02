from areaFunctions import bennysShop
from areaFunctions import guessPasskey
from areaFunctions import startAssassination
import time


#FIXME Having trouble with movement
def initGlobals():

    global pathia
    global this_area
    global player_inventory
    global game_over
    global player_name

    pathia = {
        'Home': {"Name": "Homestead",
                 "Description": "A modest home that you built with your own two hands. Big enough for three, but only occupied by you since the tragedy.",
                 "Item": "Backpack",
                 "Exits": {"f": "Bridge"}},
        'Bridge': {"Name": "Woodley Bridge",
                   "Description": "A wooden bridge extending over a ravine, guarded by Gus the Gatekeeper. There is a toll, and it's the only crossing for miles.",
                   "Item": "",
                   "Exits": {"f": "Forest", "b": "Home"}},
        'Forest': {"Name": "Farlow Forest",
                   "Description": "A thick, enchanted forest that is home to the Forester Elves. They require a magic password in order to be granted passage.",
                   "Item": "",
                   "Exits": {"f": "Village", "b": "Bridge"}},
        'Village': {"Name": "Venifur Village",
                    "Description": "A small, bustling village full of merchants, travelers, bards, and residents doing their best to live out their lives in peace.",
                    "Item": "",
                    "Exits": {"f": "Mountain", "b": "Forest"}},
        'Mountain': {"Name": "Pathia Mountain",
                     "Description": "A looming, earthly structure with such natural treachery that to ascend unprepared is to likely void oneself of life.",
                     "Item": "",
                     "Exits": {"f": "Castle", "b": "Village"}},
        'Castle': {"Name": "Castle Larkin",
                   "Description": "A grand castle belonging to the Larkin family ever since their Lordship began over these lands hundreds of years ago.",
                   "Item": "",
                   "Exits": {"b": "Mountain"}},
    }

    this_area = pathia["Home"]
    player_inventory = []
    game_over = False


def showInstructions():
    print('\033[94m' + '''
        Welcome to the land of Pathia. The year is 1292 and it is a time of turmoil since the death of the beloved Lord Lucian Larkin, with his Lordship having passed
        to his son, the despicable Archibald. The newly ordained Lord Archibald is a selfish, celf-centered, and loathsome man that nobody respects or cares much for.
        He cares naught for anyone or anything except himself and the ever-growing desire to acquire more wealth and more power no matter the cost.
    ''' + '\033[0m')
    time.sleep(2)

    print('\033[94m' + '''
        You are a solemn, simple, and good-hearted farmer who has worked and tilled his family land for as long as you can remember. Sadly, you have been on your own since
        your wife and son were taken by the plague a few years back. It was a pain like no other, but you are strong-willed, and you were able to get past that tragedy and
        move on with your life, despite having next to nothing to live for. You devote all of your time to the harvest since you live in a region where your annual climate 
        does not yield a winter, harvest is year-round. You keep to yourself and do not bother anybody; you only travel to the village marketplace to sell the bulk of the 
        fruits of your labor to your one and only friend and business associate Benny once a week so that you can pay your land's taxes every month.
    ''' + '\033[0m')
    time.sleep(2)

    print('\033[94m' + '''
        One day while working in your field, a representative of his Lordship approaches you with grave, potentially upsetting information; followed by a threat:
    ''' + '\033[91m' + '''
    
                        "By decree of his Lord Archibald Larkin: all those who own farmland within his domain will receive a tax increase
                        from 20% up to 85% which is to be paid by the first of every month in full. Any and all who do not wish to comply 
                        or do not pay their new amount of due taxes in full on or before the set date will have their lands and assets
                        seized and they will be thrown in jail without trial for a period of time no less that 10 years!"
                        
    ''' + '\033[0m' + '\033[32m' + '"This is outrageous!!!!!"' + '\033[0m' ''' you think to yourself. ''' + '\033[94m' + '''
        
        You decide that now is a good a time as any to embark on a quest to assassinate this piece-of-crap Lord and rid the land of his blatant tyranny.
        You have nothing left to lose anyway and you relish the prospect of seeing your wife and son again in the next life.
        You're getting tired of farming anyways.
        
        You head inside and have a hearty dinner before preparing for your Journey of Sorts in the morning. You set your backpack that holds your 
        compass and map on the kitchen table so that you can grab and go when you are ready to embark! Lord Archibald.....I'm coming for you.  
    ''' + '\033[0m')
    time.sleep(1)

    print('\033[36m' + '''
                    Game instructions:
                        Type the actions you wish to command the game to do.
                        If you wish to take an item and put into your inventory:
                            Type: "grab " + item
                        if you wish to move your character between areas:
                            Type: "forward" or "back" or "f" or "b"
                        
                    You must traverse through Pathia in order to confront the deplorable Lord Archibald.
                    You will not succeed in your mission unless you have added all FIVE quest items to your
                    inventory. Stay level-headed and keep your wits about you traveler! Good luck!!!
    
    ''' + '\033[0m')


def grab(item):
    global this_area
    global player_inventory

    if this_area["Item"].lower() == item and not (this_area["Item"] in player_inventory):
        player_inventory.append(this_area["Item"])
        this_area["Item"] = ''
    else:
        print("That item is not here.")


#FIXME Having trouble with movement
def parseCmd(command):
    l_cmd = command.lower()
    valid_directions = ["f", "b", "forward", "forwards", "forth", "back", "backward", "backwards"]

    if l_cmd in valid_directions:
        move(l_cmd[0])
    elif l_cmd.startswith("grab "):
        item = l_cmd.split(' ')[1]
        grab(item)
    else:
        print("Invalid command, please try again.")


def showStatus():
    area_name = this_area['Name']
    area_description = this_area['Description']
    area_item = this_area['Item']

    if area_item == '':
        area_item = "nothing"

    print('\033[1m' + f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ You are in {area_name} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + '\033[0m')
    print(f"{area_description}")
    print('\033[35m' + f"In this area: {area_item}" + '\033[0m')
    paths = ''
    this_path = ''

    for e in this_area["Exits"].keys():
        if e == "f":
            this_path = "forward"
        if e == "b":
            this_path = "backward"
        paths += f"{this_path} "

    for item in player_inventory:
        print(f"Current inventory: {item}")

    if len(player_inventory) == 5:
        print('\033[36m' + "\n-------> You have acquired all 5 quest items, you are ready to attempt to take out Lord Archibald. May luck be on your side!" + '\033[0m')

    print('\033[33m' + f"Possible paths are: {paths}" + '\033[0m')


def move(path):
    global this_area
    global game_over
    global player_inventory
    global player_name

    if path in this_area["Exits"].keys():
        area_name = this_area["Exits"][path]

        if area_name == "Castle":
            player_choice = input("\nYou are about to head towards Castle Larkin, are you sure you have what you need before you proceed further? (Y/N): ")
            if player_choice.lower() == "n":
                return
            this_area = pathia["Mountain"]
        else:
            print("\nInvalid choice, please try again.")

        if area_name == "Mountain":
            print("\nYou have reached the mouth of a deep and dark cave. You muster your confidence and proceed inside slowly and quietly.")
            time.sleep(1)
            print("A few minutes in, you reach an enormous, sleeping troll of a particularly menacing looking type! You definitely do not want to wake it.....")
            time.sleep(1)

            player_choice = input("\nAs you quietly sneak past this deadly, sleeping troll, you notice a treasure chest behind him. Do you want to try and pick the lock? (Y/N): ")
            if player_choice.lower() == "y":
                print("\nYou pull a pin from your pocket and begin to pick the lock. Your hand slips and you make a short, audible 'Screetch!!' The troll stirs, but does not wake.")
                time.sleep(1)
                print("You re-insert the pin and with a few more jiggles, you manage to open the chest! Inside is the famed 'Deepcuts-Dagger!' NICE.")
                player_inventory.append("Deepcuts-Dagger")
                print("You place your new weapon into your backpack and continue forth to the back exit that dumps you onto the path towards Castle Larkin. 'WHEW!'")
                this_area = pathia["Castle"]
            elif player_choice.lower() == "n":
                this_area = pathia[area_name]
                return
            else:
                print("Invalid choice, please try again.")

        if area_name == "Village":
            print("\nYou have reached Venifur Village. You must first head over to the Notary to make sure your affairs are in order. You really have no choice!")
            time.sleep(1)
            print("\nYou spoke with the Notary and have filed your last will and testament, which states the following: ")
            print('\033[3m' + f'''
            
                "In the untimely event of my death, I, {player_name}, wish that the entirety of my assets at the time of my passing, including my farmland, my livestock,
                 my home, and all possessions therein, be put up for auction exclusively to the benefit of the townsfolk of Venifur Village, Pathia. Any of my estate that is
                 left over not claimed in auction shall be evenly distributed only among those that qualify as the poorest among the populace of this beautiful country of ours."
                 ***** Specifics as to who can qualify for an evenly distributed share of my remaining estate have been filed with the town's Notary and confirmed by my lawyer *****
                 
            ''' + '\033[0m')
            time.sleep(1)
            print("\nNow that that is done, you should head over to the Village Convenience Shop to say farewell to your dearest friend and long-time purchaser of your goods, Benny.")
            time.sleep(1)
            print("\nBenny is out front of his shop observing the comings and goings of the Village folk, as he likes to do while his shop is empty.")
            time.sleep(1)
            print(f"\n\t\tBenny: Oh shit, hey {player_name}! It's damn good to see you, man. Whoa...wait a minute, you're giving off a certain kind of energy....hmmmm....")
            time.sleep(1)
            print("\n\t\tI'm no fool and you look like a man on a mission so....shit. I actually have gift for you. Let's head over into the shop and chat for a quick sec!")
            bennysShop()

        if area_name == "Forest":
            print("\nYou have been walking a short while on the winding path through Farlow Forest. You approach a looming wall of trees and brush that stretch for miles in either direction.")
            print("There's no way around this wall that wont take weeks and there's no climbing over it. As you approach the Elven-made doorway in the thick brush, you find that suddenly")
            print("you cannot move! The ground in front of the door is enchanted to stop any creature in their tracks and does not not let them proceed further unless released!")
            print("All you can do is wait for the inhabitants of this sacred, old forest to make contact with you. You don't know much, but you do know that the Forester Elves")
            print("value their home and their privacy as fiercely as they respect honor and wit. Hopefully you can convince them of your need to pass and that you mean them no trouble.")
            time.sleep(1)
            print("\nThe Captain of the border guard, Captain Lucian, appears at the top of the gate and looks down upon you for a few seconds...")
            print("\t\tCapt. Lucian: You there! What brings you so deep into Farlow Forest?'")
            print("\n\t'I am on an important mission to quite frankly assassinate the new Lord Archibald who has seen fit to threaten my livelihood among his first acts as Lord!")
            time.sleep(1)
            print("Not sure if blurting out the complete and total truth was the smartest thing to do, but it's too late now. You await his response....")
            time.sleep(1)
            print("\n\t\tCapt. Lucian: Alright traveler, I thank you for your open honesty. If this is truly your purpose, then we are with you! That new asshat of a Lord has waged war")
            print("\t\tupon our smaller woodland communities that are loyal to our Elven Lord, King Filarion Inakian. It is clear that Archibald's armies are slowly making their way here.")
            print("\t\tYou may pass through our kingdom unharmed....... IF....you can guess our passkey phrase. If you do so correctly, we will even give you a passing gift.")
            time.sleep(1)
            player_input = input("\n\t\t'Do you agree? Or should I release the enchantment holding you in place, only to have you driven back the way you came? (Y/N)").lower()[0]

            if player_input == 'y':
                guessPasskey()
            elif player_input == 'n':
                print("\nYour feet have been freed. Now you are staring at a dozen spears, glinting in the sunlight, beckoning you to turn around and head back the way you came.")
                time.sleep(1)
                this_area = pathia["Bridge"]
            else:
                print("Invalid input, please try again.")


def gameLoop():
    global this_area
    global player_inventory
    global player_name

    print("What is your character name going to be? (Type a first name only please) ", end=' ')
    player_name = input(">>> ")
    print(f"\nWelcome to 'A Journey of Sorts' {player_name}!")
    print("Prepare yourself for a " + '\033[92m' + "splendid journey" + '\033[0m' + " through the land of Pathia!")

    while not game_over:

        if this_area['Name'] == "Castle Larkin":
            area_name = this_area['Name']
            area_description = this_area['Description']
            print(f"\nYou have entered {area_name}, you are as prepared as you can be. Make sure to trust your senses, stay quiet, stay focused, and do not hesitate.")
            time.sleep(3)
            print(f"\n{area_description}")
            time.sleep(3)
            print("\nYou move in and out of the shadows, making your way to Lord Archibald's bedroom. You take great care not to be discovered because that would bring")
            print("you a whole heap of trouble in the form of palace guards, and then the large portion of Pathia's military that's stationed at the castle down upon your head.")
            time.sleep(3)
            print("\nYou have reached Archibald's bedroom, you quietly open the door, sneak in, and close it behind you. The Lord is fast asleep. You approach his bedside, pull")
            print("out your Deepcuts_Dagger, raise it above your head, bring your focus in on his chest right above his heart, aaaaaaaaaaand..........")
            time.sleep(3)
            startAssassination()
            continue

        showStatus()
        print("\nWhat would you like to do?", end=' ')
        command = input(">>> ")
        parseCmd(command)

    print("Would you like to play again? (Y/N) ", end=' ')
    play_again = input(">>> ")

    if play_again.lower() == "y":
        startGame()
    elif play_again.lower == "n":
        print('\033[91m' + "\nWe will see you next time for a Journey of Sorts!" + '\033[0m')
        exit(0)
    else:
        print("\nInvalid inout, please try again.")


def startGame():
    initGlobals()
    showInstructions()
    gameLoop()


pathia = {}
this_area = {}
player_inventory = []
game_over = False
startGame()
