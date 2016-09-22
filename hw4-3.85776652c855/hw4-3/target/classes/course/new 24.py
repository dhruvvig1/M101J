
def split_fileA(line):
    # split the input line in word and count on the comma
     str=line.split(',')
	 word=str[0]
    # turn the count to an integer  
	 tmp=str[1]
     count=int(tmp)
     return (word, count)


return line.split()