# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image bg def:
    "bg/def.png"
image bg pro:
    "bg/pro.png"
image bg wit:
    "bg/wit.png"
image bg judge:
    "bg/judge.png"
image bench def:
    "benches/def.gif"
    zoom 5
image bench pro:
    "benches/pro.gif"
    zoom 5
image bench wit:
    "benches/wit.gif"
    zoom 5

# The game starts here.

label start:

    # we want to use phoenix so we need to run the code that initalixes him
    call init_C_judge()

    call court_say(judge, "Hi, right now there is nothing in script.rpy", "judge talk")

    # This ends the game.

    return
