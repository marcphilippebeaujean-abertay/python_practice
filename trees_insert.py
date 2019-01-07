import random

class TreeNode:
    def __init__(self, val, root=None, height=0):
        self.root = root
        self.left = None
        self.right = None
        self.val = val
        self.height = height

    def insert(self, val, height=0):
        if val == self.val:
            return
        if val<self.val:
            if self.left == None:
                self.left = TreeNode(val, root=self, height=(self.height+1))
            else:
                self.left.insert(val)
        if val>self.val:
            if self.right == None:
                self.right = TreeNode(val, root=self, height=(self.height+1))
            else:
                self.right.insert(val)

    def get_tree_height(self):
        height_arr = []
        self._traverse_for_height(height_arr)
        return height_arr

    def _traverse_for_height(self, height_arr):
        list.append(self.height)
        if self.left != None:
            self.left._traverse_for_height(height_arr)
        if self.right != None:
            self.right._traverse_for_height(height_arr)

    def print(self):
        if self.left:
            self.left.print()
        print(f' {self.val} at height {self.height}')
        if self.right:
            self.right.print()

    def create_depth_list(self):
        depth_list = []
        depth_list = self._add_to_depth_list(depth_list, 0)
        return depth_list

    def _add_to_depth_list(self, depth_list, depth):
        if len(depth_list) <= depth:
            depth_list.append([self])
        else:
            depth_list[depth].append(self)
        if self.left:
            depth_list = self.left._add_to_depth_list(depth_list, depth+1)
        if self.right:
            depth_list = self.right._add_to_depth_list(depth_list, depth+1)
        return depth_list


def create_minimal_bst(sorted_list, start_id, end_id, height=0):
    if end_id < start_id:
        return None
    mid = (start_id + end_id) // 2
    n = TreeNode(sorted_list[mid], height=height)
    n.left = create_minimal_bst(sorted_list, start_id, mid-1, height+1)
    n.right = create_minimal_bst(sorted_list, mid+1, end_id, height+1)
    return n

list = []
for num in range(0, 10):
    rand_nr = random.randint(0, 50)
    list.append(rand_nr)
root_node = create_minimal_bst(list, 0, len(list)-1)
list = root_node.create_depth_list()
for num in list:
    print(f'{num}')