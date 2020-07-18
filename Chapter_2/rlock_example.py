from threading import RLock, Thread 
from time import sleep
from random import randint

class Box:
	def __init__(self):
		self.lock = RLock()
		self.total_items = 0

	def execute(self, value):
		with self.lock:
			self.total_items += value

	def add(self):
		with self.lock:
			self.execute(1)

	def remove(self):
		with self.lock:
			self.execute(-1)

def adder(box, items):
	print(f"[INFO] №{items} items to ADD.")
	while items:
		box.add()
		sleep(0.2)
		items -= 1
		print(f"[INFO] ADDED one item -->{items} item to ADD.")

def remover(box, items):
	print(f"[INFO] №{items} items to REMOVE.")
	while items:
		box.remove()
		sleep(0.2)
		items -= 1
		print(f"[INFO] REMOVED one item -->{items} item to REMOVE.")

def main():
	items = 10
	box = Box()

	t1 = Thread(target=adder,
		        args=(box, randint(10,20)))
	t2 = Thread(target=remover,
		        args=(box, randint(1, 10)))
	t1.start()
	t2.start()
	t1.join()
	t2.join()

if __name__ == "__main__":
	main()