# pip install rpg

import subprocess
import shlex

def run_command2(inp, out, command):
    with open(inp, 'r') as file:
        process = subprocess.Popen(shlex.split(command),
                                   shell=False,
                                   stdout=subprocess.PIPE,
                                    encoding='utf8')
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        rc = process.poll()
        return rc

# inp = "amyloid-beta.fasta"
# out = "rpg-2_test.fasta"

# run_command2(inp, out, "rpg -i {} -o {} -e 2 5".format(inp, out)
