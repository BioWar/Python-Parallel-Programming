from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
	ls = list(range(1, 11))
else:
	ls = None

buf = comm.scatter(ls, root=0)
print(f"[INFO] Process = {rank}, ls = {buf}.")