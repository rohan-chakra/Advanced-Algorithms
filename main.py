from util.triangulation import *
from util.avl import *
import matplotlib.pyplot as plt
from util.generate_polygon import verts
from util.cycles import findMonotones

class Vertices(Point):
	def __init__(self, x, y, idx):
		Point.__init__(self,x,y)
		self.typeOfVertex = None
		self.idx = idx

	@staticmethod
	def findType(point):
		p1 = point.prev ; p2 = point ; p3 = point.next
		val = (float(p2.y - p1.y) * (p3.x - p2.x)) - (float(p2.x - p1.x) * (p3.y - p2.y)) 
		
		# Interior angle
		if val > 0: 
			orientation = 'clockwise'	# >180 deg
		elif val < 0: 
			orientation = 'counterclockwise'# <180 deg
		else: 
			orientation = 'colinear'

		if p2.y > p1.y and p2.y > p3.y and orientation == 'clockwise':
			return 'split'
		elif p2.y < p1.y and p2.y < p3.y and orientation == 'clockwise':
			return 'merge'
		elif p2.y > p1.y and p2.y > p3.y and orientation == 'counterclockwise':
			return 'start'
		elif p2.y < p1.y and p2.y < p3.y and orientation == 'counterclockwise':
			return 'end'
		else:
			return 'regular'


class Edge:
    
	def __init__(self, point, idx):

		self.startVer = point
		self.endVer = point.next
		self.helper = None
		self.idx = idx

	myTree = AVL_Tree() ; root = None ; diagonals = []

	
	def handle_split(ver):
		E.root = E.myTree.insert(E.root, EdgeList[ver], 'point')
		E.myTree.predSuc(E.root, EdgeList[ver])
		E.root = E.myTree.delete(E.root, EdgeList[ver], 'point')
		E.diagonals.append((ver, E.myTree.pre.edge.helper))
		E.myTree.pre.edge.helper = ver
		EdgeList[ver].helper = ver
		E.root = E.myTree.insert(E.root, EdgeList[ver], 'edge')
		
	def handle_merge(ver):
		if EdgeList[ver.prev].helper.typeOfVertex == 'merge':
			E.diagonals.append((ver, EdgeList[ver.prev].helper))
		
		E.root =E.myTree.delete(E.root,EdgeList[ver.prev],'edge')
		E.root = E.myTree.insert(E.root, EdgeList[ver],'point')
		E.myTree.predSuc(E.root,EdgeList[ver])
		E.root = E.myTree.delete(E.root, EdgeList[ver],'point')
		helper_ej = E.myTree.pre.edge.helper
		if helper_ej.typeOfVertex == 'merge':
			E.diagonals.append((ver, helper_ej))
		E.myTree.pre.edge.helper = ver

	def handle_start(ver):
		E.root = E.myTree.insert(E.root,EdgeList[ver],'edge')
		EdgeList[ver].helper = ver

	def handle_end(ver):
		if EdgeList[ver.prev].helper.typeOfVertex == 'merge':
			E.diagonals.append((ver, EdgeList[ver.prev].helper))
		
		E.root = E.myTree.delete(E.root, EdgeList[ver.prev],'edge')

	def handle_regular(ver):
		if ver.next.y < ver.y:
			if EdgeList[ver.prev].helper.typeOfVertex == 'merge':
				E.diagonals.append((ver, EdgeList[ver.prev].helper))
			E.root = E.myTree.delete(E.root,EdgeList[ver.prev],'edge')
			E.root = E.myTree.insert(E.root, EdgeList[ver],'edge')
			EdgeList[ver].helper = ver
		else:
			E.root = E.myTree.insert(E.root, EdgeList[ver],'point')
			E.myTree.predSuc(E.root, EdgeList[ver])
			E.root = E.myTree.delete(E.root, EdgeList[ver],'point')
			helper_ej = E.myTree.pre.edge.helper
			if helper_ej.typeOfVertex == 'merge':
				E.diagonals.append((ver, helper_ej))
			E.myTree.pre.edge.helper = ver 
		
	symbol_tab = locals()	
	@staticmethod
	def makeMonotone(list_of_ver):

		Q = sorted(list_of_ver, key = lambda ver: ver.y) 
		while Q:
			ver = Q.pop()
			Edge.symbol_tab['handle_' + ver.typeOfVertex](ver)

	@staticmethod
	def link(S):
		for i in range(0,len(S)):

			S[i].prev = S[i-1]
			S[i].next = S[(i+1)%(len(S))]
			if S[i].typeOfVertex == None:
				S[i].typeOfVertex = Vertices.findType(S[i])

		

if __name__=='__main__':

	E = Edge

	inputs = verts
	S = [Vertices(inputs[i][0],inputs[i][1],'v'+str(i+1)) for i in range(len(inputs))]	
	E.link(S)

	EdgeList = {S[p]:Edge(S[p], 'e'+str(p+1)) for p in range(len(S))}	

	Edge.makeMonotone(S)
	print("\n\nEdges:")
	for e in EdgeList:
		print(e, "->", EdgeList[e].endVer)

	print('\n\nDiagonals:')
	for x in E.diagonals:
		print(x[0], '->',x[1])

	for key,edge in EdgeList.items():
		list_of_x = [edge.startVer.x, edge.endVer.x]
		list_of_y = [edge.startVer.y, edge.endVer.y]
		plt.plot(list_of_x, list_of_y, color = 'k')

	for d in Edge.diagonals:
		list_of_x = [d[0].x, d[1].x]
		list_of_y = [d[0].y, d[1].y]
		plt.plot(list_of_x, list_of_y, color='b')

	Mark = {'merge':"v", 'split':"^", 'start':"s",'end':"X",'regular':"o"}
	for p in S:
		plt.scatter(p.x, p.y, marker=Mark[p.typeOfVertex], color='k')

	plt.axis('equal')
	plt.title('Creation of y-Monotones & triangulation')
	
	temp = [(x[1], x[0]) for x in E.diagonals] ; E.diagonals = E.diagonals+temp
	print('D edges:')
	for i in E.diagonals:
		print(i[0].idx, '->', i[1].idx)

	monotones = findMonotones(EdgeList, E.diagonals)
	for x in monotones:
		poly = [i[0] for i in x]
		dia = triangulate(poly)
		for d in dia:
			list_of_x = [d[0].x, d[1].x]
			list_of_y = [d[0].y, d[1].y]
			plt.plot(list_of_x, list_of_y, color='red')

	plt.show()


	



				
    


