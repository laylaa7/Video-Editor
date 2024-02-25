import shutil
from moviepy import*
from moviepy.editor import *
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"

clip = VideoFileClip("videos/Download.mp4")
numofclip = int(input("enter number of clips"))
outputfolder="/Users/laylamuhammed/Desktop/layla 2"

for i in range(numofclip):
  start = int(input("start :"))
  end = int(input("end :"))
  subclip = clip.subclip(start,end)
  output_filename = f"subclip_{i+1}.mp4"
  #combined = concatenate_videoclips([clip])
  subclip.write_videofile(output_filename)
  shutil.move(output_filename, outputfolder) 

  
clip.close()

  #from 0 sec to 5 sec

#clip=clip.cutout(2,4)

#clip.ipython_display(width = 360)


