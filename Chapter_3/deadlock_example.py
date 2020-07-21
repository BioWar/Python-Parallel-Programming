from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print(f"[INFO] My rank is: {rank}.")

if rank == 1:
	data_send = 'a'
	destination_process = 5
	source_process = 5
	data_received = comm.recv(source=source_process)
	comm.send(data_send, dest=destination_process)

	print(f"[INFO] Sending data {data_send} to process {destination_process}.")
	print(f"[INFO] Data received is = {data_received}.")

if rank == 5:
	data_send = 'b'
	destination_process = 1
	source_process = 1
	data_received = comm.recv(source=source_process)
	comm.send(data_send, dest=destination_process)

	print(f"[INFO] Sending data {data_send} to process {destination_process}.")
	print(f"[INFO] Data received is = {data_received}.")