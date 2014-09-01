#!/usr/bin/python
import random
# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
text = form.getvalue('text')
components = form.getvalue('components')

if (text==None):
	text="Please enter some text, or use the example buttons"

e = ['impedance in the COMPONENT\n', 'residual capacitance caused by the COMPONENT\n', 'crosstalk due to the proximity of the COMPONENT to the COMPONENT\n', 'voltage spikes in the COMPONENT\n', 'parasitic capacitance of the COMPONENT\n', 'voltage gitches in the COMPONENT\n', 'incorrect impedance matching between the COMPONENT and the COMPONENT\n', 'the COMPONENT not being manufactured to specification\n', 'thermal effects in the COMPONENT\n', 'electromagnetic interference\n', 'current leakage in the COMPONENT\n', 'spurious resets\n', 'excessive bridging loss\n', 'jitter in the COMPONENT clock\n', 'clock drift\n', 'the COMPONENT inducing current in the COMPONENT\n', 'stray harmonics\n', 'the internal resistance of the COMPONENT\n', 'a possible manufacturing defect in the COMPONENT\n', 'excessive heat emitted by the COMPONENT\n', 'an excessively long trace between the COMPONENT and the COMPONENT\n', 'the COMPONENT being placed too close to the COMPONENT on the PCB', 'the susceptibility of the COMPONENT to ESD', 'lack of shielding against alpha radiation (cosmic rays) in the COMPONENT', 'electromagnetic resonance']
eb = e

cb = ['LCD screen\n', 'PCB\n', 'radio tranciever\n', 'pull-up resistor\n', 'battery\n', 'power supply\n', 'capacitor C1\n', 'resistor R3\n', 'EEPROM\n', 'SPI bus\n', 'USB connector\n', 'voltage regulator\n', 'low-pass filter\n', 'decoupling capacitor\n', 'coil\n', 'anetenna\n', 'microcontroller\n', 'switch\n', 'button\n', 'IR receiver']

if (components==None):
	c = cb
else:
	c = components.split(',')

inn = text

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
		e = eb


	while (ex.find("COMPONENT")!=-1):
		i = ex.find("COMPONENT")
		comp = c[random.randrange(0, len(c))]
		c.remove(comp)
		comp = comp.strip()
		if len(c) == 0:
			c = cb
		ex = ex[:i].strip() + " " + comp + " " + ex[i + 10:].strip()

	ind = inn.find("REASON")
	if(len(inn[ind:]) < 7):
		inn = inn[:ind].strip().rstrip() + " " + ex.strip()
	else:
		inn = inn[:ind].strip().rstrip() + " " + ex.strip() + gspace(inn[ind + 6]) + inn[ind + 6:].strip().rstrip()







print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<style type=\"text/css\">body, input, textarea {font-family:Calibri,Segoe UI,Myriad Pro,Myriad,Trebuchet MS,Helvetica,Arial,sans-serif;}</style>"
print "<title>Excuses, Excuses</title>"
print "</head>"
print "<body>"
print "%s" % (inn)
print "</body>"
print "</html>"
