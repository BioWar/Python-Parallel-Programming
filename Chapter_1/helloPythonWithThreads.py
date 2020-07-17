from threading import Thread
from time import sleep


class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Hello Parallel Python CookBook!\n"


    def print_message(self):
        print(self.message)

    def run(self):
        print("[INFO] Thread starting...")

        x = 0
        while (x < 10):
            self.print_message()
            sleep(0.8)
            x += 1
        print("[INFO] Thread ended...")

if __name__ == "__main__":
    print("[INFO] Process started...")
    hello_Python = CookBook()
    hello_Python.start()
    print("[INFO] Process ended.")
