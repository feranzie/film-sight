import threading
import time

count = 0
stop_event = threading.Event()

def counter_thread():
    global count
    try:
        while not stop_event.is_set():
            count += 1
    except KeyboardInterrupt:
        print("Keyboard Manual Interrupt. Ege is Gay")
        stop_event.set()

def main_thread():
    global count
    try:
        while not stop_event.is_set():
            print(count)
            time.sleep(10)
    except KeyboardInterrupt:
        print("Keyboard Manual Interrupt. Ege is Gay")
        stop_event.set()

def handler():
    try:
        update = threading.Thread(target=counter_thread)
        printer = threading.Thread(target=main_thread)

        update.start()
        printer.start()
        
        while not stop_event.is_set():
            pass  # Wait until the threads finish or a KeyboardInterrupt occurs

        update.join()
        printer.join()
    except KeyboardInterrupt:
        print("Keyboard Manual Interrupt. Ege is Gay")
        stop_event.set()

if __name__ == "__main__":
    handler()
