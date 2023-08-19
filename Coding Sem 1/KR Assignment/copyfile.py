import os, sys


f1 = input ("Enter a source file: ").strip() 
f2 = input("Enter a target file: ").strip()


if os.path.isfile(f2):
    print(f2 + " already exists")
    sys.exit()


file = open (f1, "r")
outfile = open (f2, "w")

for line in file:
    outfile.write(line)
print('Writing is Done!!!')

file.close()
outfile.close()