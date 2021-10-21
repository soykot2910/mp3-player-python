from tkinter import *
import pygame 
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk


root =Tk()
root.title('MP3 Player')
root.geometry("500x300")

pygame.mixer.init()

# Add song function
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    song_box.insert(END,song)

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    
    for song in songs:
        song_box.insert(END,song)


def next_song():
    next_one=song_box.curselection()
    next_one=next_one[0]+1
    song=song_box.get(next_one)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
 
    # clear active bar in playlist 
    song_box.select_clear(0,END)

    # Activate new song bar
    song_box.activate(next_one)
    
    # set active bar to next song
    song_box.select_set(next_one,last="None")

def prev_song():
     next_one=song_box.curselection()
     next_one=next_one[0]-1
     song=song_box.get(next_one)

     pygame.mixer.music.load(song)
     pygame.mixer.music.play(loops=0)
    
     # clear active bar in playlist 
     song_box.select_clear(0,END)

     # Activate new song bar
     song_box.activate(next_one)
        
     # set active bar to next song
     song_box.select_set(next_one,last="None")

    
def play():
    song=song_box.get(ACTIVE)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)

global paused
paused=False

def pause(is_paused):
    global paused
    paused=is_paused

    if paused:
         pygame.mixer.music.unpause()
         paused=False
    else:
        pygame.mixer.music.pause()
        paused=True

    
	

song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="green", selectforeground="black")
song_box.pack(pady=20)

# Create player control buttons image
back_btn_img=PhotoImage(file='images/back50.png')
forward_btn_img=PhotoImage(file='images/forward50.png')
play_btn_img=PhotoImage(file='images/play50.png')
pause_btn_img=PhotoImage(file='images/pause50.png')
stop_btn_img=PhotoImage(file='images/stop50.png')

# Create player control Frame
controls_frame=Frame(root)
controls_frame.pack()


# Create player control button
back_btn=Button(controls_frame,image=back_btn_img, borderwidth=0,command=prev_song)
forward_btn=Button(controls_frame,image=forward_btn_img, borderwidth=0,command=next_song)
play_btn=Button(controls_frame,image=play_btn_img, borderwidth=0,command=play)
pause_btn=Button(controls_frame,image=pause_btn_img, borderwidth=0,command=lambda: pause(paused))
stop_btn=Button(controls_frame,image=stop_btn_img, borderwidth=0,command=stop)

back_btn.grid(row=0, column=0,padx=10)
forward_btn.grid(row=0, column=1,padx=10)
play_btn.grid(row=0,column=2,padx=10)
pause_btn.grid(row=0,column=3,padx=10)
stop_btn.grid(row=0,column=4,padx=10)

# Create menu
my_menu=Menu(root)
root.config(menu=my_menu)

# Add song menu
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command(label="Add  One Song To Playlist",command=add_song)

# add many song
add_song_menu.add_command(label="Add  Many Song To Playlist",command=add_many_songs)



root.mainloop()