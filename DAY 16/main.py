# QUESTION 01
try:
    file = open('data.txt', 'r')
    print("File 'data.txt' opened successfully.")
    file.close()
except FileNotFoundError:
    print("Error: The file 'data.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# QUESTION 02
file = open('data.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()

# QUESTION 03
file = open('output.txt', 'w')
file.write("Hello, World!")
file.close()

# QUESTION 04
try:
    file = open('data.txt', 'r')
except FileNotFoundError:
    print("Error: The file 'data.txt' does not exist.")

# QUESTION 05
file = open('data.txt', 'r')
lines = file.readlines()
print(f"Number of lines: {len(lines)}")
file.close()

# QUESTION 06
file = open('log.txt', 'r')
lines = file.readlines()
for line in lines:
    if 'error' in line:
        print(line.strip())
file.close()

# QUESTION 07
source_file = open('data.txt', 'r')
destination_file = open('data_copy.txt', 'w')
contents = source_file.read()
destination_file.write(contents)
source_file.close()
destination_file.close()

# QUESTION 08
file = open('output.txt', 'a')
file.write("\nEnd of file")
file.close()

# QUESTION 09
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# QUESTION 10
import os
file_size = os.path.getsize('data.txt')
print(f"Size of data.txt: {file_size} bytes")
