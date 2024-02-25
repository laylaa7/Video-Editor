from tkinter import *
from PIL import Image , ImageTk
from tkinter import filedialog
import shutil
from moviepy import*
from moviepy.editor import *
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"

#todo: minutes and seconds format in time
# the processing time  ( loader)
#intro vid in each subclip ( transition fade in ) 
# fade in - fade out - fade in

window = Tk() 
window.geometry("600x450")
window.title("video editing interface by layla")

def validate_timepoints(text):
    
    if not text:
        return True, 0
    
    parts = text.split(',')
    count = 0 
    
    for part in parts:
        
        part = part.strip()
        times = part.split('-')
        
        if len(times) != 2:
            return False, count
        
        
        if not times[0].isdigit() or not times[1].isdigit():
            return False, count
        
        
        count += 1
    
    return True, count

def process_clips():
    text = timepoints.get()
    # check user input
    valid, count = validate_timepoints(text)
    
    if valid:
        print("Submitted text:", text)
        print("Number of 'start-end' pairs:", count)
        invalid.config(text="")  
        
        vidtext=video1.get()
        clip = VideoFileClip(vidtext)

        outputfiletext=folder.get()
        
        for i in range(count):
            start_end = timepoints.get().split(',')[i].strip().split('-')
            start, end = int(start_end[0]), int(start_end[1])
            
            
            subclip = clip.subclip(start, end)
            
            
            output_filename = f"subclip_{i+1}.mp4"
            
            
            subclip.write_videofile(output_filename)
            
            # Move the output file to the specified output folder
            shutil.move(output_filename, outputfiletext) 
            
        print("Clips processed and moved to specified folder.")   
    else:
          invalid.config(text="Invalid format. Please use the format: start-end, start-end, ...")
          print("invalid")

def select_folder():
    
    folder_path = filedialog.askdirectory(title="Select a folder for video files")
    
    if folder_path:  
        
        folder.insert(0,folder_path)
        print("Selected folder for video files:", folder_path)

def browse_vidfile():
    filename = filedialog.askopenfilename(title="select a video file" , filetypes=(("Video files","*.mp4 *.mov"),("All files","*,*"))) 
    if filename: 
        video1.insert(0,filename)
        print("Selected file:", filename)
    
def browse_vidfile2():
    filename2 = filedialog.askopenfilename(title="select a video file" , filetypes=(("Video files","*.mp4 *.mov"),("All files","*,*")))
    if filename2: 
        finalfile.insert(0,filename2)
        print("Selected file:", filename2)
        
def intro():
    text4 = finalfile.get()
    text5=folder.get()
    shutil.move(text4, text5) 

    
   
label1 = Label(window,text="Input video File:").grid(row=0,column=0)
video1 = Entry(window)
video1.grid(row=0,column=1)
Buttonexplore = Button(window,text="browse",command=browse_vidfile).grid(row=0,column=2)

label2 = Label(window,text="Output Folder :").grid(row=1,column=0) 
Buttonfolder = Button(window,text="browse",command=select_folder).grid(row=1,column=2)
folder= Entry(window)
folder.grid(row=1,column=1)


label3= Label(window,text="Intro Video File (Optional) :").grid(row=2,column=0)
finalfile = Entry(window)
finalfile.grid(row=2,column=1)
Buttonfile = Button(window,text="browse",command=browse_vidfile2).grid(row=2,column=2)

label4 = Label(window,text="Time Points (format: start-end , start-end ): ").grid(row=3,column=0)
timepoints= Entry(window)
timepoints.grid(row=3,column=1)
#timebuttons = Button(window,text="browse",command=browse_file).grid(row=3,column=2)

#def proceesvideo():
invalid = Label(window, fg="red")
invalid.grid(row=5, column=0, columnspan=2)


submitbutton= Button(window,text="process",command=lambda:(process_clips(),intro()))
submitbutton.grid(row=4,column=1)

window.mainloop()