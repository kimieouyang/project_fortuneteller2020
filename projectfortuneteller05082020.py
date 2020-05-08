from microbit import *
import random
import time
import music

#Project finalized version May 8th,2020
#Please connect your buzzer to listen to music!
#1.Display fortune teller machine instruction 
#2.An asker input frmo sensor(cover and shake the LED screen)
#3.Display "loading graphes" as the universe is receiving the asker's question 
#4.Press btn to finish the asking
#5.Random display a positive msg from system msg set with a random song in the background 



#setup
msgs = ["You got this!!Keep rolling!", 
        "The universe is listening to you", 
        "Be on the alert to recognize your prime at whatever time of your life it may occur", 
        "Your road to glory will be rocky, but fulfilling", 
        "Patience is your alley at the moment. Don’t worry!", 
        "Nothing is impossible to a willing heart", 
        "You don’t need strength to let go of something. What you really need is understanding",
        "If you want the rainbow, you have to tolerate the rain",
        "Success lies in the hands of those who wants it",
        "Do the thing you fear and the death of fear is certain",
        "We must always have old memories and young hopes",
        "Focus on the magic of things; yourself",
        "The middle of the process is no place to determine the end of it",
        "Follow what calls you",
        "Be passionate and totally worth the chaos",
        "A fresh start will put you on your way",
        "A pleasant surprise is waiting for you",
        "Adventure can be real happiness",
        "All the effort you are making will ultimately pay off",
        "Allow compassion to guide your decisions",
        "Any decision you have to make tomorrow is a good decision",
        "Happiness begins with facing life with a smile and a wink",
        "Keep your face to the sunshine and you will never see shadows",
        "The sure way to predict the future is to invent it",
        "Time and patience are called for many surprises await you!"]
 
#The different fragments from "The entertainer"
fg1213 = ['d4:1', 'd#', 'e', 'c5:2', 'e4:1', 'c5:2','e4:1', 'c5:5','r:2', 'c5:1', 
'd5', 'd#', 'e5', 'c5', 'd5', 'e5:2', 'b4:1', 'd5:2', 'c5:5','r:2',
'd4:1', 'd#', 'e', 'c5:2', 'e4:1', 'c5:2','e4:1', 'c5:5','r:2', 'a4:1', 
'g', 'f#', 'a', 'c5', 'e:2', 'd:1', 'c', 'a4', 'd5:5','r:2']

fg124 = ['d4:1', 'd#', 'e', 'c5:2', 'e4:1', 'c5:2','e4:1', 'c5:5','r:2', 'c5:1', 
'd5', 'd#', 'e5', 'c5', 'd5', 'e5:2', 'b4:1', 'd5:2', 'c5:5','r:2', 'c5:1', 'd', 
'e', 'c', 'd', 'e:2', 'c:1', 'd', 'c', 'e', 'c', 'd', 'e:2', 'c:1', 'd', 'c', 'e', 
'c', 'd', 'e:2', 'b4:1', 'd5:2', 'c:5','r:2']

fg56 = ['e4:1', 'f', 'f#', 'g:2', 'a:1', 'g:2', 'e:1', 'f', 'f#', 'g:2', 
'a:1', 'g:2', 'e5:1', 'c', 'g4', 'a', 'b', 'c5', 'd', 'e', 'd', 'c', 'd', 'c:4','r:2',
'g4:1', 'f#', 'g', 'c5:2', 'a4:1', 'c5:2', 'a4:1', 'c5', 'a4', 'g', 'c5', 'e', 'g:2', 
'e:1', 'c', 'g4', 'a:2', 'c5', 'e:1', 'd:2', 'c:5', 'r:2']


song_list = [music.PRELUDE, music.NYAN, music.PYTHON, music.CHASE, fg1213, fg124, fg56]
arrow_image_list = [Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW]
#another animate img setup 
pattern1 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "99999")

pattern2 = Image("00000:"
              "00000:"
              "00000:"
              "99999:"
              "99999")

pattern3 = Image("00000:"
              "00000:"
              "99999:"
              "99999:"
              "99999")

pattern4 = Image("00000:"
              "99999:"
              "99999:"
              "99999:"
              "99999")

pattern5 = Image("99999:"
              "99999:"
              "99999:"
              "99999:"
              "99999")

pattern6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")
all_patterns = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6]

#intro
display.show(Image.HAPPY)
sleep(2000)
display.scroll('cover & shake board while asking question', delay=100)
display.scroll('press any btn to finish asking', delay=100)
 
while True:
    was_shook = accelerometer.was_gesture("shake")
    is_low_light = display.read_light_level() < 20
    any_button = button_a.is_pressed() or button_b.is_pressed()
    if was_shook and is_low_light:
        #cover the board to start the asking process like just like hold hands to ask with eyes closed
        #I tried to set a variable to combine shake and cover actions but failed
        #and sometimes the light sensor is too sensitive, don't know how to make it not so sensitive
        display.show(arrow_image_list)
        display.show(all_patterns, loop=True, delay=600, wait=False)
    if any_button:    
        #press to finish asking
        time.sleep(1)
        #show animated image as the loading indicator 
        music.play(random.choice(song_list), loop=True, wait=False)
        #play a random song to cheer up the asker
        display.scroll(random.choice(msgs), delay=100) 
        music.stop()
        #show the random positice msg to the asker
        display.show(Image.HAPPY)
        sleep(2000)
        #indicate the process is done
