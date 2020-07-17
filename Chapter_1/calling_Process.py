import os
import sys

program = "python"
print("Process calling...")
arguments = ["called_Process.py"]

# In this example os.execvp function starts a new process,
# replacing the current one. Note that "End of calling_Process.py"
# is never printed.
os.execvp(program, (program,) + tuple(arguments))
print("End of calling_Process.py.")
