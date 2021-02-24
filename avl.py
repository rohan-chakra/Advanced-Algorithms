from util.triangulation import Point
#from monotone import Edge

class TreeNode(object): 
	def __init__(self, edge, element): 
		self.edge = edge
		self.val = {'point' :edge.startVer.x, 'edge': (edge.startVer.x+edge.endVer.x)/2.0}[element]
		self.left = None
		self.right = None
		self.height = 1
		self.element = element

# AVL tree class which supports insertion, 
# deletion operations 
class AVL_Tree(object): 

	def __init__(self):
		self.pre = None
		self.suc = None

	def insert(self, root, edge, element): 
		
		val = {'point' :edge.startVer.x, 'edge': (edge.startVer.x+edge.endVer.x)/2.0}[element]
		if not root: 
			return TreeNode(edge,element) 
		elif val < root.val: 
			root.left = self.insert(root.left, edge, element) 
		else: 
			root.right = self.insert(root.right, edge,element) 

		# Step 2 - Update the height of the 
		# ancestor node 
		root.height = 1 + max(self.getHeight(root.left), 
						self.getHeight(root.right)) 

		# Step 3 - Get the balance factor 
		balance = self.getBalance(root) 

		 
		if balance > 1 and val < root.left.val: 
			return self.rightRotate(root) 

		# Case 2 - Right Right 
		if balance < -1 and val > root.right.val: 
			return self.leftRotate(root) 

		# Case 3 - Left Right 
		if balance > 1 and val > root.left.val: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		# Case 4 - Right Left 
		if balance < -1 and val < root.right.val: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

	
	def delete(self, root, edge, element): 

		val = {'point' :edge.startVer.x, 'edge': (edge.startVer.x+edge.endVer.x)/2.0}[element]
		if not root: 
			return root 

		elif val < root.val: 
			root.left = self.delete(root.left, edge, element) 

		elif val > root.val: 
			root.right = self.delete(root.right, edge, element) 

		else: 
			if root.left is None: 
				temp = root.right 
				root = None
				return temp 

			elif root.right is None: 
				temp = root.left 
				root = None
				return temp 

			temp = self.getMinValueNode(root.right) 
			# root.val = temp.val 
			root.edge = temp.edge ; root.val = temp.val ; root.element = temp.element
			root.right = self.delete(root.right, temp.edge, temp.element) 

		# If the tree has only one node, 
		# simply return it 
		if root is None: 
			return root 

		# Step 2 - Update the height of the 
		# ancestor node 
		root.height = 1 + max(self.getHeight(root.left), 
							self.getHeight(root.right)) 

		# Step 3 - Get the balance factor 
		balance = self.getBalance(root) 

		# Step 4 - If the node is unbalanced, 
		# then try out the 4 cases 
		# Case 1 - Left Left 
		if balance > 1 and self.getBalance(root.left) >= 0: 
			return self.rightRotate(root) 

		# Case 2 - Right Right 
		if balance < -1 and self.getBalance(root.right) <= 0: 
			return self.leftRotate(root) 

		# Case 3 - Left Right 
		if balance > 1 and self.getBalance(root.left) < 0: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		# Case 4 - Right Left 
		if balance < -1 and self.getBalance(root.right) > 0: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

	def leftRotate(self, z): 

		y = z.right 
		T2 = y.left 

		# Perform rotation 
		y.left = z 
		z.right = T2 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		# Return the new root 
		return y 

	def rightRotate(self, z): 

		y = z.left 
		T3 = y.right 

		# Perform rotation 
		y.right = z 
		z.left = T3 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		# Return the new root 
		return y 

	def getHeight(self, root): 
		if not root: 
			return 0

		return root.height 

	def getBalance(self, root): 
		if not root: 
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right) 

	def getMinValueNode(self, root): 
		if root is None or root.left is None: 
			return root 

		return self.getMinValueNode(root.left) 

	def inOrder(self, root): 

		if not root: 
			return

		self.inOrder(root.left) 
		print("{0} ".format(root.val), end="") 
		self.inOrder(root.right)

	def predSuc(self,root, edge): 	# find Predecessor & Successor
		
		
		if root is None: 
			return
	
		val = edge.startVer.x 
		if root.val == val: 
	
			# the maximum value in left subtree is predecessor 
			if root.left is not None: 
				tmp = root.left  
				while(tmp.right): 
					tmp = tmp.right  
				self.pre = tmp 
	
	
			# the minimum value in right subtree is successor 
			if root.right is not None: 
				tmp = root.right 
				while(tmp.left): 
					tmp = tmp.left  
				self.suc = tmp  

			return 
	
		# If val is smaller than root's val, go to left subtree 
		if root.val > val : 
			self.suc = root  
			self.predSuc(root.left, edge) 
	
		else: # go to right subtree 
			self.pre = root 
			self.predSuc(root.right, edge)

		


	


