import threading, time

class reqthread(threading.Thread):
    def run(self):
        for i in range(0, 100):
            time.sleep(1)
            print('.')

try:
    thread = reqthread()
    thread.start()
    thread.join()
except (KeyboardInterrupt, SystemExit):
    print('\n! Received keyboard interrupt, quitting threads.\n')