import time
import random
items = []
option = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                        "gorgon"])


def print_pause(message):
    print(message)
    time.sleep(0.5)


def welcome():
    print_pause("You find yourself standing in an open field, filled\n"
                "with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + option + " is somewhere around\n"
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very\n"
                "effective) dagger.")


def cave():
    print_pause("You peer cautiously into the cave.")
    if "Sword" in items:
        print_pause("You've been here before, anf gotten all the good stuff."
                    "It's just an empty cave now")
        print_pause("You walk back out to the field.")
        enter()
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eyes catches a glint of metal behind a rock.")
        print_pause("You have found them magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword\n"
                    "with you.")
        items.append("Sword")
        print_pause("You walk back out to the field.")
        enter()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " +
                option + ".")
    print_pause("Eep! This is the "+option+"'s house!")
    print_pause("The "+option+" attacks you!")
    if "Sword" not in items:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    while True:
        housechoice = input("Would you like to (1) fight or (2) run away? ")
        if housechoice == "1":
            if "Sword" in items:
                print_pause("As the " + option + " moves to attack, "
                            "you unsheath your new sword.")
                print_pause("The Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("But the " + option + " takes one look at "
                            "your shiny new toy and runs away!")
                print_pause("You have rid the town of the " + option + ".")
                print_pause("You are victorious!")
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the " +
                            option + ".")
                print_pause("You have been defeated!")
            play_again()
            break
        elif housechoice == "2":
            print_pause("You run back into the field.")
            print_pause("Luckily, you don't semms to have been followed.")
            enter()
            break


def enter():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice = input("(Please enter 1 or 2.)")
        if choice == "1":
            house()
            break
        elif choice == "2":
            cave()
            break


def play_again():
    replay = input("Would you like to play again? (y/n)").lower()
    while True:
        if replay == "y":
            print_pause("Excellent! Restarting the game!")
            play_game()
        elif replay == "n":
            print_pause("Thanks for playing! See you next time.")
            exit()
        else:
            play_again()


def play_game():
    global items
    items = []
    welcome()
    enter()


play_game()
