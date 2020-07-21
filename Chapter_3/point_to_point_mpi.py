from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print(f"[INFO] My rank is: {rank}.")

if rank == 0:
	data = 10000000
	destination_process = 4
	comm.send(data, destination_process)
	print(f"[INFO] Sending data {data} to process {destination_process} from process {rank}.")
if rank == 1:
	destination_process = 8
	data = "Hello."
	comm.send(data, destination_process)
	print(f"[INFO] Sending data {data} to process {destination_process} from process {rank}.")
if rank == 4:
	data = comm.recv(source=0)
	print(f"[INFO] Data received in rank = {rank} from process source = 0, data = {data}.")
if rank == 8:
	data1 = comm.recv(source=1)
	print(f"[INFO] Data received in rank = {rank} from process source = 1, data = {data1}.")