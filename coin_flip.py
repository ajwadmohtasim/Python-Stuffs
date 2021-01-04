import random
limit = 0
process = 0
total_process = 10000
total_streak = 0
total_toss = 100
#Main Loop
while True:
    #Resetting list to test how many streak in each SETS of FLIP
    coin_flip_list = []
    #FLIP SET
    while True:
        coin_flip_list.append(random.randint(0, 1))  #H or T/ 1 or 0 same thing
        limit += 1
        if limit == total_toss:
            limit = 0
            break
    # Streak Count
    streak = 0
    for i in range(1, len(coin_flip_list)):
        if coin_flip_list[i] == coin_flip_list[i-1]:
            streak += 1 
        else:
            streak = 0
        if streak == 6:
            total_streak += 1
            
    #Loop Break Upon Total TEST PROCESSES
    process += 1
    if process == total_process:
        break
print("Out of ", total_process, " >> Streak: ", total_streak)
print('Chance of streak: %s%%' % (total_streak / 100))