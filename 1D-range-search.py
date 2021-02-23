class Node: 
	def __init__(self, d): 
		self.data = d 
		self.left = None
		self.right = None

def sortedArrayToBST(arr): 
	
	if not arr: 
		return None

	mid = (len(arr)) // 2
	
	root = Node(arr[mid]) 
	
	root.left = sortedArrayToBST(arr[:mid]) 
	
	root.right = sortedArrayToBST(arr[mid+1:]) 
	return root 

arr = [1, 2, 3, 4, 5, 6, 7] 
root = sortedArrayToBST(arr) 

def region(root, regi): 
		
	if root == None: 
		return
	
	if (root.left == None and root.right == None): 
		regi.append(root) 
		return
		
	if root.right: 
		self.region(root.right, regi) 
		
	if root.left: 
		self.region(root.left, regi) 

def FindSplitNode(root, x1, x2):
	v = root
	while((v.left!= None or v.right!= None) and (x2 <= v.data or x1 > v.data)):
		if(x2 <= v.data):
			v = v.left

		else:
			v = v.right
	return v 

def OneDRangeQuery(root, x1, x2, report):
	v_split = FindSplitNode(root, x1, x2)
	print(v_split.data)
	right_regi = []
	left_regi = []
	
	if(v_split.left== None and v_split.right== None):
		print("HI!")
		if(v_split.data <= x2 and v_split.data >= x1):
			report.append(v_split)

	else:
		report.append(v_split)
		v = v_split.left
		while(v.left !=None or v.right!= None):
			if(x1 <= v.data):
				region(v.right,right_regi)
				report.append(v)
				report.append(right_regi)
				v = v.left

			else:
				v = v.right
		if(v.data >=x1 and v.data <=x2):
			report.append(v)


		v = v_split.right
		while(v.left !=None or v.right!= None):
			if(x2 >= v.data):
				region(v.left, left_regi)
				report.append(v)
				report.append(left_regi)
				v = v.right

			else:
				v = v.left
		if(v.data >= x1 and v.data <= x2):
			report.append(v)




x1 = int(input("Enter lower limit of range:"))
x2 = int(input("Enter upper limit of range:"))
root = sortedArrayToBST([1,2,3,4,5,6,7])
report = []
OneDRangeQuery(root,x1,x2, report)
for i in report:
	if type(i)==list:
		for j in i:
			print(j.data, end = ' ')

	else:
		print(i.data,end = ' ')
