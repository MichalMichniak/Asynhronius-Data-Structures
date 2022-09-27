from sys import argv
import threading
import time
import Queue

N = 10000
print_lock = threading.Lock()
def print_thread(queue : Queue.Asynch_Queue,nr):
    while not queue.signal.locked():
        # time.sleep(1)
        if (x:=queue.pop()) != None:
            # print_lock.acquire()
            print(f"{nr}:{x}")
            # print_lock.release()


def push_thread(queue : Queue.Asynch_Queue):
    for i in range(N):
        #time.sleep(0.01)
        queue.push(i)
    time.sleep(1)
    if not queue.signal.locked():
        queue.signal.acquire()


def main():
    queue = Queue.Asynch_Queue()
    a_thr = threading.Thread(target = push_thread, args = [queue])
    aa_thr = threading.Thread(target = push_thread, args = [queue])
    b_thr = threading.Thread(target = print_thread, args = [queue,0])
    c_thr = threading.Thread(target = print_thread, args = [queue,1])

    aa_thr.start()
    a_thr.start()
    b_thr.start()
    c_thr.start()
    aa_thr.join()
    a_thr.join()
    b_thr.join()
    c_thr.join()

if __name__ == '__main__':
    main()