# Write a Python program to write a list to a file.

f=open("python.txt","a")
l=['Hello','world']
f.writelines(l)
f.close()