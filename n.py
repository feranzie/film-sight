from threading import Thread
import time

try:
    uInput = ""

    counter = 3

    thread_running = True


    def passwordInputting():
        global counter
        start_time = time.time()
        while time.time() - start_time <= 10:
            uInput = input()
            if uInput != "password":
                print("Incorrect Password.", counter, "tries remaining.")
                counter -= 1
                                    
            else:
                # code for if password is correct
                break

    def passwordTimer():

        global thread_running
        global counter

        start_time = time.time()
        last_time = time.time()

        # run this while there is no input or user is inputting
        while thread_running:
            time.sleep(0.1)
            if time.time() > last_time + 1:
                print("Counter:", int(time.time() - start_time))
                last_time = time.time()
            if time.time() - start_time >= 10:
                if uInput == "password":
                    continue
                else:
                    if counter > 0:
                        print("Incorrect Password.", counter, "tries remaining.")
                        counter -= 1
                        start_time = time.time()
                        
                    else:
                        # code for when no more tries left
                        break
                    
    timerThread = Thread(target=passwordTimer)
    inputThread = Thread(target=passwordInputting)

    timerThread.daemon = True
    inputThread.daemon = True 

    timerThread.start()
    inputThread.start()

    inputThread.join() # interpreter will wait until your process get complete
except:
    print("Keyboard Manual Interrupt. Ege is Gay")
thread_running = False

print("Program Finished")
exit()