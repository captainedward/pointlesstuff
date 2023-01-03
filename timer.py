import time
import datetime
# The following bytes object consists of 160 signed 8-bit samples,
# which are base64 encoded, When played at 8000 Hz, it results in a
# tone of 400 Hz. The duration of the sound is 0.02 Hz, so it should
# be looped 50 times per second for longer sounds.
base64_encoded_sound_data = b'''
gKfK5vj/+ObKp39YNRkHAQcZNViAp8rm+P/45sqngFg1GQcBBxk1WI
Cnyub4//jmyqeAWDUZBwEHGTVYf6fK5vj/+ObKp39YNRkHAQcZNViA
p8rm+P/45sqngFg1GQcBBxk1WH+nyub4//jmyqd/WDUZBwEHGTVYf6
fK5vj/+ObKp39YNRkHAQcZNViAp8rm+P/45sqnf1g1GQcBBxk1WA==
'''

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
	else:
		tea = int(input("\n" + "Vuoi fare un Tea:\n1-Nero\n2-Verde\n3-Custom\n\n"))
