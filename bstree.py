import random

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTree:
    head = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            p = self.head
            while True:
                if val == p.val:
                    return False
                if val < p.val:
                    if p.left is None:

                        p.left = Node(val)
                        return
                    else:
                        p = p.left
                else:
                    if p.right is None:
                        p.right = Node(val)
                        return
                    else:
                        p = p.right

    def search(self, val):
        p = self.head
        while True:
            if p is None:
                print("False")
                return False
            elif val == p.val:
                print("True")
                return True
            elif val < p.val:
                p = p.left
            else:
                p = p.right
                
        



def print_node(p): # prints tree basic way
    if p.left is not None:
        print_node(p.left)
    print(p.val)
    if p.right is not None:
        print_node(p.right)


def print_node_with_depth(p, d): #prints a tree arguements(tree,depth)
    if p.left is not None:
        print_node_with_depth(p.left, d+1)
    print("  "*d, p.val)
    if p.right is not None:
        print_node_with_depth(p.right, d+1)
        

def append_to_list(list_to_append, tree_node): # creates a sorted list from a tree
    left = tree_node.left
    right = tree_node.right

    if left is not None:
        append_to_list(list_to_append, left)

    list_to_append.append(tree_node.val)

    if right is not None:
        append_to_list(list_to_append, right)



def balance(new_tree, items): #creates a balanced tree from a list
    if len(items) == 2:
        new_tree.insert(items[1])
        new_tree.insert(items[0])
    elif len(items) > 0:
        middle = len(items)//2
        a = items[0:middle]
        b = items[middle+1:]
        new_tree.insert(items[middle])

        balance(new_tree, a)
        balance(new_tree, b)
        
        
def tree_merger(tree1, tree2): #merges 2 trees on 2nd argued tree by using append to list function
    a=[]
    append_to_list(a, tree1.head)
    for element in a:
        tree2.insert(element)
    return tree2



def balance_tree(tree,new_tree): # balances tree by using balance and append to list func.s
    c=[]
    append_to_list(c, tree.head)
    tree=BSTree()
    balance(new_tree,c)
    print_node_with_depth(new_tree.head,0)
    

t = BSTree()
e=BSTree() 
for i in range(5):
    t.insert(random.randint(0,20))
    
for i in range(5):
    e.insert(random.randint(0,20))

p = t.head
q = e.head

print_node(p)
print()
print_node(q)

tree_merger(e,t)
print()
print_node_with_depth(p,0)
print()
print()
z=BSTree()#empty tree to balance merged "t"
balance_tree(t,z)

