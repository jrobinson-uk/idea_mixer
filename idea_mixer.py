from tkinter import *
from PIL import Image,ImageTk
import glob
from time import sleep
import random
from gpiozero import Button


button = Button(4)

files = glob.glob("/home/pi/idea_mixer/*.png")

images={}
inputs=[]
outputs=[]
misc=[]
items=[None,None,None]

window = Tk()

window.overrideredirect(1)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
space=int(screen_width/40)
maxsize=(space*12,space*12)
vpad=(screen_height-maxsize[0])/4
textstyle = ("roboto",16,"bold")


print(screen_width,screen_height,space,maxsize)

window.geometry("{0}x{1}+0+0".format(screen_width,screen_height))
window.focus_set()

for file in files:
    im = Image.open(file)
    start=file.find("(")+1
    end = file.find(")")
    name = file[start:end]
    name = name.replace(" ","\n")
    print(name)
    if "in(" in file:
        inputs.append(name) #im.resize(maxsize)
    elif "out(" in file:
        outputs.append(name) #=im.resize(maxsize)
    else:
        misc.append(name)
    images[name]=ImageTk.PhotoImage(im.resize(maxsize))

#    print(file,name,inputs,misc,outputs)


print(images)



inputImg = Label(window,bd = 1,highlightthickness=4)
inputImg.grid(row=0,column=0,sticky=N+E+S+W,padx=space,pady=vpad)
inputLabel = Label(window,font=textstyle)
inputLabel.grid(row=1,column=0,sticky=N,padx=space)

miscImg = Label(window)
miscImg.grid(row=0,column=1,sticky=N+E+S+W,pady=vpad)
miscLabel = Label(window,font=textstyle)
miscLabel.grid(row=1,column=1,sticky=N,padx=space)

outputImg = Label(window)
outputImg.grid(row=0,column=2,sticky=N+E+S+W,padx=space,pady=vpad)
outputLabel = Label(window,font=textstyle)
outputLabel.grid(row=1,column=2,sticky=N,padx=space)


def set_images():
    #rand_in = random.choice(inputs)
    #rand_misc = random.choice(inputs+misc+outputs)
    #rand_out = random.choice(outputs)

    #print (rand_in,rand_misc,rand_out)

    inputImg.config(image=images[items[0]])
    miscImg.config(image=images[items[1]])
    outputImg.config(image=images[items[2]])
    inputLabel.config(text=items[0])
    miscLabel.config(text=items[1])
    outputLabel.config(text=items[2])







def main():
    while True:
      #  input()       
        button.wait_for_press()
        print("pressed")
        for x in range (15):
            if x<5:
                items[0] = random.choice(inputs)
            if x<10 or items[1] == items[0]:
                items[1] = random.choice(inputs+misc+outputs)
            if x<15 or items[2] == items[0] or items[2] == items[1]:
                items[2] = random.choice(outputs)
                
            set_images()

            window.update_idletasks()
            sleep(0.1)

        







##def set_labels(text=False):
##    rand_in = random.choice(inputs)
##    rand_misc = random.choice(inputs+misc+outputs)
##    rand_out = random.choice(outputs)
##
##    print (rand_in,rand_misc,rand_out)
##
##    inputImg.config(image=images[rand_in])
##    miscImg.config(image=images[rand_misc])
##    outputImg.config(image=images[rand_out])
##    if text==True:
##        inputLabel.config(text=rand_in)
##        miscLabel.config(text=rand_misc)
##        outputLabel.config(text=rand_out)
##
##def main():
##    while True:
##        button.wait_for_press()
##        print("pressed")
##        for x in range (10):
##            print("inner loop")
##            set_labels(text=True)
##            window.update_idletasks()
##            sleep(0.1)
              

window.after(1000,main)
window.mainloop()
