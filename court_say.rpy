label court_say(character, line, anim):

    if character.role == "def":
        scene bg def
        with None
    elif character.role == "pro":
        scene bg pro
        with None
    elif character.role == "judge":
        scene bg judge
        with None


    $ renpy.show(anim)

    if character.role == "def":
        show bench def
    elif character.role == "pro":
        show bench pro

    character "[line]"
    with None

    $ renpy.hide(anim)

    return