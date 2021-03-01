import time


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
    sing()
    dang()

if __name__ == "__main__":
    main()
