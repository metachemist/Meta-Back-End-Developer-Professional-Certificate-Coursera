import random 
f = open("petname.txt", "r") 
f_content = f.read()
f_content_list = f_content.split("\n")
print(f_content_list)
f.close()
print(random.choice(f_content_list))