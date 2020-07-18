from threading import Thread, Semaphore
from time import sleep
from random import randint
from logging import basicConfig, info, INFO

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
basicConfig(level=INFO, format=LOG_FORMAT)

semaphore = Semaphore(0)
item = 0

def consumer():
	info('Consumer is waiting')
	info(f'Semaphore (before acquire) value={semaphore._value}')
	semaphore.acquire()
	info(f'Semaphore (after  acquire) value={semaphore._value}')
	info(f'Consumer notify: item number {item}')

def producer():
	global item
	sleep(3)
	item = randint(0, 1000)
	info(f'Producer notify: item number {item}')
	info(f'Semaphore (before release) value={semaphore._value}')
	semaphore.release()
	info(f'Semaphore (after  release) value={semaphore._value}')

def main():
	for i in range(4):
		t1 = Thread(target=consumer)
		t2 = Thread(target=producer)
		t1.start()
		t2.start()
		t1.join()
		t2.join()

if __name__ == "__main__":
	main()