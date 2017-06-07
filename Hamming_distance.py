import sys
def fileread():
	seqarray = [sys.argv[1]]#empty list for sequences
	f = openandread() #open file
	seqdata = [] #sequences stored in list form
	line = f.readline()#read each line
	while True:
            if not line:
                break
            if line [0] == '>':       # Check to see if we're onto the next record
                break
            seqdata.append(line.rstrip()) #appends sequences to seqdata
            line = f.readline()
        nts = ''.join(seqdata).replace(" ", "").replace("\r", "")
        seqarray.append(nts) #appends cleared data to seq array
        
      	if not line:
            return fastaid, seqarray

def Hamming_distance():
	s = seqarray[0]
	t = seqarray[1]
	for d in s,t:
		if s[d] == t[d]:
			d+0
		if s[d] != t[d]:
		 	d+1
		print d
