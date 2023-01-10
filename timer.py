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
	print("\nYour leaves are infusing...\n")

	total_seconds = tea_time
	while total_seconds > 0:
		timer = datetime.timedelta(seconds = total_seconds)
		print(timer, end="\r")
		time.sleep(1)
		total_seconds -= 1
	print(art, "\nYour Tea is ready!")
#remove this line if you don't want it to make any sound
	print('\007')	
tea = int(input("\nYou want to drink a:\n1-Black Tea\n2-Green Tea\n3-Custom\n\n"))
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
		m = int(input("\nHow many minutes: "))
		s = int(input("\nHow many seconds: "))
		tea_time = m * 60 + s
		countdown()
		break
	else:
		tea = int(input("\nYou want to drink a:\n1-Black Tea\n2-Green Tea\n3-Custom\n\n"))
