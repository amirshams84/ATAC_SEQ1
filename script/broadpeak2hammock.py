#!/usr/bin/env python2

import sys,os

if len(sys.argv)!=2:
	print '<broadpeak file> <track name>'
	sys.exit()

infile=sys.argv[1]

# all values on 9th field are -1, exclude them

id=1
fout=open(infile+'.tmp','w')
with open(infile) as fin:
	for line in fin:
		lst=line.rstrip().split('\t')
		fout.write('{0[0]}\t{0[1]}\t{0[2]}\tscorelst:[{0[6]},{0[7]}],id:{1},'.format(lst,id))
		id+=1
		if len(lst[3])>1:
			fout.write('name:"'+lst[3]+'",')
		if lst[5]!='.':
			fout.write('strand:"'+lst[5]+'",')
		fout.write('\n')
fout.close()

os.system('sort -k1,1 -k2,2n '+infile+'.tmp'+' > '+infile+'.srt')
os.system('mv '+infile+'.srt'+' '+infile)
os.system('bgzip -c '+infile+' > '+infile+'.gz')
os.system('tabix -f -p bed '+infile+'.gz')
