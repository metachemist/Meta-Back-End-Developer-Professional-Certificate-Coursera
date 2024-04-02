import random 
f = open("petname.txt", "r") 
f_content = f.read()
f_content_list = f_content.split("\n")
print(f_content_list)
f.close()
print(random.choice(f_content_list))

#Finally, If I had multiple files in my folder, I could allow myself to pick a file from which to read in a list of names.

#Here's how that would work:

import random
f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))