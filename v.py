import threading 
from os import system
import sys  

def run_face(): 
    system('python3 tz.py')
  
def vid_play(video_path): 
    cmf = "vlc"+" "+video_path+" >& log"
    system(cmf) 

if __name__ == "__main__": 
    # creating thread 
    v=sys.argv[1]
    t1 = threading.Thread(target=vid_play, args=(v,)) 
    t2 = threading.Thread(target=run_face, args=()) 
  
    t1.start() 
    t2.start() 
  
    t1.join() 
    t2.join() 
  
    print("Thanks for using !") 
