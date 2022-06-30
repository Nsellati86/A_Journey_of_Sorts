from areaFunctions import bennysShop
from areaFunctions import guessPasskey
import time


def initGlobals():

    global pathia
    global this_area
    global player_inventory
    global game_over
    global player_name

    pathia = {
        'Home': {"Name": "Homestead",
                 "Description": "A modest home, that you built with your own two hands. Big enough for three, but only occupied by you since the tragedy.",
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

    this_area = pathia["Homestead"]
    player_inventory = []
    game_over = False
    player_name = input("What is your character name going to be? >>> ")
    print(f"Welcome to 'A Journey of Sorts' {player_name}!")


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
            this_area = pathia[area_name]
        else:
            print("\nInvalid choice, please try again.")

        if area_name == "Mountain":
            print("\nYou have reached the mouth of a dark cave. You adorn your Obscurity Cloak and proceed inside slowly.")
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
            print(f'''
            
                "In the untimely event of my death, I, {player_name}, wish that the entirety of my assets at the time of my passing, including my farmland, my livestock,
                 my home, and all possessions therein, be put up for auction exclusively to the benefit of the townsfolk of Venifur Village, Pathia. Any of my estate that is
                 left over not claimed in auction shall be evenly distributed only among those that qualify as the poorest among the populace of this beautiful country of ours.
                 ***** Specifications as to who can qualify for an even distribution of my left over estate filed with the town's Notary and confirmed by my lawyer *****
                 
            ''')
            time.sleep(1)
            print("\nNow that that is done, you should head over to the Village Convenience Shop to say farewell to your dearest friend and long-time purchaser of your goods, Benny.")
            time.sleep(1)
            print("\nBenny is out front of his shop observing the comings and goings of the Village folk, as he likes to do while his shop is empty.")
            time.sleep(1)
            print(f"\n\t\tOh shit, hey {player_name}! It's damn good to see you, man. Whoa...wait a minute, you're giving off a certain kind of energy....hmmmm....")
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
            print("\nThe Captain of the border guard appears at the top of the gate and looks down upon you for a few seconds...")
            print("\n\t\t'You there! What brings you so deep into Farlow Forest?'")
            print("\n\t'I am on an important mission to quite frankly assassinate the new Lord Archibald who has seen fit to threaten my livelihood among his first acts as Lord!'")
            print("Not sure if blurting out the complete and total truth was the smartest thing to do, but it's too late and now you await his response....")
            time.sleep(1)
            print("\n\t\t'Alright traveler, I thank you for your open honesty. If this is truly your purpose, then we are with you! That new asshat of a Lord has waged war upon")
            print("\n\t\tour smaller woodland communities that are loyal to our Elven Lord, King Filarion Inakian. It is clear that Archibald's army are making their way here.")
            print("\n\t\tYou may pass through our kingdom unharmed....... IF....you can guess our passkey phrase. If you do so correctly, we will even give you a parting gift.'")
            time.sleep(1)
            player_input = input("\n\t\t'Do you agree? Or should I release the enchantment holding you in place, only to have you driven back the way you came? (Y/N)").lower()[0]

            if player_input == 'y':
                guessPasskey()
            elif player_input == 'n':
                print("Your feet have been freed. Now you are staring at a dozen spears, glinting in the sunlight, beckoning you to turn around and head back the way you came.")
                time.sleep(1)
                this_area = pathia["Bridge"]
            else:
                print("Invalid input.")



def grab(item):
    global this_area
    global player_inventory

    if this_area["Item"].lower() == item and not (this_area["Item"] in player_inventory):
        player_inventory.append(this_area["Item"])
        this_area["Item"] = ''
    else:
        print("That item is not here.")


initGlobals()
