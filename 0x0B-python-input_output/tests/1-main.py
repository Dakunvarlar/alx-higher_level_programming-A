#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write("my_first_file.txt", "This schoool is so cool!\n")
print(nb_characters)
