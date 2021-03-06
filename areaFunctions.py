import time
import random

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


def bennysShop():
    global player_inventory
    global player_name
    global this_area
    global area_name

    area_name = this_area['Name']
    menu_prompt = ('\033[33m' + "\tAvailable commands:\n"
                   "\t(talk) with Benny\n"
                   "\t(accept) gift from Benny\n"
                   "\t(exit) Benny's shop\n"
                   "Enter command (use the word, or it's first letter, in parenthesis): " + '\033[0m')

    print("Welcome to Benny's Shop!\n")
    cust_input = input(menu_prompt).strip().lower()[0]

    while cust_input != 'e':
        if cust_input == 't':
            print('\033[32m' +
                "\n\tYou: Hey Benny, I just wanted to pop in to say that I'm swinging through town real quick on my way to Larkin Castle to have a quick word with our new Lord Archie.")
            print(
                "\tIn case I don't get the chance to, I just wanted to say thank you for the long, fruitful partnership we had and for being such a good friend all of these years.'" + '\033[0m')
            time.sleep(1)
            print('\033[33m' +
                f"\n\t\tBenny: No sweat {player_name}, You are a stand up guy and you always gave me a good discount when I bought in bulk, but you've got that look in your eye my friend..." + '\033[0m')
            time.sleep(1)
            print('\033[33m' +
                "\t\tMake sure you take this gift before you leave. Something tells me that you are going to need it...." + '\033[0m')
        elif cust_input == 'a':
            print(
                "\nBenny just gave you the Soundless-Boots! These will actually come very much in handy...In fact, it's doubtful that you can pull this off without them. Benny's the BEST!")
            player_inventory.append("Soundless-Boots")
            time.sleep(1)
            print("\nYou put on your new boots and shake Benny's hand.")
        elif cust_input == 'e':
            print(
                "\nYou exit Benny's store. You get back onto the road and continue on your journey of sorts. The path to Castle Larkin winds up the mountain.")
            this_area = pathia[area_name]
        else:
            print("Invalid command.")

        cust_input = input("Enter command (use the word, or it's first letter, in parenthesis): ").strip().lower()[0]


def guessPasskey():
    global this_area
    global player_inventory

    player_inventory = []
    print('\033[3m' + "\n\t\tCapt. Lucian: " + '\033[0m', end='')
    print('\033[1m' + '\033[94m' +
          "You must guess the passkey if you wish to be granted passage. You will enter a letter, and if it is contained within the word, it will be revealed." + '\033[0m')
    print('\033[1m' + '\033[94m' +
          "\t\tYou will be given 10 chances to reveal all of the letters of the passkey. If you run out of guesses before you can reveal the passkey, then you shall not pass." + '\033[0m')
    print()
    time.sleep(1)

    guesses = []
    wrongGuesses = 0
    listOfGuesses = []
    passkey = 'friend'

    guessed = "-" * len(passkey)
    for x in range(len(passkey)):

        while wrongGuesses != guesses:
            x = input("Passkey: %s  \nGuess a letter: " % guessed).lower()

            if x in passkey:
                print(x, "is in the passkey!")
                listOfGuesses.append(x)

                new_guessed = ""
                for index, char in enumerate(passkey):
                    if char == x:
                        new_guessed += x
                    else:
                        new_guessed += guessed[index]

                guessed = new_guessed

                if guessed == passkey:
                    time.sleep(1)
                    print("You have guessed the passkey!", end=' ')
                    print("The word was %s" % passkey)
                    print('\033[3m' + "\n\t\tCapt. Lucian: " + '\033[0m', end=' ')
                    print('\033[1m' + '\033[94m' +
                        "\n\t\tCongratulations, You have guessed correctly! You have earned safe passage through the kingdom and may proceed on to Venifur Village!" + '\033[0m')
                    print('\033[1m' + '\033[94m' +
                        "\t\tAlso, to aid you on this quest that we believe to be just and right, please accept this gift: " + '\033[0m')
                    time.sleep(1)
                    print("\nYou have received: Protection-Potion! This will surely help you if it comes down to having to fight your way to or from the the completion of your ultimate goal!")
                    player_inventory.append("Protection-Potion")
                    print("Current inventory: ", end=' ')
                    print(*player_inventory, sep=", ")
                    return True
                else:
                    print("Letters guessed so far:", listOfGuesses, "\n")

            else:
                print(x, "is not in the passkey.")
                wrongGuesses += 1
                print("Wrong guesses:", wrongGuesses)
                listOfGuesses.append(x)
                print("Letters guessed so far:", listOfGuesses, "\n")

    print("You did not guess the passkey! You must turn around and go back the way you came. Maybe the Captain will let you try again if you come back?")
    this_area = pathia["Bridge"]
    return False


def guessNumber():
    global player_inventory
    global this_area

    gusNum = random.randrange(1, 6)
    chances = 3
    guess = None

    print('\033[3m' + "\n\t\tGus: ", end='' + '\033[0m')
    print('\033[1m' + "Alrighty friend, if you want to cross the bridge, you will have to get past me. I am NOT super fun to try and get past, believe me.")
    print("\t\tYou have two options: Option (1): you can simply pay the toll, pass on by, and be on your merry way! Or..... Option (2): You can play my quick")
    print("\t\tgame and win a valuable prize along with passage to cross the bridge! The game is simple: you have three chances to guess the number I'm thinking")
    print("\t\tof, a number between 1 and 5. So, what will it be? Option (1) or (2)? (Be sure to enter the number only)" + '\033[0m')
    option_choice = int(input("\t\t>>> "))
    time.sleep(1)

    if option_choice == 1:
        print("\n\t\t'Well, that's alright. The toll will cost you 10 chits to cross, and have a merry day!")
        time.sleep(1)
        this_area = pathia["Forest"]

    elif option_choice == 2:
        print("\n\t\tGus: Option 2? Good choice my friend.")
        print("\t\tNow I'm thinking of a number between 1 and 5")

        while guess != gusNum and chances > 0:
            guess = int(input("\t\tTry to guess the number: "))

            if guess == gusNum:
                print("\t\tYou got it!")
                time.sleep(1)
                print("\nGus gave you the Obsurity-Cloak! Wow, this item will greatly come in handy! NICE!")
                print("You put your new item into your backpack, and continue forth on you quest.")
                print("Current inventory: ", end=' ')
                print(*player_inventory, sep=", ")
                this_area = pathia["Forest"]

            elif guess != gusNum:
                print("\t\tNot the right number friend, try again.")
                chances -= 1

            else:
                print("Invalid option choice, please try again.")
    else:
        print("Invalid option choice, please enter one of only 2 choice integers.")


def startAssassination():
    global game_over

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
    if len(player_inventory) == 5:
        print("\nCongratulations! Your Dagger was fast and true and you pierced Lord Archibald's heart before he even realized what happened! He looks at you one last time,")
        print("then his eyes darken, life leaves his body, and he slumps down onto the ground in a heap, never to rise again.")
    else:
        print("\nOh no, you did not have all five of the quest items to aid you in defeating Lord Archibald! Perhaps time will reverse a bit and you will have a second chance")
        print("to complete your mission; this time with everything you need to succeed! See you next time traveller." + '\033[94m' + "Thanks for playing!" + '\033[0m')
        game_over = True
