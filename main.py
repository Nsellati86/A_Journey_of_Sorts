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
                   "Exits": {"f": "Village"}},
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
                "In the untimely event of my death, I, {player_name}, wish that the entirety of all my assets at the time of my passing, including my farmland, my livestock,
                 my home, and all possessions therein, be put up for auction exclusively to the benefit of the townsfolk of Venifur Village, Pathia. Any of my estate that is
                 left over not purchased in auction shall be evenly distributed only among those that qualify as the poorest among the populace of this beautiful country of ours.
            ''')
            time.sleep(1)
            print("\nNow that that is done, you should head over to the Village Convenience Shop to say farewell to your dearest friend and long-time purchaser of your goods, Benny.")
            time.sleep(1)
            print("\n\t'Hey Benny, I wanted to pop in to say that I'm swinging through town real quick on my way to Larkin Castle to have a quick word with our new Lord Archie.")
            print("\n\tIn case I don't get the chance to, I just wanted to say thank you for the long, fruitful partnership we had and for being such a good friend all of these years.'")
            time.sleep(1)
            print(f"\n\t\tNo sweat {player_name}, You are a stand up guy and you always gave me a good discount when I bought in bulk, but you've got that look in your eye my friend...")
            time.sleep(1)
            print("\n\t\tI'm no fool and you look like a man on a mission so....take these as a gift from your pal Benny and I wish you the best of luck on your 'chat' with our Lord!")
            print("\nBenny just gave you the Soundless-Boots! These will actually come very much in handy...In fact, I doubt you can pull this off without them. Benny's the BEST!")
            player_inventory.append("Soundless-Boots")
            print("\nYou put on your new boots, shake Benny's hand, and exit the store. You get back onto the road and continue on. The path to Castle Larkin winds up the mountain.")
            this_area = pathia[area_name]

        if area_name == "Forest":
            print("\nYou have been walking a short while on the path through Farlow Forest. You approach a looming wall of trees and brush that stretch for miles in either direction.")
            print("There's no way around this wall that wont take weeks and there's no climbing over it. As you approach the Elven-made doorway in the thick brush, you find that ")
            print("you can no longer move! The ground in front of the door is enchanted to stop any man or beast in their tracks and doesn't not let them proceed further!")
            print("All you can do is wait for the inhabitants of this sacred, old forest to make contact with you. You don't know much, but you do know that the Forester Elves ")
            print("Value their home and their privacy. Hopefully you can convince them of your need to pass through and that you mean them no trouble.")
            time.sleep(1)
