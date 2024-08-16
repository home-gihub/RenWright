
##--Winston Payne--##
# Gender: Male      #
# Animations: 6     #
#####################

#####--Animations--#####
# 1 - talk             #
# 2 - sweat            #
# 3 - sweat & talk     #
# 4 - damage           #
# 5 - pat head idk     #
# 6 - pat head talk    #
########################

label init_C_payne():
    image payne stand:
        "payne/Frame_0000.gif"
        pause 0.05
        repeat

    image payne talk:
        "payne/Frame_0001.gif"
        pause 0.1
        "payne/Frame_0004.gif"
        pause 0.1
        "payne/Frame_0002.gif"
        pause 0.1
        "payne/Frame_0004.gif"
        pause 0.1
        "payne/Frame_0003.gif"
        pause 0.1
        "payne/Frame_0004.gif"
        pause 0.1
        "payne/Frame_0002.gif"
        pause 0.1
        "payne/Frame_0004.gif"
        pause 0.1
        repeat

    image payne sweat:
        "payne/Frame_0005.gif"
        pause 0.15000000000000002
        "payne/Frame_0006.gif"
        pause 0.15000000000000002
        "payne/Frame_0007.gif"
        pause 0.15000000000000002
        "payne/Frame_0008.gif"
        pause 0.15000000000000002
        repeat

    image payne sweat talk:
        "payne/Frame_0009.gif"
        pause 0.1
        "payne/Frame_0010.gif"
        pause 0.1
        "payne/Frame_0011.gif"
        pause 0.1
        "payne/Frame_0012.gif"
        pause 0.1
        repeat

    image payne damage:
        "payne/Frame_0014.gif"
        pause 0.05
        "payne/Frame_0015.gif"
        pause 0.05
        "payne/Frame_0016.gif"
        pause 1.1500000000000001

    image payne pat:
        "payne/Frame_0018.gif"
        pause 0.75
        "payne/Frame_0017.gif"
        pause 0.25
        "payne/Frame_0018.gif"
        pause 0.45
        "payne/Frame_0017.gif"
        pause 0.25
        "payne/Frame_0018.gif"
        pause 1.25
        repeat

    image payne pat talk:
        "payne/Frame_0019.gif"
        pause 0.1
        "payne/Frame_0020.gif"
        pause 0.1
        "payne/Frame_0021.gif"
        pause 0.1
        "payne/Frame_0020.gif"
        pause 0.1
        "payne/Frame_0019.gif"
        pause 0.1
        "payne/Frame_0023.gif"
        pause 0.1
        "payne/Frame_0022.gif"
        pause 0.1
        "payne/Frame_0020.gif"
        pause 0.15000000000000002
        "payne/Frame_0019.gif"
        pause 0.15000000000000002
        "payne/Frame_0023.gif"
        pause 0.1
        "payne/Frame_0022.gif"
        pause 0.1
        "payne/Frame_0020.gif"
        pause 0.15000000000000002
        repeat


    define wp = Character("Payne")
    $ wp.role = "pro" 

    return