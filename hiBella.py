#psuedorandom generator
import os, time

#global vars
password = ""
bigString = ""
redos = 6
result = 999
debug = 0
fredos = 6



#TODO try and catch the file opening
#the mode "a" creates file if it doesn't exist
file = open("rec.txt", "a")

#if file exists, wipe it clean
file.truncate(0)

file.write("GOOGLE SERVER - pretty close tbh "+ '\n')
while (redos >= 0):
    startTime = time.time()
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
    bigString = bigString + builderString

    #TODO need more reliable way to account for network erros tbh
    redos = redos - 1

#server that's farther away to prove that it does KINDA what I think it does 
file.write('\n' + "SERVER THAT's FARTHER AWAY - CALI I THINK " + '\n')
while (fredos >= 0):
    startTime = time.time()
    result = 999
    result = os.system('ping -c 1 ' + '65.49.22.66 ' + "-n " + "1") # -n specifies number of echoes bc it defaults to 4!
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
    bigString = bigString + builderString

    #TODO need more reliable way to account for network erros tbh
    fredos = fredos - 1
file.write('\n' + bigString)
file.close()


