print("THE LEAN CHRONICLES")
#here is the games title 
import time

def delay_print(s):
    for char in s:
        print(char, end='')
        time.sleep(0.04)
#here i placed a delay print as i found it was nicer to read when the text was delayed.
        
delay_print("you wake up, you feel a pain in your leg and you head hurts...like hell. ")
delay_print("you have no memory of last night, the night before that, or any other, ")
delay_print("you barely remember you own name, all you remember is bathing in lean. ")
delay_print("you must seek out the fountain of lean. ")
delay_print("do you head to the nearest tavern a drink away your issue or do you seek a doctor. ")
#here is the introduction for the game.
loop = 1
while loop == 1:
    print("tavern/doctor")
    decision1 = input()
    if decision1 == "tavern":
        loop = 2
#ive used loops here as it worked nicely with the style of game im going for.
#after a bit of trial and error it proved the most trust worthy way of asking questions. if you ask questions and the reply the user types is invalid it loops back to the oringial question rather than breaking the program.

#the rest of this content is gameplay that contains relatively similar code.
        delay_print("you struggle to stand up, you feel a sharp pain in your leg. you start limping along the dirt path. ")
        delay_print("you walk for miles, you finally see a sign *tavern* you walk to towards it and enter. ")
        delay_print("you are greated by the roaring laugh of veteran warriors and the crashing of beer mugs. ")
        delay_print("it seems a great army has stopped here, you head to the counter and you ask for")
        print("local rumors/a drink")
        decision2 = input()
        if decision2 == "local rumors":
            delay_print("hmm, well i did hear of this local physicopath, damn heard he came running into the vilage scream'n bout some ")
            delay_print("dragon then he tripped over broke his leg then passed out in a puddle of his own apple juice. ")
            delay_print("..the milita tried to get anything outta him but he was too out of it, they gave up and dumped him not far from here")
            delay_print("i didnt see the poor fool though, been kept pretty busy here.")
            delay_print("i wouldnt worry about that though")
            if decision2 == "Inquire more":
                print("")
    elif decision1 == "doctor":
        loop = 2
#ive used 2 loops as if i used only 1 part of the gameplay would be unaccessable.
        delay_print("you pull yourself up using every mucle in your body, you realise there are two roads. ")
        delay_print("one seems more worn in, well-used and such the other being in better condition but it seems its hasnt caried ones feet in all to long")
        delay_print("...which will you chose?")
        print("used road/lesser used road")
        decision3 = input()
        if decision3 == "used road":
            delay_print("you start limping down the muddy, print covered path. you walk for miles seeing farms, small houses, and the odd trader.")
            delay_print("you over hear the traders")
                            
        

    else:
        print("invalid answer")
    
