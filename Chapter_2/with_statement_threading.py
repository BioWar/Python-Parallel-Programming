from threading import Thread, Lock, RLock, Condition, Semaphore
from logging import basicConfig, info, INFO

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
basicConfig(level=INFO, format=LOG_FORMAT)

def threading_with(statement):
	with statement:
		info(f"{statement} acquired via with")

def threading_not_with(statement):
	statement.acquire()
	try:
		info(f"{statement} acquired directly")
	finally:
		statement.release()

if __name__=="__main__":
	lock = Lock()
	rlock = RLock()
	condition = Condition()
	mutex = Semaphore(1)
	threading_syncrhonization_list = [lock, rlock, condition, mutex]

	for statement in threading_syncrhonization_list:
		t1 = Thread(target=threading_with, args=(statement,))
		t2 = Thread(target=threading_not_with, args=(statement,))
		t1.start()
		t2.start()
		t1.join()
		t2.join()