import struct
file=open("text.dat","w")
for n in range(1000):
    data=struct.pack('i',n)
    file.write(str(data))

file.close()
