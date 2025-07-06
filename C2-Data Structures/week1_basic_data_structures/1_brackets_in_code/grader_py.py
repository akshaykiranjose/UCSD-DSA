from subprocess import Popen, PIPE
from pathlib import Path

test_dir = Path(r"tests")
total_testcases, success_testcases = 0, 0
for file in test_dir.iterdir():
    if not str(file).endswith('.a'):

        process = Popen(['main.exe', file], 
                        stdout=PIPE, universal_newlines=True)
        (stdout, stderr) = process.communicate()

        true_output = open(f"{file}.a", 'r').readline()
        #print(true_output, type(true_output))
        #break
        total_testcases += 1
        if true_output == stdout:
            success_testcases += 1
        else:
            #print(true_output, type(true_output))
            print(stdout, type(stdout))
            break

print(f"{success_testcases}/{total_testcases} successful")