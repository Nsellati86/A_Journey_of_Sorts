import time

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

    menu_prompt = ("\tAvailable commands:\n"
                   "\t(talk) with Benny\n"
                   "\t(accept) gift from Benny\n"
                   "\t(exit) Benny's shop\n"
                   "Enter command (use the word, or it's first letter, in parenthesis): ")

    print("Welcome to Benny's Shop!\n")
    cust_input = input(menu_prompt).strip().lower()[0]

    while cust_input != 'e':
        if cust_input == 't':
            print(
                "\n\t'Hey Benny, I just wanted to pop in to say that I'm swinging through town real quick on my way to Larkin Castle to have a quick word with our new Lord Archie.")
            print(
                "\n\tIn case I don't get the chance to, I just wanted to say thank you for the long, fruitful partnership we had and for being such a good friend all of these years.'")
            time.sleep(1)
            print(
                f"\n\t\tNo sweat {player_name}, You are a stand up guy and you always gave me a good discount when I bought in bulk, but you've got that look in your eye my friend...")
            time.sleep(1)
            print(
                "\n\t\tMake sure you take this gift before you leave. Something tells me that you are going to need it....")
        elif cust_input == 'a':
            print(
                "\nBenny just gave you the Soundless-Boots! These will actually come very much in handy...In fact, it's doubtful that you can pull this off without them. Benny's the BEST!")
            player_inventory.append("Soundless-Boots")
            time.sleep(1)
            print("\nYou put on your new boots, shake Benny's hand.")
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

    passkey = ['friend']

    word = passkey
    num_guesses = 10
    hidden_word = '-' * len(word)
    guess = 1

    print("\n\t\t'You must guess the passkey if you wish to be granted passage. You will enter a letter, and if it is contained within the word, it will be revealed.")
    print("\n\t\tYou will be given 10 chances to reveal all of the letters of the passkey. If you run out of guesses before you can reveal the passkey, then you shall not pass.")
    time.sleep(1)

    while guess <= num_guesses and '-' in hidden_word:
        print(hidden_word)
        user_guess = input("Enter a character (guess #{}): ".format(guess))

        if len(user_guess) == 1:
            num_occurrences = word.count(user_guess)
            position = -1

            for occurrence in range(num_occurrences):
                position = word.find(user_guess, position + 1)
                hidden_word = hidden_word[:position] + user_guess + hidden_word[position + 1:]

            guess += 1

    if not '-' in hidden_word:
        print("\n\tThe passkey is {}".format(word))
        time.sleep(1)
        print("\n\t\t'Congratulations, You have guessed correctly! You have earned safe passage through the kingdom and may proceed on to Venifur Village! Also, to help aid you")
        print("\n\t\ton this quest that we believe to be just and right, please accept this gift: '")
        time.sleep(1)
        print("\nYou have received: Protection-Potion! This will surely help you if it comes down to having to fight your way to or from the the completion of your ultimate goal!")
        player_inventory.append("Protection-Potion")
    else:
        print("\nYou did not reveal the passkey and you now must turn around and go back the way you came! Maybe they will let you try again if you leave and come back?")
        this_area = pathia["Bridge"]

