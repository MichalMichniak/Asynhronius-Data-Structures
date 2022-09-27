import threading
# unfinished
class Asynch_BST:
    class __BST_elem:
        def __init__(self,key,data,right = None, left=None):
            self.right = right
            self.left = left
            self.node_lock = threading.Lock()
            self.left_lock = threading.Lock()
            self.right_lock = threading.Lock()
            self.data = data
            self.key = key
            self.del_lock = threading.Lock()

        def left(self):
            return self.left    

        def right(self):
            return self.right

    def __init__(self):
        self.root = None
        self.root_lock = threading.Lock()

    def push_empty_left(self,elem : __BST_elem ,key,data):
        if not elem.del_lock.locked():
            temp = 0
            elem.left_lock.acquire()
            if elem.left == None:
                elem.left = Asynch_BST.__BST_elem(key,data)
            else:
                temp = 1
            elem.left_lock.release()
            return temp
        else:
            raise ValueError()
    
    def push_empty_right(self,elem : __BST_elem ,key,data):
        if not elem.del_lock.locked():
            temp = 0
            elem.right_lock.acquire()
            if elem.left == None:
                elem.left = Asynch_BST.__BST_elem(key,data)
            else:
                temp = 1
            elem.right_lock.release()
            return temp
        else:
            raise ValueError()

    def dellete(self,key):
        pass
        
