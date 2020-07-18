import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT = 100000
shared_resource_lock = threading.Lock()

### Lock Management ###
def increment_with_lock():
	global shared_resource_with_lock
	for i in range(COUNT):
		shared_resource_lock.acquire()
		shared_resource_with_lock += 1
		shared_resource_lock.release()

def decrement_with_lock():
	global shared_resource_with_lock
	for i in range(COUNT):
		shared_resource_lock.acquire()
		shared_resource_with_lock -= 1
		shared_resource_lock.release()

### No Lock Management ###
def increment_without_lock():
	global shared_resource_with_no_lock
	for i in range(COUNT):
		shared_resource_with_no_lock += 1

def decrement_without_lock():
	global shared_resource_with_no_lock
	for i in range(COUNT):
		shared_resource_with_no_lock -= 1

### Main
if __name__ == "__main__":
	t1 = threading.Thread(target=increment_with_lock)
	t2 = threading.Thread(target=decrement_with_lock)
	t3 = threading.Thread(target=increment_without_lock)
	t4 = threading.Thread(target=decrement_without_lock)
	threads = [t1, t2, t3, t4]
	for t in threads:
		t.start()
	for t in threads:
		t.join()
	print(f"[INFO] Value of shared_resource_with_lock={shared_resource_with_lock}.")
	print(f"[INFO] Value of shared_resource_with_no_lock={shared_resource_with_no_lock}.")