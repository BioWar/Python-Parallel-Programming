from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

send_data = (rank + 1) * np.ones(size, dtype=np.int32)
recv_data = np.empty(size, dtype=np.int32)
comm.Alltoall(send_data, recv_data)

print(f"[INFO] Process {rank} sending {send_data} receiving {recv_data}.") 