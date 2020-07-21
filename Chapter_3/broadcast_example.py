from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
	var = 100
else:
	var = None

print(f"[INFO] Process = {rank}, initial var = {var}.")
var = comm.bcast(var, root=0)
print(f"[INFO] Process = {rank}, updated var = {var}.")