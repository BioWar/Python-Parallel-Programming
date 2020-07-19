from threading import Thread
from queue import Queue
from logging import basicConfig, info, INFO
from time import sleep
from random import randint

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
basicConfig(level=INFO, format=LOG_FORMAT)

class Producer(Thread):
	def __init__(self, queue, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.queue = queue

	def run(self):
		for i in range(5):
			item = randint(0, 256)
			self.queue.put(item)
			info(f"Producer notify: item #{item} appended to queue by {self.name}")
			sleep(1)

class Consumer(Thread):
	def __init__(self, queue, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.queue = queue

	def run(self):
		while True:
			item = self.queue.get()
			info(f"Consumer notify: {item} popped from queue by {self.name}")
			self.queue.task_done()

if __name__=="__main__":
	queue = Queue()

	t1 = Producer(queue, name="Producer-1")
	t2 = Consumer(queue, name="Consumer-1")
	t3 = Consumer(queue, name="Consumer-2")
	t4 = Consumer(queue, name="Consumer-3")

	t1.start()
	t2.start()
	t3.start()
	t4.start()

	t1.join()
	t2.join()
	t3.join()
	t4.join()