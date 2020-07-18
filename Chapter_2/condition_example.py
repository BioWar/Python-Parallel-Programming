from logging import basicConfig, info, INFO
from threading import Thread, Condition
from time import sleep

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
basicConfig(level=INFO, format=LOG_FORMAT)
items = []
condition = Condition()

class Consumer(Thread):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def consume(self):
		with condition:
			if len(items) == 0:
				info('No items to consume 0/10')
				condition.wait()

			items.pop()
			info(f'Consumed 1 item {len(items)}/10')

			condition.notify()

	def run(self):
		for i in range(20):
			sleep(2)
			self.consume()

class Producer(Thread):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def produce(self):
		with condition:
			if len(items) == 10:
				info(f'Items produced {len(items)}/10. Stopped.')
				condition.wait()

			items.append(1)
			info(f'Total items {len(items)}/10')
			condition.notify()

	def run(self):
		for i in range(20):
			sleep(0.5)
			self.produce()

def main():
	producer = Producer(name='Producer')
	consumer = Consumer(name='Consumer')
	producer.start()
	consumer.start()
	producer.join()
	consumer.join()

if __name__=="__main__":
	main()