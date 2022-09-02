#psuedorandom generator
import os, time

#global vars
password = ""
redos = 12
result = 999
debug = 0

#function takes in a 3 digit number
def portioner(znum):
    global password, redos
    interval = 1
    for j in range (1,74,1):
        interval = j * 13
        
        if (interval + 1 >= znum):  #the +1 is bc 955 was being left out despite it being ok to use

            #hardcode specifically take out 94 (space) and 95 (underscore)
            if ((j+47) == 94 or (j+47) == 95):
                print("!!!!!!!!!!")
                return "!!!!!!!!!!!"
                
            #48-122 inclusive for most alphanumeric plus typeable special symbols
            #return ascii of j + 47  (1 + 47 = 48)
            password += chr(j+47)
            redos -= 1
            return chr(j+47)
    #if the num happens to be > 962 (OUTSIDE THE MULTIPLE OF THE RANGE WE WANT)
    #then redo the ping by not decrementing the counter
    print("!!!!!!!!!!!!!!!!")
    return "!!!!!!!!!!!!"


#TODO try and catch the file opening
#the mode "a" creates file if it doesn't exist
file = open("rec.txt", "a")

#if file exists, wipe it clean
file.truncate(0)

#TODO:
#try and catch the potential errors for no internet or timeout also don't run the rest if error caught!
while (redos >= 1):

    startTime = time.time()  #start timer
    result = 999
    result = os.system('ping -c 1 ' + '8.8.8.8 ' + "-n " + "1") # -n specifies number of echoes bc it defaults to 4!
    while (result != 0):  #result being 0 means successful ping
        #do dummy stuff
        #TODO this typically doesn't have enough time to execute??? Genuinely I have no idea why
        debug += 1
    #if success, then the result is ---0 then gucci gang
    duration = time.time() - startTime #this executes only after ping is recieved back
    strDur = str(duration * 1000)

    builderString = strDur[len(strDur)-3] + strDur[len(strDur)-2] + strDur[len(strDur)-1]  #dynamically grab last 3 digits
    file.write(str(duration) + '\n')
    file.write(builderString + '\n')
    file.write(portioner(int(builderString))+ '\n')

#print out password to file
file.write(password + '\n')

file.write("Debug: " + str(debug))

file.close()

#.8.8.8.8 is google server