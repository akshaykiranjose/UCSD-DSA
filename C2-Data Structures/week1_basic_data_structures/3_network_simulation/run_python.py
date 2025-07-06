import subprocess
from termcolor import colored

for i in range(1, 23):
    test_file = f"tests/{i:02}"
    answer_file = f"{test_file}.a"
    output_file = f"{test_file}.out"

    # Run soln.py with input redirection and output capture
    with open(test_file, 'r') as infile, open(output_file, 'w') as outfile:
        subprocess.run(['python', 'process_packages.py'], stdin=infile, stdout=outfile)

    # Read expected and actual output
    with open(output_file, 'r') as out, open(answer_file, 'r') as ans:
        output_lines = out.readlines()
        answer_lines = ans.readlines()

    # Compare outputs line by line
    if output_lines == answer_lines:
        print(colored(f"Test {i:02}: PASS", 'green'))
    else:
        print(colored(f"Test {i:02}: FAIL", 'red'))
        '''
        diff = difflib.unified_diff(
            answer_lines, output_lines,
            fromfile=f'{test_file}.a',
            tofile=f'{test_file}.out',
            lineterm=''
        )
        for line in diff:
            print(line)
        '''
