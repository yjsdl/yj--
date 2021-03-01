import threading
import time

#定义一个全局变量
g_num = 0

def test1(num):
    global g_num
    # 上锁，，如果之前没有被上锁，那么此时上锁成功
    # 如果上锁之前已经被锁上了，那么此时会堵塞到这里，直到这个锁被解开
    mutex.acquire()
    for i in range(num):
        g_num += 1
    # 解锁
    mutex.release()
    print("----in test1--g_num=%d---" % g_num)

def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("----in test2--g_num=%d--" % g_num)

#创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))

    t1.start()
    t2.start()

    # 等待上面的线程执行完毕
    time.sleep(5)
    
    print("---in main Thread g_num = %d---" % g_num)

if __name__ == "__main__":
    main()
