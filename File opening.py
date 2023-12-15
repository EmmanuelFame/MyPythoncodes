f= open('text.txt', 'r')
#print(f.read(1))
for line in f:
    print(line, end='')
print(f.readline(1))
f.close
file_write=open('s.txt', 'w')
file_write.write('this is a test\n')
file_write.write('12345')
file_write.close
