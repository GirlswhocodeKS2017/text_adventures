#!/usr/bin/python


intro = """\n You awake in a strange room. It is a large, traditionally 
decorated room. You hear a loud scream from what appears 
to be a nearby room.\n"""

print intro

choice = raw_input("Do you 'leave' the room or 'stay'? \n")

if choice == 'stay':
    response ="""\n You decide to stay. Maybe it is all a dream. You close your
    eyes, hoping that you will wake up. A hiddeous monster 
    busts through the door.\n """
    print response
    choice = raw_input("Do you 'stay' in bed (it's all a dream) or do you grab the 'lamp'? \n")
    if choice == 'stay':
        print "\n Sorry. It wasn't a dream. You meet a grisely end."
    elif choice == 'lamp':
        response = """\n You pick up the lamp and swing it at 
        the monster. Direct hit!
        Who new you were such a bad mamba jamba!.\n """
        print response
    else:
        print "\n You didn't choose a viable option. Restart."
        exit(0)
elif choice == 'leave':
    response = """\n You slowly open the door... and come face to face 
    with a huge, scary monster! You are eaten! Better luck next time.\n"""
    print response 
    exit(0)
