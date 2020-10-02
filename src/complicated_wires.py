# -*- coding: utf-8 -*-
"""
This programme solves the Complicated Wires module.

We allow for a lot of input forgiveness to ensure that erroneous
inputs entered under stress do not crash the programme and cause more
time to be wasted. We also do not discriminate between capitalisation
or wire colour ordering.

We also modify the progression of the manual - we first ask for all
possible useful properties of the bomb first, rather than at cutting
point, to save on time, make questioning more efficient, and save
working memory.
"""

# These lists define all possible external properties of the bomb.
lights_state = ["YES", "NO"]
colours = ["WHITE", "RED", "RED WHITE", "WHITE RED", "BLUE", "BLUE WHITE",
           "WHITE BLUE", "RED BLUE", "BLUE RED"]
star_existence = ["YES", "NO"]
max_batteries_possible = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# These inputs create the consistent external properties of the bomb.
batteries = input("How many batteries are there? ")
while not(batteries in max_batteries_possible):
    batteries = input("""That is not a valid number of batteries. 
Please try again: """.replace("\n", ""))
parallel_port = input("Is there a parallel port? ").upper()
while not(parallel_port == "YES" or parallel_port == "NO"):
    parallel_port = input("""You've made a typo - the answer to \"Is there a 
parallel port?\" is yes or no. Please try again: """.replace("\n","")).upper()
is_serial_even = input("Is the serial even? ").upper()
while not(is_serial_even == "YES" or is_serial_even == "NO"):
    is_serial_even = input("""You've made a typo - the answer to \"Is the 
serial even?\" is yes or no. Please try again: """.replace("\n", "")).upper()

# This function contains all possible scenarios for a complicated wire.
def complicated_wires(lights, colour, star,
                      batteries = int(batteries),
                      parallel_port = parallel_port,
                      is_serial_even = is_serial_even):

    # These are all of the light off and no star scenarios.
    if (lights == "NO" and colour == "WHITE" and star == "NO"):
        return "Cut the wire."
    if (lights == "NO" and (colour == "RED"
                            or colour == "RED WHITE"
                            or colour == "WHITE RED"
                            or colour == "BLUE"
                            or colour == "WHITE BLUE"
                            or colour == "BLUE WHITE"
                            or colour == "RED BLUE"
                            or colour == "BLUE RED")
        and star == "NO" and is_serial_even == "YES"):
        return "Cut the wire."

    # These are all of the light off and star scenarios.
    if (lights == "NO" and (colour == "WHITE"
                            or colour == "RED"
                            or colour == "RED WHITE"
                            or colour == "WHITE RED")
        and star == "YES"):
        return "Cut the wire."
    if (lights == "NO" and (colour == "RED BLUE"
                            or colour == "BLUE RED")
        and star == "YES" and parallel_port == "YES"):
        return "Cut the wire."

    # These are all of the light on and no star scenarios.
    if (lights == "YES" and (colour == "RED"
                             or colour == "RED WHITE"
                             or colour == "WHITE RED")
        and star == "NO" and batteries >= 2):
        return "Cut the wire."
    if (lights == "YES" and (colour == "BLUE"
                             or colour == "BLUE WHITE"
                             or colour == "WHITE BLUE")
        and star == "NO" and parallel_port == "YES"):
        return "Cut the wire."
    if (lights == "YES" and (colour == "RED BLUE"
                             or colour == "BLUE RED")
        and star == "NO" and is_serial_even == "YES"):
        return "Cut the wire."

    # These are all of the light on and star scenarios.
    if (lights == "YES" and (colour == "WHITE"
                             or colour == "RED"
                             or colour == "RED WHITE"
                             or colour == "WHITE RED")
        and star == "YES" and batteries >= 2):
        return "Cut the wire."
    if (lights == "YES" and (colour == "BLUE"
                             or colour == "WHITE BLUE"
                             or colour == "BLUE WHITE")
        and star == "YES" and parallel_port == "YES"):
        return "Cut the wire."
    else:
        return "Do not cut the wire."

# This forgiving section asks the user for the properties of the
# complicated wire.
while True:
    lights = input("Is the light on? ").upper()
    while not(lights in lights_state):
        lights = input("""You've made a typo - the answer to \"Is the light
 on?\" is yes or no. Please try again: """.replace("\n", "")).upper()
    colour = input("What colour is the wire? ").upper()
    while not(colour in colours):
        colour = input("""You've made a typo - that colour cannot appear.
 Please try again: """.replace("\n", "")).upper()
    star = input("Is there a star? ").upper()
    while not(star in star_existence):
        star = input("""You've made a typo - the answer to\"Is there a 
star?\" is yes or no. Please try again: """.replace("\n", "")).upper()
    input(complicated_wires(lights, colour, star)
          +"\n \nPress Enter to retry.")
