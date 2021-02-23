import random
import matplotlib.pyplot as plt
class Node:

	def __init__(self):

		self.left = None
		self.right = None


class Line(Node):

	def __init__(self,axis,value):
		Node.__init__(self)
		self.axis = axis 
		self.value = value

class Point(Node):

	def __init__(self,x,y):
		Node.__init__(self)
		self.x = x
		self.y = y

class Tdtree:
	def __init__(self):
		self.root = None

	def region(self, root, regi): 
		
		if root == None: 
			return
		
		if (root.left == None and root.right == None): 
			regi.append(root) 
			return
		
		if root.right: 
			self.region(root.right, regi) 
		
		if root.left: 
			self.region(root.left, regi) 

	def buildkdtree(self,P,depth = 0):
		n = len(P)
		if n <= 0:
			return None

		if(n==1): 
			return P[0]

		elif depth % 2 == 0:
			sorted_points = sorted(P, key=lambda point: point.x)
			median = sorted_points[n // 2]
			curnode = Line(0,median.x)
		else:
			sorted_points = sorted(P, key=lambda point: point.y)
			median = sorted_points[n // 2]
			curnode = Line(1,median.y)
		
		if(n%2==0):
			curnode.left = self.buildkdtree(sorted_points[:n // 2], depth+1)
			curnode.right = self.buildkdtree(sorted_points[n // 2:], depth+1)

		else:
			curnode.left = self.buildkdtree(sorted_points[:n // 2+1], depth+1)
			curnode.right = self.buildkdtree(sorted_points[n // 2+1:], depth+1)
		return curnode
		


	def lies_completely_inR(self, P, R):

		maxx = max(i.x for i in R)
		minx = min(i.x for i in R)
		maxy = max(i.y for i in R)
		miny = min(i.y for i in R)
		for v in P:
			if(minx<=v.x<=maxx and miny<=v.y<=maxy):
				continue
			else:
				return False
		return True

	def searchkdtree(self, v, R, final_points):
		regi_left =[]
		self.region(v.left,regi_left)
		if(v.left== None and v.right == None):
			l1 = []
			l1.append(v)
			if(self.lies_completely_inR(l1,R)):
				return l1

		elif(self.lies_completely_inR(regi_left, R)):

			final_points.append(regi_left)

		elif v.left:
			self.searchkdtree(v.left, R, final_points)

		regi_right =[]
		self.region(v.right,regi_right)
		if(self.lies_completely_inR(regi_right, R)):
			final_points.append(regi_right)
			return 

		elif v.right:
			self.searchkdtree(v.right, R, final_points)


	

COUNT=[10]
def print2DUtil(root, space) : 
	  
	if (root == None) : 
		return
	space += COUNT[0] 

	print2DUtil(root.right, space)  
	  
	print()  
	for i in range(COUNT[0], space): 
		print(end = " ")  
	if isinstance(root,Point):
		print("x-{},y-{}".format(root.x, root.y))
	else:
		print("ax-{},val-{}".format(root.axis,root.value))  
	  
	print2DUtil(root.left, space)  

def print2D(root) : 
    print2DUtil(root, 0)  


if __name__ == '__main__':
	rangeX = (0, 100)
	rangeY = (0, 100)
	qty = 7
	randPoints = []
	excluded = set()
	i = 0
	for i in range(0,qty):
		x = random.randrange(*rangeX)
		y = random.randrange(*rangeY)
		randPoints.append((x,y))

	P = list(Point(x,y) for x,y in randPoints)
	x = int(input("Enter x of lower left corner vertex of range query: "))
	y = int(input("Enter y of that vertex: "))
	height = int(input("Enter height: "))
	width = int(input("Enter width: "))
	R = [Point(x,y), Point(x+width,y), Point(x+width,y+height), Point(x,y+height)]
	t = Tdtree()
	root = t.buildkdtree(P)
	print2D(root)
	final_points = []
	t.searchkdtree(root, R, final_points)


	for i in randPoints:
		xa,ya=i
		plt.plot(xa,ya, 'ko')

	for i in final_points:
		for points in i:
			plt.plot(points.x,points.y, 'ro')

	R = [(x,y), (x+width,y), (x+width,y+height), (x,y+height)]
	R.append(R[0])
	xs, ys = zip(*R) 
	plt.plot(xs,ys) 
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()
