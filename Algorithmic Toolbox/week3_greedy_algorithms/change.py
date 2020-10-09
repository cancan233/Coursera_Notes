# Uses python3
import sys

def get_change(m):
    #write your code here
    n = 0
    for i in [10, 5, 1]:
        n += m // i
        m = m % i
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 30
    print(get_change(m))
