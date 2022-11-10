from core.basic import *
from core.extend_interface import *
import queue
import threading
import time


class FOFA_Scan():
    def __init__(self,queue):
        self.queue = queue
        print('Fofa扫描器启动')
    def run(self):
        while not queue.empty():
            try:
                data = whatweb(queue.get())
                print(data.json())
            except:
                pass


if __name__ == '__main__':
    queue = queue.Queue()
    for i in get_fofa_result():
        queue.put(i[0])
    scan = FOFA_Scan(queue)
    threading_list = []
    for i in range(1,10):
        t = threading.Thread(target=scan.run)
        t.setDaemon(True)
        t.start()
        threading_list.append(t)
    for k in threading_list:
        k.join()
