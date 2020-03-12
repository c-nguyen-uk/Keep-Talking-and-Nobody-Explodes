# -*- coding: utf-8 -*-
"""
This programme solves the Morse Code module.

It is important that we allow for input forgiveness since the defuser
is likely to misread the morse code. Hence we only reqiure that the
initial part of the morse code needs to be fully correct. The programme
will then suggest possible correct frequencies. If enough lives are
available, then all of them can be attempted. Otherwise, more correct
morse code will need to be appended.
"""

# Creating dictionaries of all possible morse code, words and
# frequencies which could appear.

morse_to_words = {".........-...-..": "shell", ".....-.-...-.....": "halls",
                "....-....-.-.-.-": "slick", "-.-...-.-.-.-": "trick",
                "-...----..-....": "boxes", ".-....--.-...": "leaks",
                "...-.-.----....": "strobe", "-........-.-.---": "bistro",
                "..-..-....-.-.-.-": "flick","-...------......": "bombs",
                "-....-...--.-": "break", "-....-...-.-.-.-": "brick",
                "...-..--.-": "steak", "...-..-.--.": "sting",
                "...-.-.-.----.-.": "vector", "-.....--...": "beats"}
words_to_freqs = {"shell": "3.505", "halls": "3.515", "slick": "3.522",
                 "trick": "3.532", "boxes": "3.535", "leaks": "3.542",
                 "strobe": "3.545", "bistro": "3.552", "flick": "3.555",
                 "bombs": "3.565", "break": "3.572", "brick": "3.575",
                 "steak": "3.582", "sting": "3.592", "vector": "3.595",
                 "beats": "3.600"}

# This function returns possible the frequencies corresponding to the
# morse code.

def morse_code(morse):
    freqs_list = []
    for i in morse_to_words:
        if morse in i:
            word = morse_to_words[i]
            freq = words_to_freqs[word]
            freqs_list.append(freq)
    if freqs_list == []:
       return "The morse code is wrong." 
    return "The frequency could be: {f} MHz.".format(f=", ".join(freqs_list))

# We now ask for morse code.

while True:
    morse = str(input("Dots and dashes without spaces:"))
    input(morse_code(morse) + "\n \nPress Enter to retry.")
