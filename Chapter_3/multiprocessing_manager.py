import multiprocessing

def worker(dictionary, key, item):
	process_name = multiprocessing.current_process().name
	print(f"[INFO] {process_name} >>> {key} : {item}.")
	dictionary[key] = item

if __name__=="__main__":
	mgr = multiprocessing.Manager()
	dictionary = mgr.dict()
	jobs = [multiprocessing.Process(target=worker, args=(dictionary, i , i*2)) for i in range(10)]
	for j in jobs:
		j.start()
	for j in jobs:
		j.join()
	print('Results: ', dictionary)