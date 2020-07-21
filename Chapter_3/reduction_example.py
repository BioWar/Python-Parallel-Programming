from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

array_size = 10
recv_data = np.zeros(array_size, dtype=np.int32)
send_data = (rank + 1)*np.ones(array_size, dtype=np.int32)

print(f"[INFO] Process {rank} sending {send_data}.")

comm.Reduce(send_data, recv_data, root=0, op=MPI.SUM)
print(f"[INFO] On task {rank} after Reduce: data = {recv_data}.")