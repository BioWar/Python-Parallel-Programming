from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank + 1)**2

data = comm.gather(data, root=0)
if rank == 0:
	print("Data = ", data)
	print(f"[INFO] Rank = {rank}, received data.")
	for i in range(1, size):
		value = data[i]
		print(f"[INFO] Process {rank} received {value} from process {i}.")