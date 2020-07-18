import threading
import time

def first_function():
	print(f"[INFO] {threading.currentThread().getName()} is starting...")
	time.sleep(2)
	print(f"[INFO] {threading.currentThread().getName()} is exiting...")
	return

def second_function():	
	print(f"[INFO] {threading.currentThread().getName()} is starting...")
	time.sleep(2)
	print(f"[INFO] {threading.currentThread().getName()} is exiting...")
	return

def third_function():	
	print(f"[INFO] {threading.currentThread().getName()} is starting...")
	time.sleep(2)
	print(f"[INFO] {threading.currentThread().getName()} is exiting...")
	return

if __name__ == "__main__":
	t1 = threading.Thread(name='first_function',
						  target=first_function,)
	t2 = threading.Thread(name='second_function',
					      target=second_function,)
	t3 = threading.Thread(name='third_function',
						  target=third_function,)
	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()
