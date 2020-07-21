from mpi4py import MPI
import numpy as np

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

neighbour_processes = [0, 0, 0, 0]

if __name__=="__main__":
	comm = MPI.COMM_WORLD
	rank = comm.rank
	size = comm.size

	grid_row = int(np.floor(np.sqrt(comm.size)))
	grid_col = comm.size // grid_row
	area = grid_row * grid_col

	if area > size:
		grid_col -= 1
	if area > size:
		grid_row -= 1

	if (rank == 0):
		print(f"[INFO] Building a {grid_row} x {grid_col} grid topology.")

	cartesian_communicator = comm.Create_cart((grid_row, grid_col),
											  periods=(False, False),
											  reorder=True)
	my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)
	neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
	neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)
	print(f"[INFO] Process = {rank}, row = {my_mpi_row}, column = {my_mpi_col}. \n \
		    ---> neighbour_processes[UP] = {neighbour_processes[UP]}; \n \
		    ---> neighbour_processes[DOWN] = {neighbour_processes[DOWN]}; \n \
		    ---> neighbour_processes[LEFT] = {neighbour_processes[LEFT]}; \n \
		    ---> neighbour_processes[RIGHT] = {neighbour_processes[RIGHT]}. \n")