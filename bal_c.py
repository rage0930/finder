import time
import random
import bit
from bit import *
from time import sleep

print('',time.ctime())
print('\n ============== ================= ==RANDOM HUNTER== ================= ==============\n\n')

i = 1000000

keys=0
while True:
    t = int(time.time())
    while keys<=i:
        a1 = random.randrange(0x100000000000000000,0x1fffffffffffffffff)
        ## "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
        
        #a1 = random.randrange(0x8000000000000000,0xffffffffffffffff)
        ## "16jY7qLJnxb7CHZyqBP8qca9d51gAjyXQN"
        
        keys+=1
        key = Key.from_int(a1)
        y1 = key.address
        #print('y1=',y1,' hex=',hex(a1))
        #print('a1=',a1)
        #filetest=open("16j.Target.test.txt","a")
        #filetest.write('\n '+str(hex(a1))+' | a1='+ str(a1) + ' | addr=' + str(y1) + '\n')
        #filetest.close()
        if y1.startswith('19vki'):
            print('' + hex(a1) + ' | ' + y1 + ' \n')
            file=open("16j.Target.Info.partial.txt","a")
            file.write('\n '+str(hex(a1))+' | a1='+ str(a1) + ' | addr=' + str(y1) + '\n')
            file.close()
        if y1 == "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG":
            print('Target found!!' + hex(line) + ' | ' + y1 + '\n')
            file=open("16j.Target.Info.txt","a")
            file.write('\n '+str(hex(a1))+' | a1='+ str(a1) + ' | addr=' + str(y1) + '\n')
            file.close()
            wait = input("Press Enter to Exit.")
            sleep(8640000)
            exit()

        if keys == i:
            took = int(time.time() - t)
            pps = int(keys / took)
            print('',i,' keys took',took,'seconds @ ',pps,' pps')
            keys = 0
            t = int(time.time())