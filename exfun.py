#def house():
#	return """
#	  /\\ 
#	 |  |
#	 |__|
#	 """

#print house()


#def triangle(s):
#	x = s 
#	print x * 5
#	print " " + x * 3
#	print "  " + x
#triangle("s")


#def days_in_month(month):
#	if (month == "February"):
#		print '28'
#	elif (month == "April" or month == "June" or month == "September" or month == "November"):
#		print '30'
#	else:
#		print '31'

#month = raw_input("How many days are in your favorite month? \n > ")
#days_in_month(month)

#def is_leap_year(yr):
#	return(yr % 4 == 0 and not yr % 100 == 0) or yr % 400 == 0
#print is_leap_year(1999)

from random import choice

print "Hi, I'm Jimmy 3000.56 the computer. Let's play Rock-Paper-Scissors!"
game = raw_input("Make your move (r, p, s): ")

def play(game, c, h):
	x = choice("rps")
	if x == game:
		print "I played", x
		print "It's a tie!"
	if x == "r" and game == "p":
		print "I played Rock!"
		print "Awww! I lost!"
		h += 1
	if x == "r" and game == "s":
		print "I played Rock!"
		print "Boi! I won!"
		c += 1
	if x == "p" and game == "s":
		print "I played Paper!"
		print "Awww! I lost!"
		h += 1
	if x == "p" and game == "r":
		print "I played Paper!"
		print "Boi! I won!"
		c += 1
	if x == "s" and game == "p":
		print "I played Scissors!"
		print "Boi! I won!"
		c += 1
	if x == "s" and game == "r":
		print "I played Scissors!"
		print "Awww! I lost!"
		h += 1
	print str(c) + ":" + str(h)
	return c, h
c = 0
h = 0
while not game == "q":
	c, h = play(game, c, h)
	game = raw_input("Make your move (r, p, s): " + "Or 'q' for quit: ")

