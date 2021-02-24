from functools import cmp_to_key
import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.prev = None
		self.next = None

	def subtract(self, p):
		return Point(self.x - p.x, self.y - p.y)

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

def compare(p1, p2):
    if p1.y > p2.y:
        return -1
    elif p1.y < p2.y:
        return 1
  
    else:
        if p1.x > p2.x:
            return -1
        else:
            return 1
    
def different_chain(p1,p2,top_most,bottom_most):
	
	n1 = p1
	count = 0
	while n1!=top_most or n1!=bottom_most:
		n1= n1.prev
		if(n1==p2):
			count = 1
			return False
	n2 = p1
	while n2!=bottom_most or n2!=top_most:
		n2 = n2.next
		if(n2==p2):
			count = 1
			return False

	if(count ==0):
		return True
	'''	
	if(p1.prev==p2 or p1.next==p2):
		return False
	else:
		return True
	'''
def findAngle(p1,p2,p3):

	#p1 = p.prev ; p2 = point ; p3 = point.next
	return ((float(p2.y - p1.y) * (p3.x - p2.x)) - (float(p2.x - p1.x) * (p3.y - p2.y))) 
		

def ifDiagInside(x, y):
	if findAngle(x.next,x,x.prev) > findAngle(x.next, x, y):
		return False
	else:
		return True

def triangulate(S):

	sortedS = sorted(S, key= cmp_to_key(lambda a,b: compare(a,b)))

	top_most = sortedS[0]
	bottom_most = sortedS[-1]
	stack = []
	stack.append(sortedS[0])
	stack.append(sortedS[1])


	D = [] #list of diagonals to triangulate

	for j in range(2,len(sortedS)-1):

		if different_chain(sortedS[j],stack[-1],top_most, bottom_most):
			while stack:
				point = stack.pop()
				if(stack):
					D.append([sortedS[j], point])

			stack.append(sortedS[j-1])
			stack.append(sortedS[j])

		else:
			point = stack.pop()
			# while(stack and different_chain(stack[-1],sortedS[j])):
			while(stack and ifDiagInside(stack[-1],sortedS[j])):
				point = stack.pop()
				D.append([sortedS[j],point])
			stack.append(point)
			stack.append(sortedS[j])

	stack.pop()
	stack.pop(0)	
	for i in range(len(stack)):
		if(sortedS[i]!=top_most):
			D.append([bottom_most,sortedS[i]])

	return D

if __name__=='__main__':
		
	# p1 = Point(0,7); p2 = Point(1,6); p3 = Point(2,1); p4 = Point(3,0); 

	# p5 = Point(6,2); p6 = Point(5,4); p7 = Point(6,8); p8 = Point(4,10); 
	v = [(341, 151), (259, 190),(263, 314), (172, 233),(135, 225),\
	 (121, 183),(5, 161), (85, 134),(139, 143)]
	# S=[p1,p2,p3,p4,p5,p6,p7,p8]
	S = [Point(t[0],t[1]) for t in v]

	for i in range(0,len(S)):

		S[i].prev = S[i-1]
		S[i].next = S[(i+1)%(len(S))]

	D = triangulate(S)

	for i in D:
		list_of_x = [i[0].x, i[1].x]
		list_of_y = [i[0].y, i[1].y]
		plt.plot(list_of_x, list_of_y, color = 'r')
	plt.xlabel('x')
	plt.ylabel('y')


	list_of_x = []
	list_of_y = []
	for i in S:
		list_of_x.append(i.x)
		list_of_y.append(i.y)

	plt.plot(list_of_x, list_of_y, color = 'k')
	plt.plot([S[-1].x,S[0].x],[S[-1].y,S[0].y], color = 'k')
	plt.title('Triangulation of Monotone')
	plt.show()