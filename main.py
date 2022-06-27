import time


def initGlobals():

    global pathia
    global this_area
    global player_inventory
    global game_over

    pathia = {
        'Home': {"Name": "Homestead",
                 "Description": "A modest home, that you built with your own two hands. Big enough for three, but only occupied by you since the tragedy.",
                 "Item": "Backpack",
                 "Exits": {"f": "Bridge"}},
        'Bridge': {"Name": "Woodley Bridge",
                   "Description": "A wooden bridge extending over a ravine, guarded by Gus the Gatekeeper. There is a toll, and it's the only crossing for miles.",
                   "Item": "Obscurity Cloak",
                   "Exits": {"f": "Forest", "b": "Home"}},
        'Forest': {"Name": "Farlow Forest",
                   "Description": "A thick, enchanted forest that is home to the Forester Elves. They require a magic password in order to be granted passage.",
                   "Item": "Protection Potion",
                   "Exits": {"f": "Village"}},
        'Village': {"Name": "Venifur Village",
                    "Description": "A small, bustling village full of merchants, travelers, bards, and residents doing their best to live out their lives in peace.",
                    "Item": "Soundless Boots",
                    "Exits": {"f": "Mountain", "b": "Forest"}},
        'Mountain': {"Name": "Pathia Mountain",
                     "Description": "A looming, earthly structure with such natural treachery that to ascend unprepared is to likely void oneself of life.",
                     "Item": "Deepcuts Dagger",
                     "Exits": {"f": "Castle", "b": "Village"}},
        'Castle': {"Name": "Castle Larkin",
                   "Description": "A grand castle belonging to the Larkin family ever since their Lordship began over these lands hundreds of years ago.",
                   "Item": "",
                   "Exits": {"b": "Mountain"}},
    }

    this_area = pathia["Homestead"]
    player_inventory = []
    game_over = False

