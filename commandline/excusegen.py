import random

f = open("input.txt", 'r')
inn = f.read()
f.close()



f = open("excuses.txt", 'r')
e = f.readlines()
f.close()

f = open("components.txt", 'r')
c = f.readlines()
f.close()

#print e

#print c

def gspace(a):
	if ((a=='.')|(a==',')):
		return ""
	else:
		return " "


while inn.find("REASON")!=-1:
	ex = e[random.randrange(0, len(e))]
	e.remove(ex)
	ex = ex.strip()
	if len(e) == 0:
		f = open("excuses.txt", 'r')
		e = f.readlines()
		f.close()


	while (ex.find("COMPONENT")!=-1):
		i = ex.find("COMPONENT")
		comp = c[random.randrange(0, len(c))]
		c.remove(comp)
		comp = comp.strip()
		if len(c) == 0:
			f = open("components.txt", 'r')
			c = f.readlines()
			f.close()
		ex = ex[:i].strip() + " " + comp + " " + ex[i + 10:].strip()

	ind = inn.find("REASON")
	inn = inn[:ind].strip().rstrip() + " " + ex.strip() + gspace(inn[ind + 6]) + inn[ind + 6:].strip().rstrip()
print inn 
