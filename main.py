import time
import random


def initGlobals():

    global pathia
    global this_area
    global player_inventory
    global game_over
    global player_name
    global gus_quest
    global lucian_quest
    global forest_quest
    global passphrase_quest
    global benny_quest
    global troll_quest

    pathia = {
        'Home': {"Name": "Homestead",
                 "Description": "A modest home that your family built centuries ago. So many memories contained within... Big enough for 12, but only occupied by you since the tragedy.",
                 "Item": "Backpack",
                 "Exits": {"f": "Bridge"}},
        'Bridge': {"Name": "Woodley Bridge",
                   "Description": "A wooden bridge extending over a ravine, newly guarded by Gus the Gatekeeper. Gus is a bear-sized man and this bridge is the only crossing for miles.",
                   "Item": "Wetstone",
                   "Exits": {"f": "Forest", "b": "Home"}},
        'Forest': {"Name": "Farlow Forest",
                   "Description": "A thick, enchanted forest that is home to the Forester Elves. They require a magic password in order to be granted passage.",
                   "Item": "Ring",
                   "Exits": {"f": "Village", "b": "Bridge"}},
        'Village': {"Name": "Venifur Village",
                    "Description": "A small, bustling village full of merchants, travelers, bards, and residents doing their best to live out their lives in peace.",
                    "Item": "Hat",
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
    gus_quest = ''
    lucian_quest = ''
    benny_quest = ''
    troll_quest = ''
    forest_quest = ''
    passphrase_quest = ''
    game_over = False


def showInstructions():
    print('\033[94m' + '''
        Welcome to the land of Pathia. The year is 1292 and it is a time of turmoil since the death of the beloved Lord Lucian Larkin, with his Lordship having passed
        to his son, the despicable Archibald. The newly ordained Lord Archibald is a selfish, celf-centered, and loathsome man that nobody respects or cares much for.
        He cares naught for anyone or anything except himself and the ever-growing desire to acquire more wealth and more power no matter the cost.
    ''' + '\033[0m')
    time.sleep(1)

    print('\033[94m' + '''
        You are a solemn, simple, and good-hearted farmer who has worked and tilled his family land for as long as you can remember. Sadly, you have been on your own since
        your wife and son were taken by the plague a few years back. It was a pain like no other, but you are strong-willed, and you were able to get past that tragedy and
        move on with your life, despite having next to nothing to live for. You devote all of your time to the harvest since you live in a region where your annual climate 
        does not yield a winter, harvest is year-round. You keep to yourself and do not bother anybody; you only travel to the village marketplace to sell the bulk of the 
        fruits of your labor to your one and only friend and business associate Benny once a week so that you can pay your land's taxes every month.
    ''' + '\033[0m')
    time.sleep(1)

    print('\033[94m' + '''
        One day while working in your field, a representative of his Lordship approaches you with grave, potentially upsetting information; followed by a threat:
    ''' + '\033[91m' + '''
                        "By decree of his Lordship Archibald Larkin: all those who own farmland within his domain will receive a tax increase
                        from 20% up to 85% which is to be paid by the first of every month in full. Any and all who do not wish to comply 
                        or do not pay their new amount of due taxes in full on or before the set date will have their lands and assets
                        seized and they will be thrown in jail without trial for a period of time no less that 10 years!"
    ''')
    time.sleep(1)

    print('''
    ''' + '\033[0m' + '\033[32m' + '"This is outrageous!!!!!"' + '\033[0m' ''' you think to yourself. ''')
    time.sleep(1)

    print('\033[94m' + '''
        
        You decide that now is a good a time as any to embark on a quest to assassinate this piece-of-crap Lord and rid the land of his blatant tyranny.
        You have nothing left to lose anyway and you relish the prospect of seeing your wife and son again in the next life. You're getting tired of farming anyways....
    ''')
    time.sleep(1)

    print('''
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
                        Nothing you need to type is case-sensitive and you can type the
                            first letter of anything except the items you must grab!
                        Press "CTRL + C" in the terminal if you wish to stop your journey 
                            before you reach the end of the game (All data will not be saved).
                        
                        
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


def parseCmd(command):
    l_cmd = command.lower()
    valid_directions = ["f", "b", "forward", "backwards", "forth", "back", "backward"]

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

    print('\033[1m' + f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Current location: {area_name} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + '\033[0m')
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

    print('\033[36m' + f"Current inventory: " + '\033[0m')
    for item in player_inventory:
        print('\033[36m' + item + '\033[0m')

    if len(player_inventory) == 5:
        print('\033[36m' + '\033[1m' + "-------> You have acquired at least 5 quest items and are ready to try to take out Lord Archibald! May luck be on your side.")
        print("*** Make sure you have a dagger of some sort in your inventory, or you will not succeed. There is a legend of a mystical Dagger")
        print("*** hidden somewhere in the mountain...maybe it will be worth looking around for, it's on your way to Castle Larkin anyways..." + '\033[0m')

    print('\033[33m' + f"\nPossible paths are: {paths}" + '\033[0m')


def move(path):
    global this_area
    global player_name
    global gus_quest
    global lucian_quest
    global forest_quest
    global passphrase_quest
    global troll_quest
    global benny_quest

    if path in this_area["Exits"].keys():
        location = this_area["Exits"][path]

        if location == "Castle":
            print("\nYou are about to enter Castle Larkin, in which case you must begin your final mission to kill Lord Archibald. Are you sure you want to proceed? (Y/N) ", end=' ')
            player_input = input("(Make sure you have some sort of Dagger in your inventory!)" + '\033[1m' + " >>> " + '\033[0m')

            if player_input.lower() == "n":
                return
        this_area = pathia[location]

        if location == "Castle" and player_inventory == ["Deepcuts-Dagger"]:
            area_description = this_area['Description']
            print(f"\nYou have entered {location}, you are as prepared as you can be. Make sure to trust your senses, stay quiet, stay focused, and do not hesitate.")
            time.sleep(3)
            print(f"\n{area_description}")
            time.sleep(3)
            print("\nYou move in and out of the shadows, making your way to Lord Archibald's bedroom. You take great care not to be discovered because that would bring")
            print("you a whole heap of trouble in the form of palace guards, and then the large portion of Pathia's military that's stationed at the castle down upon your head.")
            time.sleep(5)
            print("\nYou have reached Archibald's bedroom, you quietly open the door, sneak in, and close it behind you. The Lord is fast asleep. You approach his bedside, pull")
            print("out your Deepcuts-Dagger, raise it above your head, bring your focus in on his chest right above his heart, aaaaaaaaaaand..........")
            time.sleep(3)
            startAssassination()

        if troll_quest == 1 and location == "Mountain":
            time.sleep(1)
            print("\nYou re-enter the mountain cave thinking 'Damn! I gotta try and sneak past that troll again!' ....Just as you start to move forward.....")
            time.sleep(5)
            print("You look to your right just behind you and realize that there is a shortcut around the troll to the back exit that dumps you on the path to Castle Larkin!")
            time.sleep(5)
            this_area = pathia["Castle"]

        else:
            if location == "Mountain":
                print("\nYou have reached the mouth of a deep and dark cave. You muster your confidence and proceed inside slowly and quietly.")
                time.sleep(3)
                print("A few minutes in, you reach an enormous, sleeping troll of a particularly menacing looking type! You definitely do not want to wake it.....")
                time.sleep(3)
                print("\nAs you quietly sneak past this deadly, sleeping troll, you notice a treasure chest behind him.")
                print("Do you want to try and pick the lock? (Y/N): ", end=' ')
                player_choice = input("(You probably REALLY REALLY should!)" + '\033[1m' + "  >>> " + '\033[0m')

                if player_choice.lower() == "y":
                    print("\nYou pull a pin from your pocket and begin to pick the lock. Your hand slips and you make a short, very audible 'Screetch!!!' The troll stirs, but does not wake.")
                    time.sleep(5)
                    print("That was close.... You re-insert the pin and with a few more jiggles, you manage to open the chest! Inside is the legendary 'Deepcuts-Dagger!'")
                    player_inventory.append("Deepcuts-Dagger")
                    time.sleep(5)
                    print("You place your new weapon into your backpack and continue forth to the back exit that dumps you onto the path towards Castle Larkin. 'WHEW!'")
                    time.sleep(5)
                    troll_quest = 1
                elif player_choice.lower() == "n":
                    troll_quest = ''
                    this_area = pathia[location]
                    return
                else:
                    print("Invalid choice, please try again.")

        if benny_quest == 1 and location == "Village":
            time.sleep(1)
            print('\033[3m' + "\n\t\tBenny: " + '\033[0m' + '\033[33m' +
                  f"Hey {player_name}, it's nice of you to revisit me, but you have your item and we've said all that needs to be said, so...take care and good luck!" + '\033[0m')
            benny_quest = 1
            this_area = pathia[location]
        else:
            if location == "Village":
                print("\nYou have reached Venifur Village. You must first head over to the Notary to make sure your affairs are in order. You really have no choice!")
                time.sleep(3)
                print("\nYou spoke with the Notary and have filed your last will and testament, which states the following: ")
                print('\033[3m' + '\033[1m' + f'''
    
                        "In the untimely event of my death, I, {player_name}, wish that the entirety of my assets at the time of my passing, including my farmland, my livestock,
                        my home, and all possessions therein, be put up for auction exclusively to the benefit of the townsfolk of Venifur Village, Pathia. Any of my estate that is
                        left over not claimed in auction shall be evenly distributed only among those that qualify as the poorest among the populace of this beautiful country of ours."
                        ***** Specifics as to who can qualify for an evenly distributed share of my remaining estate have been filed with the town's Notary and confirmed by my lawyer *****
    
                        ''' + '\033[0m')
                time.sleep(10)
                print("\nNow that that is done, you should head over to the 'Village Convenience Shop' to say farewell to your dearest friend and long-time purchaser of your goods, Benny.")
                time.sleep(5)
                print("Benny is out front of his shop observing the comings and goings of the Village folk, as he likes to do while his shop is empty.")
                time.sleep(3)
                print('\033[3m' + "\n\t\tBenny: " + '\033[0m' + '\033[33m' +
                      f"Oh shit, hey {player_name}! It's damn good to see you, man. Whoa...wait a minute, you're giving off a certain kind of energy....hmmmm....")
                time.sleep(2)
                print("\t\tI'm no fool and you look like a man on a mission so....shit. I actually have gift for you. Let's head over into the shop and chat for a quick sec!" + '\033[0m')
                bennysShop()

        if lucian_quest == 1 and location == "Forest":
            time.sleep(1)
            print('\033[3m' + "\n\t\tCapt. Lucian: " + '\033[0m' +
                  '\033[94m' + "Welcome back traveler! I trust everything is progressing smoothly on your quest? Just passing back through? We wish you the best of luck again!" + '\033[0m')
            time.sleep(2)
            this_area = pathia[location]
            lucian_quest = 1
        elif forest_quest == 1 and location == "Forest":
            time.sleep(1)
            print('\033[3m' + "\n\t\tCapt. Lucian: " + '\033[0m' +
                  '\033[94m' + f"Hello again {player_name}...are you back to try and gain passage to Venifur Village? You will still need to guess our passphrase. I'll go ahead and assume that you do!")
            time.sleep(5)
            guessPasskey()
        elif passphrase_quest == 1 and location == "Forest":
            print('\033[3m' + "\n\t\tCapt. Lucian: " + '\033[0m' +
                  '\033[94m' + f"Hello {player_name}, I see that you have come back. I presume you want to try to guess our passphrase again? Okay, best of luck traveler." + '\033[0m')
            time.sleep(5)
            guessPasskey()
        else:
            if location == "Forest":
                print("\nYou have been walking a short while on the winding path through Farlow Forest. You approach a looming wall of trees and brush that stretch for miles in either direction.")
                print("There's no way around this wall that won't take weeks and there's no climbing over it. As you approach the Elven-made doorway in the thick brush, you find that suddenly")
                print("you cannot move! The ground in front of the door is enchanted to stop any creature in their tracks and does not not let them proceed further unless released!")
                print("All you can do is wait for the inhabitants of this sacred, old forest to make contact with you. You do not know much, but you do know that the Forester Elves")
                print("value their home and their privacy as fiercely as they respect honor and wit. Hopefully you can convince them of your need to pass and that you mean them no trouble.")
                print("It would seem that Forester Elves have fortified their forest kingdom and that of the road used for safe travel through their domain. The elves have always allowed passage")
                print("through here. It is a bit alarming because this road is traversed by merchants and travelers alike. We probably have that despicable new Lord Archibald to thank for this...")
                time.sleep(1)
                print("\nThe leader of the border guard, Captain Lucian, appears at the top of the gate and looks down upon you for a few seconds...")
                time.sleep(5)
                print('\033[3m' + "\n\t\tCapt. Lucian: " + '\033[0m' +
                      '\033[94m' + "You there! What is your name and what brings you so deep into Farlow Forest during these trying times?!" + '\033[0m')
                time.sleep(3)
                print('\033[3m' + "\n\tYou: " + '\033[0m' +
                    '\033[32m' + f"My name is {player_name}. I'm on a mission to kill the new Lord Archibald, who has seen fit to threaten the livelihoods of all common folk since becoming Lord!" + '\033[0m')
                time.sleep(5)
                print("\nNot sure if blurting out the complete and total truth was the smartest thing to do, but it's too late now. You await his response....")
                time.sleep(4)
                print('\033[3m' + "\n\t\tCapt. Lucian: " + '\033[0m' +
                    '\033[94m' + "Alright traveler, I thank you for your open honesty. If this is truly your purpose, then we are with you! That new asshat of a Lord has waged war")
                print("\t\tupon our smaller woodland communities that are loyal to our Elven Lord, King Filarion Inakian. It is clear that Archibald's armies are slowly making their way here.")
                print("\t\tYou may pass through our kingdom unharmed....... IF...... you can guess our passkey phrase. If you do so correctly, we will even give you a passing gift." + '\033[0m')
                time.sleep(12)
                print('\033[94m' + "\n\t\tDo you agree? Or should I release the enchantment holding you in place and have you driven back the way you came?" + '\033[0m')
                player_input = input('\033[1m' + "\n\t\tYes " + '\033[0m' + "(Guess the passphrase) or " + '\033[1m' + "No? >>> " + '\033[0m').lower()[0]

                if player_input == 'y':
                    guessPasskey()
                elif player_input == 'n':
                    print("\nYour feet have been freed. Now you are staring at a dozen spears, glinting in the sunlight, beckoning you to turn around and head back the way you came.")
                    print("Well, not much you can do except temporarily retreat...I'm sure if you hang with Gus for a few and then come back, they'll let you choose again....maybe.")
                    forest_quest = 1
                    time.sleep(7)
                    print('\033[3m' + "\n\tYou: " + '\033[0m' +
                          '\033[32m' + "I wonder if I will have to go through that whole back and forth again? Maybe I should just try to guess the passphrase." + '\033[0m')
                    time.sleep(5)
                    this_area = pathia["Bridge"]
                else:
                    print("Invalid input, please try again.")

        if gus_quest == 1 and location == "Bridge":
            time.sleep(1)
            print('\033[3m' + "\n\t\tGus: ", end=' ' + '\033[0m')
            print('\033[37m' + '\033[1m' + "It's good to see you again! Did you miss ol' Gus? How's that item I gave you treating ya? I hope you like it." + '\033[0m')
            time.sleep(3)
            print("\nNow that you have completed the Bridge mini-quest and received Gus's treasure, there is no more need to return to Homestead, or the Bridge", end=' ')
            print("for that matter! Onward!!")
            time.sleep(5)
            gus_quest = 1
            this_area = pathia[location]
        else:
            if location == "Bridge":
                print("\nYou have come to a beautiful bridge that was crafted long ago as a means to cross over Pathia Ravine and is the only crossing for hundred of miles in either direction.")
                time.sleep(5)
                print("\nYou have used this bridge thousands of times on your travels to and from Venifur Village. Something is new though... There is now a barrier restricting access to cross")
                print("and now there is quite a large man guarding that new barrier.....I have no doubt that this new addition is thanks to Lord Archibald...such a swell guy...")
                time.sleep(7)
                print('\033[3m' + "\n\t\tGus: ", end=' ' + '\033[0m')
                print('\033[37m' + "Welcome traveler! If you want to cross the bridge, you will have to get past me. By decree of our new Lord Archibald, all must now pay a new toll.")
                time.sleep(3)
                print("\n\t\tYou have two options:")
                time.sleep(2)
                print('\033[1m' + "\n\t\tOption (1):" + '\033[0m' + " You can simply pay the toll, pass on by, and be on your merry way! Or.....")
                time.sleep(3)
                print('\033[1m' + "\t\tOption (2):" + '\033[0m' + " You can play my quick game and win a valuable prize along with passage to cross the bridge!")
                time.sleep(3)
                print("\n\t\tThe game is simple: you have three chances to guess the number that I'm thinking of, which will be a number between 1 and 5. So, what will it be?")
                time.sleep(3)
                print('\033[1m' + "\n\t\tOption 1" + '\033[0m' + " (Pay the toll) or " + '\033[1m' + "Option 2" + '\033[0m' + " (Play my game)? (Be sure to enter the number only)" + '\033[0m')
                option_choice = int(input("\t\t>>> "))

                if option_choice == 1:
                    print('\033[3m' + "\n\t\tGus: " + '\033[0m', end=' ')
                    print('\033[37m' + "Well, that's alright. Not much of a guesser, eh? Just so you know, you must pay the toll for each crossing, but my offer for the prize still stands.")
                    print("\t\tThe toll will run you 10 chits to cross, and have a merry day!" + '\033[0m')
                    time.sleep(5)
                    print("\nYou pay the toll and as you begin to cross, you cannot help but feel that maybe you should have tried to guess after all......oh well, maybe next time.")
                    time.sleep(2)
                    gus_quest = ''
                    this_area = pathia[location]
                elif option_choice == 2:
                    print('\033[3m' + "\n\t\tGus: " + '\033[0m', end=' ')
                    print('\033[37m' + "Option 2? Good choice my friend.")
                    print("\t\tNow, I'm thinking of a number between 1 and 5" + '\033[0m')
                    guessNumber()
                else:
                    print("Invalid option choice, please enter either '1' or '2'")
    else:
        print("\nYou cannot go that way! Please select a valid path choice (f or b)")


def bennysShop():
    global player_inventory
    global player_name
    global this_area
    global area_name
    global benny_quest

    area_name = pathia["Village"]

    menu_prompt = ('\033[33m' + "\tAvailable commands:\n"
                   "\t(talk) with Benny\n"
                   "\t(accept) gift from Benny\n"
                   "\t(exit) Benny's shop\n" + '\033[0m'
                   "\nEnter command (use the word, or it's first letter, in parenthesis): ")
    print()

    print('\033[1m' + "\nWelcome to Benny's Shop!\n" + '\033[0m')
    cust_input = input(menu_prompt).strip().lower()[0]

    while cust_input != 'e':
        if cust_input == 't':
            print('\033[3m' + "\n\tYou: " + '\033[0m' +
                '\033[92m' + "Hey Benny, I just wanted to pop in to say that I'm swinging through town real quick on my way to Larkin Castle to have a quick word with our new Lord Archie.")
            print("\tIn case I don't get the chance to, I just wanted to say thank you for the long, fruitful partnership we had and for being such a good friend all of these years.'" + '\033[0m')
            time.sleep(5)
            print('\033[3m' + "\n\t\tBenny: " '\033[0m' +
                  '\033[33m' +
                  f"No sweat {player_name}, You are a stand up guy and you always gave me a good discount when I bought in bulk, but you've got a certain look in your eye my friend..." + '\033[0m')
            print('\033[33m' + "\t\tMake sure you take my gift before you leave. Something tells me that you are going to need it...." + '\033[0m')
            time.sleep(5)
        elif cust_input == 'a':
            print("\nBenny just gave you the Soundless-Boots! These will actually come very much in handy...In fact, it's doubtful that you can pull this off without them. Benny's the BEST!")
            player_inventory.append("Soundless-Boots")
            time.sleep(5)
            print("\nYou put on your new boots and shake Benny's hand.")
            benny_quest = 1
            #this_area = pathia["Village"]
        elif cust_input == 'e':
            print("\nYou exit Benny's store. You get back onto the road and continue on your journey of sorts. The path to Castle Larkin winds up the mountain.")
            this_area = pathia[area_name]
        else:
            print("Invalid command.")

        cust_input = input("\nEnter command (use the word, or it's first letter, in parenthesis): ").strip().lower()[0]


def guessPasskey():
    global this_area
    global player_inventory
    global lucian_quest
    global passphrase_quest

    print('\033[94m' + "You must guess the passphrase if you wish to be granted passage. You will give us a letter, and if it is contained within the passphrase, it will be revealed to you.")
    print("\t\tYou will be given 15 chances to reveal all of the letters of the passphrase. If you run out of guesses before you can reveal the passphrase, then you shall not pass." + '\033[0m')
    print()
    time.sleep(7)

    guesses = 15
    wrongGuesses = 0
    listOfGuesses = []
    word = ['friend']
    words = ['friend',
             'pathia',
             'elves',
             'passage',
             'password',
             'forest']

    passkey = random.choice(word)
    guessed = "-" * len(passkey)
    for x in range(len(passkey)):

        while wrongGuesses != guesses:
            x = input("Passphrase: %s  \nGuess a letter: " % guessed).lower()

            if x in passkey:
                print(x, "is in the passphrase!")
                listOfGuesses.append(x)

                new_guessed = ""
                for index, char in enumerate(passkey):
                    if char == x:
                        new_guessed += x
                        wrongGuesses += 1
                    else:
                        new_guessed += guessed[index]

                guessed = new_guessed

                if guessed == passkey:
                    time.sleep(2)
                    print("You have guessed the passphrase!", end=' ')
                    print("The word was: " + '\033[4m' + passkey + '\033[0m')
                    print('\033[3m' + "\n\t\tCapt. Lucian: " + '\033[0m', end=' ')
                    print('\033[94m' +
                        "Congratulations, You have guessed correctly! You have earned safe passage through the Forester Elf kingdom and may proceed on to Venifur Village!")
                    time.sleep(3)
                    print("\t\tAlso, to aid you on this quest that we believe to be just and right, please accept this gift: " + '\033[0m')
                    time.sleep(3)
                    print("\nYou have received: Protection-Potion! This will surely help you if it comes down to having to fight your way to or from the the completion of your ultimate goal!")
                    player_inventory.append("Protection-Potion")
                    lucian_quest = 1
                    time.sleep(3)
                    this_area = pathia["Forest"]
                    return True
                else:
                    print("Letters guessed so far:", listOfGuesses, "\n")

            else:
                print(x, "is not in the passkey.")
                wrongGuesses += 1
                print("Guesses:", wrongGuesses)
                listOfGuesses.append(x)
                print("Letters guessed so far:", listOfGuesses, "\n")

        print("You did not guess the passphrase! You must turn around and go back the way you came" + '\033[3m' + " (especially if you want to try again)." + '\033[0m')
        print("Maybe Captain Lucian will let you try again if you come back? Go say hi to Gus and come right back to the forest.")
        time.sleep(5)
        lucian_quest = ''
        passphrase_quest = 1
        this_area = pathia["Bridge"]
        return False


def guessNumber():
    global player_inventory
    global this_area
    global gus_quest

    gusNum = 1 # random.randrange(1, 3)
    chances = 3
    playerGuess = None

    while playerGuess != gusNum and chances > 0:
        playerGuess = int(input('\033[37m' + "\t\tTry to guess the number: " + '\033[0m'))

        if playerGuess == gusNum:
            print('\033[37m' + "\n\t\tYou guessed the right number, friend!" + '\033[0m')
            time.sleep(1)
            print("\nGus gave you the Obscurity-Cloak! When you wear this, you become very difficult to see clearly! Wow, this item will undoubtedly come in handy!")
            print("You put on your new cloak............. Excellent! Now you are ready to cross the bridge and continue forth on your quest.")
            player_inventory.append("Obscurity-Cloak")
            gus_quest = 1
            time.sleep(5)
            this_area = pathia["Bridge"]
        elif playerGuess != gusNum:
            print('\033[37m' + "\n\t\tNot the right number, try again." + '\033[0m')
            chances -= 1
            playerGuess = int(input('\033[37m' + "\t\tTry to guess the number: " + '\033[0m'))
        else:
            print("Invalid choice, please trying guessing an integer.")


def startAssassination():
    global game_over
    global player_inventory

    print("\nLord Archibald wakes up from his slumber to see you standing over him about to plunge your Dagger into his heart! He immediately grabs the sword that he")
    print("keeps next to his bed and meets your weapon with a high-pitched 'CLANG!!' just as you were about to end his life. Things have gotten a little more complicated now!")
    time.sleep(1)
    print("\n\t\tLord Archibald: " + '\033[91m' + "Who the hell are you and what the hell do you think you are doing in my room?!?!" + '\033[0m')
    time.sleep(2)
    print('\033[92m' + "\n\tI am a simple man who was threatened by you to lose all that I have left, and who has decided that Pathia will be better off without your tyrannical rule!" + '\033[0m')
    time.sleep(2)
    print("\n\t\tLord Archibald: " + '\033[91m' + "Clearly you want me dead then, well I will not make it easy for you. If you truly want to end me, come at me!!!" + '\033[0m')
    time.sleep(2)
    print("\nYou are both standing at opposite sides of the massive, ostentatious bedroom. There is a glint of determination in your eyes and a burning rage in Lord Archibald's...")
    time.sleep(2)
    print("For one moment, there is a silence and clarity that washes over your mind...and then the urge to strike.....You LUNGE at Lord Archibald! He mimics with less ferocity")
    time.sleep(1)

    for i in range(50):
        for j in range(1000000):
            pass
        print(".", end='', flush=True)

    print()
    if len(player_inventory) == 5 and player_inventory == ["Deepcuts_Dagger"]:
        print("\nCongratulations! Your Dagger was fast and true and you pierced Lord Archibald's heart before he even realized what happened! He looks at you one last time,")
        print("then his eyes darken, life leaves his body, and he slumps down onto the ground in a heap, never to rise again.")
    else:
        print("\nOh no, you did not have all five of the quest items to aid you in defeating Lord Archibald! Perhaps time will reverse a bit and you will have a second chance")
        print("to complete your mission; this time with everything you need to succeed! See you next time traveller." + '\033[94m' + "Thanks for playing!" + '\033[0m')
        game_over = True


def gameLoop():
    global this_area
    global player_inventory
    global player_name
    global location

    print("What is your character name going to be? ", end=' ')
    player_name = input('\033[1m' + ">>> " + '\033[0m')
    print(f"\n\nWelcome to 'A Journey of Sorts' {player_name}!")
    print("Prepare yourself for a " + '\033[92m' + "splendid journey" + '\033[0m' + " through the land of Pathia!")
    time.sleep(3)

    while not game_over:

        if this_area['Name'] == "Castle Larkin":
            location = this_area['Name']
            area_description = this_area['Description']
            print(f"\nYou have entered {location}, you are as prepared as you can be. Make sure to trust your senses, stay quiet, stay focused, and do not hesitate.")
            time.sleep(3)
            print(f"\n{area_description}")
            time.sleep(3)
            print("\nYou move in and out of the shadows, making your way to Lord Archibald's bedroom. You take great care not to be discovered because that would bring")
            print("you a whole heap of trouble in the form of palace guards, and then the large portion of Pathia's military that's stationed at the castle down upon your head.")
            time.sleep(5)
            print("\nYou have reached Archibald's bedroom, you quietly open the door, sneak in, and close it behind you. The Lord is fast asleep. You approach his bedside, pull")
            print("out your Deepcuts-Dagger, raise it above your head, bring your focus in on his chest right above his heart, aaaaaaaaaaand..........")
            time.sleep(5)
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
        print('\033[91m' + "\nWe will see you next time for a" + '\033[4m' + "'Journey of Sorts!'" + '\033[0m')
        exit(0)
    else:
        print("\nInvalid input, please try again.")


def startGame():
    initGlobals()
    showInstructions()
    gameLoop()


pathia = {}
this_area = {}
player_inventory = []
game_over = False
startGame()
