import time
import threading


def sing():
    """唱歌5秒钟"""
    for i in range(5):
        print("----正在唱菊花茶----")
        time.sleep(1)


def dang():
    """唱歌5秒钟"""
    for i in range(5):
        print("---正在跳舞---")
        time.sleep(1)
        

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dang)
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()
