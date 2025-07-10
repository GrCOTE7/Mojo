import time
import tools.gc7 as gc7

def main():
    start = time.time()
    sum = 0
    for i in range(1,int(1e8+1)):
        sum += i
    end = time.time()
    duration = end - start
    print(gc7.nf(sum,0))
    print(gc7.nf(duration))
    
if __name__ == "__main__":
    main()

