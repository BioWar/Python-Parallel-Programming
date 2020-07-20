import multiprocessing
import time

def foo():
	print("[INFO] Starting function foo.")
	for i in range(10):
		print(f"---> {i}")
		time.sleep(1)
	print("[INFO] Finished function foo.")

if __name__=="__main__":
	p = multiprocessing.Process(target=foo)
	print(f"[INFO] Process before execution: {p}, {p.is_alive()}")
	p.start()
	print(f"[INFO] Process running: {p}, {p.is_alive()}")
	p.terminate()
	print(f"[INFO] Process terminated: {p}, {p.is_alive()}")
	p.join()
	print(f"[INFO] Process joined: {p}, {p.is_alive()}")
	print(f"[INFO] Process exit code: {p.exitcode}")