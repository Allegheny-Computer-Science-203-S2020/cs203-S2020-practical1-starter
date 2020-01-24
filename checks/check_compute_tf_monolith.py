"""Checks that the compute_tf_monolith.py produces the expected output."""

import shlex
import subprocess
import sys

if __name__ == "__main__":
    # assume that all of the checks run correctly and prove otherwise
    exit_code = 0
    # define the command that will call the check_compute_tf_monolith.py
    command = "pipenv run python termfrequency/compute_tf_monolith.py inputs/input.txt"
    # tokenize this command so that subprocess can accept each of its parts
    tokenized_command = shlex.split(command)
    print("Tokenized command to execute: " + str(tokenized_command))
    print()
    # run the tokenized command and display the output as a byte string
    result = subprocess.run(tokenized_command, stdout=subprocess.PIPE, check=True)
    print("Output of executed command: " + str(result.stdout))
    print()
    # decode the byte string using UTF-8
    decoded_stdout = str(result.stdout.decode("utf-8"))
    print("Decoded output of executed command: \n" + decoded_stdout)
    # check to see if the output contains the first line
    print("Checking each line of the output ...")
    if "live  -  2" not in decoded_stdout:
        print(" - 'live  -  2' is not detected")
        exit_code = 1
    # check to see if the output contains the first line
    if "mostly  -  2" not in decoded_stdout:
        print(" - 'mostly  -  2' is not detected")
        exit_code = 1
    # display the final message to indicate checking is finished
    print("...Finished checking each line of the output!")

    # at least one of the checks failed
    if exit_code == 1:
        print()
        print("The termfrequency/compute_tf_monolith.py is not working correctly!")
        # indicate that the program should return a non-zero exit code to indicate failure
        sys.exit(exit_code)
    # none of the checks failed
    print()
    print("The termfrequency/compute_tf_monolith.py is working correctly!")
