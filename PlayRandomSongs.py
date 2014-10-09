import webbrowser
import time
import random

def func():
    text = "http://www.youtube.com/watch?v=YKDZ4zQCQnI http://www.youtube.com/watch?v=YKDZ4zQCQnI http://www.youtube.com/watch?v=325tB8Qhi8s http://www.youtube.com/watch?v=NcJ_VTslIJIhttp://www.youtube.com/watch?v=vXnQf--8-kE"
    songs = text.split()
    while(1):
        webbrowser.open(songs[random.randint(1,len(songs))])
        time.sleep(1000) 

func()
