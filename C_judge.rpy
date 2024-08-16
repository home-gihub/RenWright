##----The Judge----##
# Gender: Male      #
# Animations: 9     #
#####################

#####--Animations--#####
# 0 - stand            #
# 1 - talk             #
# 2 - nod              #
# 3 - head shake       #
# 4 - angry            #
# 5 - ditto + talk     #
# 6 - shocked          #
# 7 - ditto + talk     #
# 8 - sleep?           #
########################

label init_C_judge():
    image judge stand:
        "judge/Frame_0000.gif"
        pause 0.4
        "judge/Frame_0001.gif"
        pause 0.05
        "judge/Frame_0002.gif"
        pause 0.05
        "judge/Frame_0001.gif"
        pause 0.05
        "judge/Frame_0000.gif"
        pause 0.75
        "judge/Frame_0001.gif"
        pause 0.05
        "judge/Frame_0002.gif"
        pause 0.05
        "judge/Frame_0001.gif"
        pause 0.05
        "judge/Frame_0000.gif"
        pause 0.05
        "judge/Frame_0001.gif"
        pause 0.05
        "judge/Frame_0002.gif"
        pause 0.05
        "judge/Frame_0001.gif"
        pause 0.05
        "judge/Frame_0000.gif"
        pause 1.25
        repeat
    
    image judge talk:
        "judge/Frame_0003.gif"
        pause 0.15000000000000002
        "judge/Frame_0006.gif"
        pause 0.15000000000000002
        "judge/Frame_0007.gif"
        pause 0.15000000000000002
        "judge/Frame_0006.gif"
        pause 0.15000000000000002
        "judge/Frame_0008.gif"
        pause 0.15000000000000002
        "judge/Frame_0006.gif"
        pause 0.15000000000000002
        "judge/Frame_0007.gif"
        pause 0.15000000000000002
        "judge/Frame_0006.gif"
        pause 0.15000000000000002
        "judge/Frame_0004.gif"
        pause 0.05
        "judge/Frame_0005.gif"
        pause 0.05
        "judge/Frame_0004.gif"
        pause 0.05
        "judge/Frame_0006.gif"
        pause 0.15000000000000002
        "judge/Frame_0007.gif"
        pause 0.15000000000000002
        "judge/Frame_0006.gif"
        pause 0.15000000000000002
        "judge/Frame_0008.gif"
        pause 0.15000000000000002
        "judge/Frame_0006.gif"
        pause 0.15000000000000002
        "judge/Frame_0007.gif"
        pause 0.15000000000000002
        "judge/Frame_0006.gif"
        pause 0.15000000000000002
        repeat
    
    image judge nod:
        "judge/Frame_0009.gif"
        pause 0.05
        "judge/Frame_0010.gif"
        pause 0.05
        "judge/Frame_0011.gif"
        pause 0.1
        "judge/Frame_0012.gif"
        pause 0.1
        "judge/Frame_0011.gif"
        pause 0.1
        "judge/Frame_0013.gif"
        pause 0.25
        "judge/Frame_0011.gif"
        pause 0.1
        "judge/Frame_0010.gif"
        pause 0.1
        "judge/Frame_0009.gif"
        pause 0.05
        repeat
    
    image judge headshake:
        "judge/Frame_0014.gif"
        pause 0.05
        "judge/Frame_0015.gif"
        pause 0.05
        "judge/Frame_0016.gif"
        pause 0.1
        "judge/Frame_0017.gif"
        pause 0.1
        "judge/Frame_0016.gif"
        pause 0.1
        "judge/Frame_0018.gif"
        pause 0.1
        "judge/Frame_0016.gif"
        pause 0.1
        "judge/Frame_0017.gif"
        pause 0.1
        "judge/Frame_0016.gif"
        pause 0.1
        "judge/Frame_0015.gif"
        pause 0.05
        "judge/Frame_0014.gif"
        pause 0.05
        repeat
    
    image judge angry:
        "judge/Frame_0019.gif"
        pause 0.4
        "judge/Frame_0020.gif"
        pause 0.05
        "judge/Frame_0021.gif"
        pause 0.05
        "judge/Frame_0020.gif"
        pause 0.05
        "judge/Frame_0019.gif"
        pause 0.75
        "judge/Frame_0020.gif"
        pause 0.05
        "judge/Frame_0021.gif"
        pause 0.05
        "judge/Frame_0020.gif"
        pause 0.05
        "judge/Frame_0019.gif"
        pause 0.05
        "judge/Frame_0020.gif"
        pause 0.05
        "judge/Frame_0021.gif"
        pause 0.05
        "judge/Frame_0020.gif"
        pause 0.05
        "judge/Frame_0019.gif"
        pause 1.25
        repeat
    
    image judge angry talk:
        "judge/Frame_0022.gif"
        pause 0.15000000000000002
        "judge/Frame_0025.gif"
        pause 0.15000000000000002
        "judge/Frame_0026.gif"
        pause 0.15000000000000002
        "judge/Frame_0025.gif"
        pause 0.15000000000000002
        "judge/Frame_0027.gif"
        pause 0.15000000000000002
        "judge/Frame_0025.gif"
        pause 0.15000000000000002
        "judge/Frame_0026.gif"
        pause 0.15000000000000002
        "judge/Frame_0025.gif"
        pause 0.15000000000000002
        "judge/Frame_0023.gif"
        pause 0.05
        "judge/Frame_0024.gif"
        pause 0.05
        "judge/Frame_0023.gif"
        pause 0.05
        "judge/Frame_0025.gif"
        pause 0.15000000000000002
        "judge/Frame_0026.gif"
        pause 0.15000000000000002
        "judge/Frame_0025.gif"
        pause 0.15000000000000002
        "judge/Frame_0027.gif"
        pause 0.15000000000000002
        "judge/Frame_0025.gif"
        pause 0.15000000000000002
        "judge/Frame_0026.gif"
        pause 0.15000000000000002
        "judge/Frame_0025.gif"
        pause 0.15000000000000002
        repeat
    
    image judge shocked:
        "judge/Frame_0028.gif"
        pause 0.4
        "judge/Frame_0029.gif"
        pause 0.05
        "judge/Frame_0030.gif"
        pause 0.05
        "judge/Frame_0029.gif"
        pause 0.05
        "judge/Frame_0028.gif"
        pause 0.05
        "judge/Frame_0029.gif"
        pause 0.05
        "judge/Frame_0030.gif"
        pause 0.05
        "judge/Frame_0029.gif"
        pause 0.05
        "judge/Frame_0028.gif"
        pause 0.75
        "judge/Frame_0029.gif"
        pause 0.05
        "judge/Frame_0030.gif"
        pause 0.05
        "judge/Frame_0029.gif"
        pause 0.05
        "judge/Frame_0028.gif"
        pause 0.05
        "judge/Frame_0029.gif"
        pause 0.05
        "judge/Frame_0030.gif"
        pause 0.05
        "judge/Frame_0029.gif"
        pause 0.05
        "judge/Frame_0028.gif"
        pause 1.25
        repeat
    
    image judge shocked talk:
        "judge/Frame_0031.gif"
        pause 0.15000000000000002
        "judge/Frame_0034.gif"
        pause 0.15000000000000002
        "judge/Frame_0035.gif"
        pause 0.15000000000000002
        "judge/Frame_0034.gif"
        pause 0.15000000000000002
        "judge/Frame_0036.gif"
        pause 0.15000000000000002
        "judge/Frame_0034.gif"
        pause 0.15000000000000002
        "judge/Frame_0035.gif"
        pause 0.15000000000000002
        "judge/Frame_0034.gif"
        pause 0.15000000000000002
        "judge/Frame_0032.gif"
        pause 0.05
        "judge/Frame_0033.gif"
        pause 0.05
        "judge/Frame_0032.gif"
        pause 0.05
        "judge/Frame_0034.gif"
        pause 0.15000000000000002
        "judge/Frame_0035.gif"
        pause 0.15000000000000002
        "judge/Frame_0034.gif"
        pause 0.15000000000000002
        "judge/Frame_0036.gif"
        pause 0.15000000000000002
        "judge/Frame_0034.gif"
        pause 0.15000000000000002
        "judge/Frame_0035.gif"
        pause 0.15000000000000002
        "judge/Frame_0034.gif"
        pause 0.15000000000000002
        repeat
    
    image judge sleep:
        "judge/Frame_0037.gif"
        pause 0.05
        repeat
    
    define judge = Character("The Judge")

    $ judge.role = "judge" 

    return