from os import listdir
from os.path import isfile, join
L = listdir("RawData")
for x in L:
    f = open(f"RawData/{x}",'r')
    s = f.read()
    f.close()
    s = s.split("\n")
    s = s[14:]
    s = [",".join(z.split("\t")) for z in s]
    s = ["wave-length (nm),A"]+s
    s = "\n".join(s)
    y = x[3:].split("_Absorbance")[0] + ".csv"
    f = open(f"Data/{y}",'w')
    f.write(s)
    f.close()
    print(y,"done")
print("Done")