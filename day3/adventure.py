hook = "You are walking through the woods with the queen's precious cargo. " \
"You hear a loud thump in the trail in front of you. " \
"What do you do? A. Run and hide B. Turn around couragously C. Run towards the noise." 

decision_a = "You hid beihind a tree and fall into a hole. You land on Tatoonine. What do you do?" \
"D. Get on a pod racer. E. Call for help. F. Cry. "

decision_b = "You face a giant rat. It is hungry. What do you do?"\
"G. Fight it. H. Run and hide. I. Befriend the rat. "

decision_c = "You find a kind old man who tripped. He offers you a wish. What do you do? " \
"J. Run and hide K. Ask about the conditions of the wish L. You wish for BYU Chocolate milk. "

decision_d = "You are challanged to a race. What do you do? M. Win the race. N. Lose the race. "

decision_e = "Sand people come to eat you. What do you do? O. Fight P. Run and hide"

decision_f = "You keep crying. What do you do? Q. Cry more R. Stop crying"

decsion_g = "You die from the rat. You win. "

decision_h = decision_a

decision_i = "The rat is now your bestie. You win. "

decision_j = decision_a

decision_k = "The old man gets angry. You die. "

decision_l = "You receive a nice glass of BYU chocolate milk. You win."

decision_m = "You win."

decision_n = "You die."

decision_o = decision_n

decision_p = decision_a

decision_q = decision_n

decision_r = decision_m



decision = input(hook) #collect the decision from user
decision = decision.upper()
decision_2 = ""
if decision == "A":
    decision2 = input(decision_a)
elif decision == "B": 
    decision2 = input(decision_b)
elif decision == "C":
    decision2 = input(decision_c)
else:
    print("You are dead.")
    # write what happens when you choose...

decision2 = decision_2.upper

if decision == "A" or decision == "B" or decision == "C":
    decision2 = decision_2.upper()

    if decision2 == "D":
        decision3 = input(decision_d)
    elif decision2 == "E":
        decision3 = input(decision_e)
    elif decision2 == "F":
        decision3 = input(decision_f)
    elif decision2 == "G":
        decision3 = input(decision_g)
    elif decision2 == "H":
        decision3 = input(decision_h)
    elif decision2 == "I":
        decision3 = input(decision_i)
    elif decision2 == "J":
        decision3 = input(decision_j)
    elif decision2 == "K":
        decision3 = input(decision_k)
    elif decision2 == "L":
        decision3 = input(decision_L)
    else:
        print("You die.")