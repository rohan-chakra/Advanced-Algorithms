
def findMonotones(EdgeList, D_edges):

	color = {x: 'white' for x in EdgeList}
	monotoneList = []

	while EdgeList:
		monotone = []
		nextEdge = list(EdgeList.keys())[0]
		prev=None
		# nextEdge = temp.next
		while color[nextEdge] != 'grey':
			color[nextEdge] = 'grey'
			if_diag = [item for item in D_edges if item[0] == nextEdge and item[1] != prev] 
			if len(if_diag):
				monotone.append((nextEdge, if_diag[-1][1]))
				D_edges.remove(if_diag[-1])
				prev=nextEdge
				nextEdge = if_diag[-1][1]
				
			else:
				monotone.append((nextEdge, nextEdge.next))
				EdgeList.pop(nextEdge)
				prev=nextEdge
				nextEdge=nextEdge.next

		monotoneList.append(monotone)
		for x in monotone: color[x[0]] = 'white'

	print('\n\nList of Monotones:')
	for x in monotoneList:
		print('\n')
		for y in x:	print(y[0].idx, '  ',y[1].idx),'\n'

	return monotoneList