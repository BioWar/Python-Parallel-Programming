import multiprocessing

def function_square(data):
	name = multiprocessing.current_process().name
	if name not in processes_dict.keys():
		processes_dict[name] = 1
	else:
		processes_dict[name] += 1
	result = data * data
	return result

if __name__=="__main__":
	manager = multiprocessing.Manager()
	processes_dict = manager.dict()
	inputs = list(range(0, 100))
	print('Pool inputs: ', inputs)
	pool = multiprocessing.Pool(processes=4)
	pool_outputs = pool.map(function_square, inputs)

	pool.close()
	pool.join()
	print('Pool outputs: ', pool_outputs)
	
	for key, item in processes_dict.items():
		print(f"{key} did function_square {item} times.")