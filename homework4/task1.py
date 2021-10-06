
class Node(object):
    def __init__(self, item):
        self.value = item
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None
    # 层序建立二叉树的元素
    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.left == None:
                temp.left = node
                return
            else:
                queue.append(temp.left)
            if temp.right == None:
                temp.right = node
                return
            else:
                queue.append(temp.right)

    def preorder(self,node):
        if node == None:
            return
        print(node.value,end = ' ')
        self.preorder(node.left)
        self.preorder(node.right)

    def recur_preorder(self):
        s = [self.root]
        while s:
            temp = s.pop(-1)
            print(temp.value,end = ' ')
            if temp.right != None:
                s.append(temp.right)
            if temp.left != None:
                s.append(temp.left)

    def midorder(self,node):
        if node == None:
            return
        self.midorder(node.left)
        print(node.value,end = ' ')
        self.midorder(node.right)

    def recur_midorder(self):
        stack = []
        node = self.root
        while len(stack)>0 or node != None:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.value,end = ' ')
                node = node.right
            
    def postorder(self,node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value,end = ' ')

    def recur_postorder(self):
        stack = [self.root]
        stack2 = []
        while len(stack) > 0:
            temp = stack.pop()
            stack2.append(temp)
            if temp.left != None:
                stack.append(temp.left)
            if temp.right != None:
                stack.append(temp.right)
        while len(stack2)>0:
            print(stack2.pop(-1).value,end = ' ')



if __name__ == '__main__':
    while True:
        try:
            s = input().split()
            a = [int(i) for i in s]
            tree = Tree()
            for i in a:
                tree.add(i)
            print('前序遍历为：')
            tree.preorder(tree.root)
            print()
            tree.recur_preorder()
            print()
            print('中序遍历为：')
            tree.midorder(tree.root)
            print()
            tree.recur_midorder()
            print()
            print('后序遍历为：')
            tree.postorder(tree.root)
            print()
            tree.recur_postorder()


        except:
            break