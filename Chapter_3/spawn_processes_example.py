import multiprocessing
from target_function import function


if __name__=="__main__":
	process_jobs = []
	for i in range(5):
		p = multiprocessing.Process(target=function, args=(i,))
		process_jobs.append(p)
		p.start()
		p.join()
	for p in process_jobs:
		print(p)