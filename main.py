import threading
import os
import time
import random
import sys


class Main:
    """# Main class
    - Primary Handler
    
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.threads = []

        

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Thread", self.name, "is running")

# Create instances of the MyThread class
thread1 = MyThread("Thread 1")
thread2 = MyThread("Thread 2")

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print("Main thread finished")
