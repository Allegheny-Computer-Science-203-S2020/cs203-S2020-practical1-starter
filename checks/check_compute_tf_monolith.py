"""Checks that the compute_tf_monolith.py produces the expected output."""

import shlex
import subprocess
import sys

if __name__ == "__main__":
    # assume that all of the checks run correctly and prove otherwise
    exit_code = 0
    # TODO: define the command that will call the check_compute_tf_monolith.py
    command = ""
    # tokenize this command so that subprocess can accept each of its parts
    tokenized_command = shlex.split(command)
    print("Tokenized command to execute: " + str(tokenized_command))
    print()
    # run the tokenized command and display the output as a byte string
    result = subprocess.run(tokenized_command, stdout=subprocess.PIPE, check=True)
    # TODO: display the standard output variable inside of the result from the subprocess
    # decode the byte string using UTF-8
    decoded_stdout = str(result.stdout.decode("utf-8"))
    print("Decoded output of executed command: \n" + decoded_stdout)
    # check to see if the output contains the first line
    print("Checking each line of the output ...")
    # TODO: This following line of code has a bug in it
    # NOTE: Think carefully about what the checker is intended to do
    # and then fix the bug so that this first check works correctly!
    if "live  -  2" in decoded_stdout:
        print(" - 'live  -  2' is not detected")
        exit_code = 1
    # TODO: All all of the required checks for the output's correctness
    # display the final message to indicate checking is finished
    # NOTE: Follow the previous example for a way to use conditional logic
    print("...Finished checking each line of the output!")
    # at least one of the checks failed
    if exit_code == 1:
        print()
        # TODO: Add a debugging output to indicate that the program did not check correctly
        # NOTE: Please refer to the README.md file for more details about expected output
        # indicate that the program should return a non-zero exit code to indicate failure
        sys.exit(exit_code)
    # none of the checks failed
    # TODO: Add a debugging output to indicate that the program did check correctly
    # NOTE: Please refer to the README.md file for more details about expected output
