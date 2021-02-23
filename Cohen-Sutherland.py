import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
#problem 2

xmax = 10.0
ymax = 9.0
xmin = 4.0
ymin = 2.0

INS = 0 # 0000 
L = 1 # 0001 
R = 2 # 0010 
BOT = 4 # 0100 
TOP = 8	 # 1000 

def code(x, y): 
	code = INS 
	if x < xmin:	 
		code = L 
	elif x > xmax: 
		code = R 
	if y < ymin:	  
		code = BOT 
	elif y > ymax:  
		code = TOP 

	return code 


def CS(x1, y1, x2, y2): 

	code1 = code(x1, y1) 
	code2 = code(x2, y2) 
	result = False

	while True: 

		if code1 == 0 and code2 == 0: 
			result = True
			break

		elif (code1 & code2) != 0: 
			break

		else: 

			x = 0
			y = 0
			if code1 != 0: 
				code_out = code1 
			else: 
				code_out = code2 

			if code_out & TOP: 
				
				x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1) 
				y = ymax 

			elif code_out & BOT: 
				
				x = x1 + (x2 - x1) *(ymin - y1) / (y2 - y1) 
				y = ymin 

			elif code_out & R: 
				
				y = y1 + (y2 - y1) *(xmax - x1) / (x2 - x1) 
				x = xmax 

			elif code_out & L: 
				
				y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1) 
				x = xmin 

			if code_out == code1: 
				x1 = x 
				y1 = y 
				code1 = code(x1, y1) 

			else: 
				x2 = x 
				y2 = y 
				code2 = code(x2, y2) 

	if result: 
		print ("Portion of line inside %.1f, %.1f to %.1f, %.1f" % (x1, y1, x2, y2)) 

	else: 
		print("Line outside") 

CS(4, 4, 8, 8) 
CS(2, 2, 4, 1) 


fig, ax = plt.subplots()


ax.add_patch(Rectangle((4, 2), 10, 9, fill = False))
ax.plot([4, 8],[4, 8])
ax.plot([2,4],[1,2])

plt.show()
