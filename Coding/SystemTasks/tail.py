#python equivalent to the tail command in Linux
#Aim: The script should be able to tail a file, should handle large amounts of data.

def tail(f,window):
    """ Returns the last window lines of a file f as a list"""
    if window==0:
        return []
    bufsize = 8124
    f.seek(0,2) #go to the end of the file, 0-beginning, 1=current position, 2=end
    remaining_bytes = f.tell() #file size
    size = window+1
    block = -1
    data = [] #list to store the n lines

    while size>0 and remaining_bytes>0:
        if remaining_bytes - bufsize > 0:
            #seek back one whole buff size
            f.seek(block*bufsize,2)
            #read buffer
            bunch = f.read(bufsize)
        else:
            #file is too small, start from the beginning
            f.seek(0,0)
            #only read what was not read
            bunch = f.read(remaining_bytes)
        bunch=bunch.decode('utf-8')
        data.insert(0,bunch)
        size -= bunch.count('\n')
        remaining_bytes-=bufsize
        block -= 1

    return ''.join(data).splitlines()[-window:]

with open("/Users/bala/pythonProject/Code/RoadToSRE/Coding/SystemTasks/paradiselost.txt", "rb") as file:
    #file object is used as iterator, entire file is not loaded into memory
    print(tail(file,5))