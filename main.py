import time
import tools.gc7 as gc7

def main():
    
    start = time.time()
    
    for i in range(int(1e1)+1):
        print(i*2, end=' ')
    
    end = time.time()
    duration = (end - start)
    
    print('\n'+gc7.nf(duration*1e6))
    
if __name__ == "__main__":
    main()

