#Imports
import argparse
import logging
import secrets
import math
import os
import time

#Argparse configuration
parser = argparse.ArgumentParser(description="A simple program for encrypting and decrypting text files")
parser.add_argument("-v",
                    "--verbose",
                    action="store_true",
                    help="show more detailed information during runtime")
parser.add_argument("-k",
                    "--keep",
                    action="store_true",
                    help="keep original unencrypted file")
parser.add_argument("-f",
                    "--file",
                    type=str,
                    required=True,
                    metavar="",
                    help="the name of the file to be encrypted")
parser.add_argument("-n",
                    "--number",
                    type=int,
                    default=2,
                    metavar="",
                    help="The number of output files (default 2)")
args = parser.parse_args()
file_name = args.file
n = args.number

#Logging configuration
if args.verbose:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
else:
    logging.basicConfig(level=logging.WARNING, format="%(message)s")

#Possible characters comprising text
alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$%^&*()+-=,.:;/\\|<>"

#Test file access
logging.info("Accessing file '" + file_name + "'.")
reader = open(file_name, "r")
line = reader.readline()

#Prepare output files
info_message = "Created the following output files:"
appenders = []
for i in range(n):
    output_file = file_name + ".part" + str(i)
    info_message += " '" + output_file + "',"
    creator = open(output_file, "w")
    creator.write("")
    appender = open(output_file, "a")
    appenders.append(appender)
info_message = info_message[:len(info_message) - 1] + "."
logging.info(info_message)

#Loop through lines in target file and append encrypted lines to output files
logging.info("Reading file '" + file_name + "' and writing encrypted contents to output files...")
start_time = time.time()
while line != "":
    for character in line:
        if character in alph:
            char_index = alph.find(character)
            index_sum = 0
            for i in range(1,n):
                rand_index = math.floor(secrets.SystemRandom().random() * len(alph))
                rand_char = alph[rand_index]
                appender = appenders[i]
                appender.write(rand_char)
                index_sum += rand_index
                if index_sum >= len(alph):
                    index_sum -= len(alph)
            key_index = char_index - index_sum
            if key_index < 0:
                key_index += len(alph)
            key_char = alph[key_index]
            appender = appenders[0]
            appender.write(key_char)
        else:
            for appender in appenders:
                appender.write(character)
    line = reader.readline()
end_time = time.time()
logging.info("Done with encryption (took " + str(end_time - start_time) + " seconds).")

#Delete original unencrypted file
if not args.keep:
    os.remove(file_name)
    logging.info("Removed original unencrypted file '" + file_name + "'.")
logging.info("Program complete.")
