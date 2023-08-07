import random
f = open ("newfile.txt", "r")
f_content = f.read()
#print(f_content)
f_content_split = f_content.split("\n")
print(random.choice(f_content_split))