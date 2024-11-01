
import os
import platform
import time
import pygame  

def play_music(music_file, duration):
    
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)  
    pygame.mixer.music.play() 

    
    time.sleep(duration)
    pygame.mixer.music.stop()

def shutdown_computer():
   
    print("Yes shit, yes thank you so much, thank you...")
    time.sleep(5)

   
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown -h now")
    else:
        print("Sistema operacional não suportado.")

def main():
    music_file = "yestks.mp3"  
    play_duration = 9  
    print("Tocando a música...")
    play_music(music_file, play_duration)  

    
    shutdown_computer()

if __name__ == "__main__":
    main()
