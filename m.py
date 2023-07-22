import threading
import time
import signal
count = 0
def counter_thread():
    global count
    try:
        while True:
            #print(count)
            count += 1
    except KeyboardInterrupt:
        print("Keyboard Manual Interrupt. Ege is Gay")  
    


       
def main_thread():
    global count
    # Create a threading.Event object.
    try:
        while True:
            print(count)
            time.sleep(10)
    except KeyboardInterrupt:
        print("Keyboard Manual Interrupt. Ege is Gay")  
    

def handler():
    try:
        update=threading.Thread(target=counter_thread)
        printer = threading.Thread(target=main_thread)
        update.daemon = True
        printer.daemon = True 
    #stop_event = threading.Event()

    # Create a thread that executes the counter_thread function.
    
    # Start the thread.
        update.start()
        printer.start()
        update.join()
        printer.join()
    except KeyboardInterrupt:
        print("Keyboard Manual Interrupt. Ege is Gay")  
    

    # Wait for the user to press Ctrl+C.
    while True:
        pass
if __name__ == "__main__":
    # Run the main thread.
    handler()







##########################3
try:
    counter = 0
    while True:
        print("Counter:", counter)
        counter += 1
except KeyboardInterrupt:
    print("\nLoop interrupted by the user.")
