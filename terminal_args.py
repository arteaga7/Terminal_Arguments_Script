'''Example of script ran in terminal with arguments.

To run this script in terminal:
$ python script_args.py myfile.txt --arg2 100
or just:
$ python script_args.py myfile.txt

To show help:
$ python script_args.py -h
or
$ python script_args.py --help
'''

# Import library
import argparse

# Create parser object
parser = argparse.ArgumentParser(description='Description of script.')

# Create no optional argument
parser.add_argument('arg1', type=str, default='untitled.txt',
                    help='No optional Argument1 should be a string')

# Create optional argument
parser.add_argument('--arg2', type=int, default=42,
                    help='Optional Argument2 should be an integer')

# Parse arguments
args = parser.parse_args()
print(f"Argument 1: {args.arg1}")
print(f"Argument 2: {args.arg2}")
