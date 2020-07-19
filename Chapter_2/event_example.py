from logging import basicConfig, info, INFO
from threading import Thread, Event
from time import sleep
from random import randint

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
basicConfig(level=INFO, format=LOG_FORMAT)
items = []
event = Event()

class Consumer(Thread):
	def __init__(self, items, event, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.items = items
		self.event = event

	def run(self):
		for i in range(5):
			sleep(2)
			self.event.wait()
			item = self.items.pop()
			info(f'Consumer notify: {item} popped by {self.name}')

class Producer(Thread):
	def __init__(self, items, event, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.items = items
		self.event = event

	def run(self):
		global item
		for i in range(5):
			sleep(3)
			item = randint(0, 100)
			self.items.append(item)
			info(f'Producer notify: item {item} appended by {self.name}')
			self.event.set()
			self.event.clear()

if __name__ == "__main__":
	t1 = Producer(items, event, name="Producer")
	t2 = Consumer(items, event, name="Consumer")

	t1.start()
	t2.start()

	t1.join()
	t2.join()