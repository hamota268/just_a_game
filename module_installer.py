#comments
#!/usr/bin/python3
#© 2019 copyright HAMOTA
#BE CREATIVE

#DISCLAMER
print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++
MAKE SURE YOU HAVE PIP PACKAGE INSTALLER
++++++++++++++++++++++++++++++++++++++++++++++++++++
ON LINUX TYPE:'sudo apt install python-pip'
++++++++++++++++++++++++++++++++++++++++++++++++++++
FROM GAME FOLDER ON WINDOW TYPE:'python get-pip.py'
++++++++++++++++++++++++++++++++++++++++++++++++++++
""")

#modules
import pip

#module_installer
def install(package):
    if getattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
try:
	install('os')
	install('pygame')
	install('time')
	install('curses')
	install('random')
	install('file')
	install('pickle')
	install('schedule')
	install('commands')
	install('SendKeys')
	install('fcntl')
	#done
	print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++
INSTALLER COMPLETED, ENJOY THE THE GAME IF NO ERRORS
++++++++++++++++++++++++++++++++++++++++++++++++++++
	""")
except:
	print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxx
SORRY, SOMETHING WENT WRONG
xxxxxxxxxxxxxxxxxxxxxxxxxxx
""")