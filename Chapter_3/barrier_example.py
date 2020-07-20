from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3
finish_line = Barrier(num_runners)
runners = ['First', 'Second', 'Third']

def runner():
	name = runners.pop()
	sleep(randrange(2, 5))
	print(f"[INFO] {name} reached the barrier at: {ctime()}.")
	finish_line.wait()

def main():
	threads = []
	print("[INFO] Starting race.")
	for i in range(num_runners):
		threads.append(Thread(target=runner))
		threads[-1].start()
	for thread in threads:
		thread.join()
	print("[INFO] Ending race.")

if __name__=="__main__":
	main()