# Imports
import argparse
import logging
import sys
import os
import time

# Argparse configuration
parser = argparse.ArgumentParser(description="A simple program for encrypting and decrypting text files")
parser.add_argument("-v",
                    "--verbose",
                    action="store_true",
                    help="show more detailed information during runtime")
parser.add_argument("-k",
                    "--keep",
                    action="store_true",
                    help="keep original undecrypted files")
parser.add_argument("-f",
                    "--file",
                    type=str,
                    required=True,
                    metavar="",
                    help="the name of the files to be combined, not including the '.part<i>' extension")
parser.add_argument("-n",
                    "--number",
                    type=int,
                    default=2,
                    metavar="",
                    help="The number of files to combine (default 2)")
args = parser.parse_args()
file_name = args.file
n = args.number

# Logging configuration
if args.verbose:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
else:
    logging.basicConfig(level=logging.WARNING, format="%(message)s")

# Possible characters comprising text
alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$%^&*()+-=,.:;/\\|<> "

# Ensuring that n >= 2
logging.info("Ensuring that number of files (-n, --number) is at least 2")
if n < 2:
    logging.error("Error: The number of files (-n, --number) should be at least 2. Exiting.")
    sys.exit(2)

# Prepare file readers
file_list_str = ""
for i in range(n):
    file_list_str += "'" + file_name + ".part" + str(i) + "', "
file_list_str = file_list_str[:len(file_list_str) - 2] + "."
logging.info("Accessing the following files: " + file_list_str)
readers = []
for i in range(n):
    reader = open(file_name + ".part" + str(i), "r")
    readers.append(reader)

# Prepare output file
logging.info("Creating output file '" + file_name + "'.")
writer = open(file_name, "w")
writer.write("")
appender = open(file_name, "a")

# Read through lines in input readers and append decrypted lines to output files
logging.info("Reading encrypted files and writing decrypted contents to '" + file_name + "'...")
start_time = time.time()
reader0 = readers[0]
line0 = reader0.readline()
while not line0 == "":
    for i in range(1, len(readers)):
        reader = readers[i]
        line = reader.readline()
        new_line0 = ""
        for j in range(len(line0)):
            if line0[j] in alph:
                char_index = alph.find(line0[j]) + alph.find(line[j])
                if char_index >= len(alph):
                    char_index -= len(alph)
                new_line0 += alph[char_index]
            else:
                new_line0 += line0[j]
        line0 = new_line0
    appender.write(line0)
    line0 = reader0.readline()
end_time = time.time()
logging.info("Done with decryption (took " + str(end_time - start_time) + " seconds).")

# Delete original undecrypted files
if not args.keep:
    for i in range(n):
        os.remove(file_name + ".part" + str(i))
    logging.info("Removed the following original encrypted files: " + file_list_str)
logging.info("Program complete.")
