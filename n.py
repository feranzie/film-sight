from threading import Thread

def func1():
    while True:
        print ('Function 1')

def main():
    t = Thread(target = func1)

    t.start()

    for i in xrange(100000):
        print ('Main')

    t.stop()

    print ('End')

if __name__ == '__main__':
    main()