import time,sys

indent = 0 #How many spaces to indent
indentIncreasing = True #weater the indentation is increasing or not

try:
    while True: #the main program loop
        print(' ' * indent,end = '') #' '+ next print
        print('********')
        time.sleep(0.1) #for pause for 1/10 of a second
        
        if indentIncreasing:
            #Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                #change direction:
                indentIncreasing = False
    
        else:
            #decrease the number of spaces:
            indent = indent - 1
        
            if indent == 0:
                #change direction:
                indentIncreasing = True
            
except KeyboardInterrupt:
    sys.exit()