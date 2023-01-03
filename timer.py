import time
import datetime

art = """\
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \\
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \\
\_____________________/
"""

def countdown():
	print("\nIl tuo tea sta infondendo...\n")

	total_seconds = tea_time
	while total_seconds > 0:
		timer = datetime.timedelta(seconds = total_seconds)
		print(timer, end="\r")
		time.sleep(1)
		total_seconds -= 1
	print(art, "\nÈ pronto")
	print('\007')	
	tea = int(input("Vuoi fare un Tea:\n1-Nero\n2-Verde\n3-Custom\n\n"))
while tea != 1 or 2 or 3:
	if tea == 1:
		tea_time = 4 * 60
		countdown()
		break
	elif tea == 2:
		tea_time = 120 + 30
		countdown()
		break
	elif tea == 3:
		m = int(input("\nDimmi quanti minuti vuoi aspettare: "))
		s = int(input("\nDimmi quanti secondi vuoi aspettare: "))
		tea_time = m * 60 + s
		countdown()
		break
	else:python3 make simple beep sound linux
		tea = int(input("\n" + "Vuoi fare un Tea:\n1-Nero\n2-Verde\n3-Custom\n\n"))
