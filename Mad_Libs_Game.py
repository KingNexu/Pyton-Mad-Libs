#menu
def menu():
    print("Mad libs game:(CREATED BY KingNexu)\n 1:Game1\n 2:Game2")
    option = input("Enter the Menu number: ")

    if option == 1:
        print("Entered Game1")
        #word variables
        adjektive = "Type in a ADJEKTIVE: "
        noun = "Type in a NOUN: "
        plural_noun = "Type in a PLURAL NOUN: "
        bodypart = "Type in a PART OF THE BODY: "
        celebrity = "Type in a CELEBRITY: "

        #variables in text
        adjektive1 = raw_input(adjektive)
        noun1 = raw_input("Type in a NOUN: ")
        plural_noun1 = raw_input("Type in a PLURAL NOUN: ")
        femal_person_room = raw_input("Type the NAME of a FEMAL person that is in the room: ")
        adjektive2 = raw_input(adjektive)
        article_of_clothing = raw_input("Type in a CLOTHING someone in the room is wearing: ")
        noun2 = raw_input(noun)
        city = raw_input("Type in a City: ")
        plural_noun2 = raw_input(plural_noun)
        adjektive3 = raw_input(adjektive)
        bodypart1 = raw_input(bodypart)
        letter = raw_input("Type in a LETTER: ")
        celebrity1 = raw_input(celebrity)
        plural_noun3 = raw_input(plural_noun)
        adjektive4 = raw_input(adjektive)
        place = raw_input("Type in a PLACE: ")
        bodypart2 = raw_input(bodypart)
        adjektive5 = raw_input(adjektive)
        adjektive6 = raw_input(adjektive)
        verb = raw_input("Type in a VERB: ")
        plural_noun4 =raw_input(plural_noun)
        num = raw_input("Type in a NUMBER: ")

        #text
        print("_____________________________________________")
        print("There are many " + adjektive1 + " ways to choose a/an " +noun1+ " to\nread. First, you could ask for recommendtaions from your freinds and")
        print(plural_noun1 + ". Just don't ask Aunt " + femal_person_room + " she only\nreads " +adjektive2+ " books with " +article_of_clothing+ "-ripping goddesses")
        print("on the cover. If your friends and family are no help, try checking out the " +noun2+ " Review in The " +city+ " Times. If she " +plural_noun2)
        print("featured there are too " +adjektive3+ " for your taste, try something a little")
        print("more low-" +bodypart1+ ", like " +letter.upper()+ ": The " +celebrity1+ " Magazine,")
        print("or" +plural_noun3+" Magazine. You cold also choose a book the")
        print(adjektive4+"-fashioned way. Head to your local libary or "+place+"and browse the shelves until somthing cathces your " +bodypart2+ ".")
        print("Or, you could save yourself a whole lot of "+adjektive5+" trouble and log on")
        print("to www.bookish.com, the " +adjektive6+ " new website to " +verb+ " for")
        print("books! With all the time you'll save not having to search for "+plural_noun4+",")
        print("you can read "+num+" more books!")
        print("_____________________________________________")
        print("made by KingNexu")
        print("_____________________________________________")

    if option == 2:
        print("Entered Game2")
        #GAME2

        #variables
        color = raw_input("Type in a COLOR: ")
        plural_noun5 = raw_input("Type in a PLURAL NOUN: ")
        celebrity2 = raw_input("Type in a CELEBRITY: ")
        again = ("Do you wan't to play again? [yes/no]: ")


        #text
        print("_____________________________________________")
        print("Roses are "+color)
        print(plural_noun5+ " are blue")
        print("I love " + celebrity2)
        print("_____________________________________________")
        print("made by KingNexu")
        print("_____________________________________________")





menu()
