#binary search tree
#insertion and search
# first create a binary tree and then do a search or traversal

class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

#insertion
def insert(root,node):
	if root is None:
		root = node
	elif node.val<root.val:
		if root.left is None:
			root.left = node
		else:
			insert(root.left,node)
	else:
		if root.right is None:
			root.right = node
		else:
			insert(root.right,node)

			
#inorder traversal -increasingly sorted
def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)

def preorder(root):
	if root:
		print(root.val)
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.val)

def minval(root):
	current = root
	while(current.left is not None):
		current = current.left
	return current

def maxval(root):
	current = root
	while(current.right is not None):
		current = current.right
	return current

def deleteNode(root,key):
	if root is None:
		return root
	if key < root.val:
		root = deleteNode(root.left,key)
	elif key > root.val:
		root = deleteNode(root.right,key)
	else:
		#no child/leaf node
		if root.left is None and root.right is None:
			temp = root
			root = None
			return temp
			
		# node with one child 
		if root.left is None:
			temp = root.right
			root.val = temp.val
			root.right = None
			return temp
			
		if root.right is None:
			temp = root.left
			root.val = temp.val
			root.left = None
			return temp
			
		# node with 2 children
		if root.left is not None and root.right is not None:
			temp = minval(root.right)
			root.val = temp.val
			root.right = deleteNode(root.right, temp.val)
	
	return root	
	
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))

inorder(r) #sorted
# preorder(r)
# postorder(r)
# print(minval(r).val)
# print(maxval(r).val)

print('new')
deleteNode(r,20)
print('new one')
inorder(r)