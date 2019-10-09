#comments
#!/usr/bin/python3
#© 2019 copyright HAMOTA
#BE CREATIVE

#modules
#import file
#import pickle
#import schedule
#import commands
import random
import curses
import os
import SendKeys
import fcntl
from time import sleep
import pyglet

#5_sec_timer_with_numbers
def timer():
	print(" *5*")
	sleep(1)
	print(" *4*")
	sleep(1)
	print(" *3*")
	sleep(1)
	print(" *2*")
	sleep(1)
	print(" *1*")
	sleep(1)
	print(" *0*")

#every_thing_must_be_in_lower_Case
#text_coloring_system
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
MAGNATA = '\033[95m'
GREY = '\033[90m'
BLACK = '\033[90m'
DEFAULT = '\033[99m'
BLUE = '\033[94m'

#emojie_convertor
class emojies:
	SMILE = '🙂'
	STRANGE = '😥'
	CONFUSED = '😕'
	AMAZED = '😲'
	FEAR = '😨'
	DIZZY = '😵'
	GRAVE = '⚰️'
	FIRE = '🔥'

#main_input_system
user_name = ""
user_command = ""
story_command = ""
exit_command = ""
music_path_command = ""	

#the_introduction
print('\033c')
print(BLUE + f"""
 
 welcome!
 this is one of the best games in the cli history you will ever play,
 FIRST YOU NEED TO TYPE YOUR NAME, THEN:		
 		type 'story mode' to play the story mode,	
 		type 'free mode' to play the free mode,
 		type 'clear' to clean the screen,
 		type 'exit' to exit the game. {emojies.SMILE}""")

#user_name
while 86 == 86:
	user_name = input(BLACK + "ENTER YOUR NAME:>> ")
	if user_name == "":
		print(RED + f"""
xxxxxxxxxxxxxxxxxxxxx
ENTER A VALID NAME {emojies.CONFUSED}
xxxxxxxxxxxxxxxxxxxxx
""")	
	elif user_name == " ":
		print(RED + f"""
xxxxxxxxxxxxxxxxxxxxx
ENTER A VALID NAME {emojies.CONFUSED}
xxxxxxxxxxxxxxxxxxxxx
""")
	elif user_name >= 8:
		print(RED + f"""
xxxxxxxxxxxxxxxxxxxxxxx
MAXIMUM 8 CHARACTERS {emojies.CONFUSED}
xxxxxxxxxxxxxxxxxxxxxxx
""")
	else:
		break

#linux_caps_lock_controller
KDSETLED = 0x4B32
SCR_LED  = 0x01
NUM_LED  = 0x02
CAP_LED  = 0x04

try:
	console_fd = os.open('/dev/console', os.O_NOCTTY)
except:
	pass

all_on = SCR_LED | NUM_LED | CAP_LED
all_off = 0

while True:
    try:
    	#caps_lock_on_switch
    	#fcntl.ioctl(console_fd, KDSETLED, all_on)
    	#caps_lock_off_switch
    	fcntl.ioctl(console_fd, KDSETLED, all_off)
    	print("CAPS LOCK IS OFF NOW")
    	break
    except:
    	pass
    	break

#windows_caps_lock_controller
while True:
	try:
		SendKeys.SendKeys("""
{CAPSLOCK}	
	""")
		print("CAPS LOCK IS OFF NOW")
		break
	except:
		pass
		break

#story_and_free_mode
while True:		
	#story_mode
	user_command = input(GREEN + (">>> ").lower())
	if user_command == "story mode":
		print(RED + f"""

welcome to the story mode!
FIRST ENTER YOUR NAME.
SECOND ENTER THE FILE PATH OF THE MUSIC YOU WANT, THEN:
		type 'start' to start the story mode,
		type 'my name' to see the name you entered,
		type 'clear' to clean the screen,
		type 'exit' to exit the story mode 
		type 'off' to turn the music off. {emojies.SMILE}""")		
		while True:	
			story_command = input(CYAN + (">>> ").lower())
			#story_mode_starter
			if story_command == "start":
				music_path_command = input(YELLOW + ("ENTER (.mp3) file PATH(press 'enter' to skip):>> "))
				timer()
				#music_player
				while True:
					try:
						player = pyglet.media.Player()
						source = pyglet.media.load(music_path_command, streaming=False)
						player.queue(source)
						#music_on
						sleep(3)
						player.play()
					except:
						print(RED + "NO SONG OR WRONG PATH")
						break
				#the_story_begin
				print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@
the story is coming soon ...
@@@@@@@@@@@@@@@@@@@@@@@@@@@@					
""")
			#screen_cleaner
			elif story_command == "clear":
				print('\033c')
			#user_name_printer
			elif story_command == "my name":
				print(f"your name is {user_name}" )
			#music_off
			elif story_command == "off":
				try:
					player.pause()
					print(f"music stopped {emojies.SMILE}")
				except:
				print(RED + f"something went wrong, but continue the game {emojies.CONFUSED}")
				pass	
			#free_mode_story_door
			elif story_command == "free mode":
				print(RED + f"EXIT THE STORY MODE FIRST {emojies.CONFUSED}")
			#story_mode_exit
			elif story_command == "exit":
				print(RED + f"ARE YOU SURE?, type 'yes' to confirm {emojies.CONFUSED}")
				exit_command = input(CYAN + (">>> ").lower())	
				#story_moode_exit_assurance	
				if exit_command == "yes":
					print(GREEN + f"thanks, for playing story mode {emojies.SMILE}")
					print(GREEN + f"press 'exit' again to exit the game {emojies.CONFUSED}")
					break
			else:
				print(RED + f"""
******************************************
WRONG COMMAND MAKE SURE CAPS LOCK IS OFF {emojies.STRANGE}
******************************************
""")
	#screen_cleaner
	elif user_command == "clear":
		print('\033c')
	#user_name_printer
	elif user_command == "my name":
		print(BLACK + f"your name is {user_name}")
	#free_mode
	elif user_command == "free mode":
		print(RED + f"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
sorry, it is not avaible yet {emojies.CONFUSED}
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
""")		
	#exit_door
	elif user_command == "exit":
		print(GREEN + f"""
####################
THANKS FOR PLAYING {emojies.SMILE}
####################
""")
		break
	#undefined_commands
	else:
		print(RED + f"""
******************************************
WRONG COMMAND MAKE SURE CAPS LOCK IS OFF {emojies.STRANGE}
******************************************
""")