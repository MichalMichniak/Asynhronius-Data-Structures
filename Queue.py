
import threading
from copy import copy



class Asynch_Queue:
    class __queue_elem:
        def __init__(self,data,next,prev):
            self.data = data
            self.next = next
            self.prev = prev



    def __init__(self):
        self.out_lock = threading.Lock()
        self.in_lock = threading.Lock()
        self.empty_lock = threading.Lock()
        self.signal = threading.Lock()
        self.root : Asynch_Queue.__queue_elem = None
        self.last : Asynch_Queue.__queue_elem  = self.root

    def push(self,data):
        self.in_lock.acquire()
        if self.root == None:
            self.out_lock.acquire()
            self.root = Asynch_Queue.__queue_elem(data,self.root,None)
            self.last = self.root
            self.out_lock.release()
            if self.empty_lock.locked():
                self.empty_lock.release()
        else:
            self.root = Asynch_Queue.__queue_elem(data,self.root,None)
            if self.root.next != None:
                self.root.next.prev = self.root        
        self.in_lock.release()
        if self.empty_lock.locked():
                self.empty_lock.release()
    
    def pop(self):
        temp = None
        if self.root != None:
            self.out_lock.acquire()
            if not self.empty_lock.locked():
                temp = self.last.data
                if self.last.prev == None:
                    self.root = None
                    self.last = None
                    self.empty_lock.acquire()
                else:
                    self.last = self.last.prev
                    self.last.next = None
            self.out_lock.release()
        return temp
    
    def peak(self):
        temp = None
        if self.root != None:
            temp = self.last.data
        return temp
    
    def empty(self):
        return self.root == None
    
    pass