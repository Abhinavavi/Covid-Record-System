from re import T
from tkinter import END


def pos(s):
	a=open(r"C:\Users\nimit\Desktop\File-Structure-Mini-Project-main\COVIDET\positive.txt")
	lines = a.readlines()
	a.close()
	p=-1
	q=0
	for i in lines:
		q=q+1
		p=i.find(s)
		if p!=-1:
			flag=i
			break
	if p!=-1:
		del lines[q-1]
		b=open(r"C:\Users\nimit\Desktop\File-Structure-Mini-Project-main\COVIDET\positive.txt","w+")
		for line in lines:
			b.write(line)
		b.close()
		T.insert(END,"\nDeletion successfull")

def neg(m):
	a=open(r"C:\Users\nimit\Desktop\File-Structure-Mini-Project-main\COVIDET\negative.txt")
	lines = a.readlines()
	a.close()
	p=-1
	q=0
	for i in lines:
		q=q+1
		p=i.find(m)
		if p!=-1:
			flag=i
			break
	if p!=-1:
		del lines[q-1]
		b=open(r"C:\Users\nimit\Desktop\File-Structure-Mini-Project-main\COVIDET\negative.txt","w+")
		for line in lines:
			b.write(line)
		b.close()
		T.insert(END,"\nDeletion successfull")
		