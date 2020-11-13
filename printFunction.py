from __future__ import print_function

def printFunc(n):
    for i in range(n):
       print(i+1,sep=' ',end='')

if __name__ == '__main__':
    n = int(raw_input())
    printFunc(n)

