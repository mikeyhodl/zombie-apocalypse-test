import random, os
from getkey import getkey, keys
import cursor

def choose(what: list, before: str = "", illegal: list = [], illegalColor: str = "\u001b[31m", currentColor: str = "\u001b[32m"):
	cursor.hide()
	num = 0
	reset = "\u001b[0m"
	while True:
		os.system('clear')
		if before: print(reset + before + "\n")
		current = what[num]
		_ = len(max(what, key = len))+2
		print(reset + "‾"*_)
		for choice in what:
			if choice == current:
				print(currentColor + "> " + choice)
			else:
				print(reset + "  " + choice)
		print(reset + "_"*_)
		inp = getkey()
		if inp in ['w',keys.UP]:
			try:
				num -= 1
			except:
				num = len(what)
		elif inp in ['s',keys.DOWN]:
			try:
				num += 1
			except:
				num = 0
		elif inp == keys.ENTER:
			os.system('clear')
			if before: print(reset + before)
			if current in illegal:
				for choice in what:
					if choice == current:
						print(illegalColor + "> " + choice)
					else:
						print(reset + "  " + choice)
				sleep(1)
			else:
				cursor.show()
				return current
		if num == len(what): num = 0
		elif num == -1: num = len(what) - 1

questions = {
	"Your house is burning down. What do you save?": ['your dog','some food cans','your clothes','your cell phone'],
	"It is night, and you will freeze to death soon. Making too much noise/light will attract the zombies. What do you do?": ['keep moving around','build a tiny fire','build a normal fire','try to wait out the night'],
	"You are cornered in a grocery store with only a knife. A horde is moving in from all sides. What do you do?": ['kill zombies to make a path','try to climb up on the wobbly shelves','shout for help','self.kill'],
	"You see a group of survivors ahead on the road. What do you do?": ['watch them for a while','ignore them','kill them and steal their stuff','try to greet them'],
	"A group of about 6 people take your stuff at gunpoint, then tell you to get in a storage container. What do you do?": ['get in the container','try to reason with them','refuse','try to fight them'],
	"You and 3 other people are down to 1 last can or food. What do you do?": ['share it', 'eat it','give it to them','burn it so there is no argument'],
	"You are given the choice between 4 weapons. What do you take?": ['katana','crossbow','pistol','RPG'],
	"You only have room in your pack for 1 more package of food. What do you take?": ['trail mix','crackers','oreos','raw chicken'],
	"You have some choices on where to set up camp.": ['next to the river','in the mountains','near the ocean','next to the city'],
	"Your camp, with your group of ~20 people, has been overrun by a horde. What do you do?": ['follow your friends','run','try and save the camp','get your stuff from your tent'],
}

while True:
	score = 0
	items = list(questions.items())
	random.shuffle(items)
	questions = {}
	for it, val in items:
		questions[it] = val
	for q in questions:
		this = list(questions[q])
		for l in range(6): random.shuffle(this)
		user = choose(this, before = q)
		that = list(questions[q])
		if user == that[0]: score += 3
		elif user == that[1]: score += 2
		elif user == that[2]: score += 1
		os.system('clear')
	os.system("clear")
	input('The results are in! ')
	os.system("clear")
	print(f'score: {score}')
	#questions: 10
	#max: 30
	if score == 0:
		print('You would be one of the first peopple to die in the apocalypse.\nYou panic at the sight of a zombie and have no survival skills, getting eaten within an hour.\nPathetic.')
	if score in range(1,5):
		print('You would live a few hours in the apocalypse.\nAs the chaos begins, you make a desperate attempt to save your stuff.\nGetting into the car, you get surrounded.\nThey break open the windows and eat you.\nThat must suck.')
	if score in range(5,10):
		print('You would live a few days in the apocalypse.\nAs the chaos begins, you attempt to go to the emergency shelters.\nYou die when they get overcrowded and overrun.\nToo bad.')
	if score in range(10,15):
		print('You would live a month in the apocalypse.\nYou find a camp and manage to survive for a month, but when the camp gets overrun, you get bit.\nSo close, yet so far.')
	if score in range(15,20):
		print('You would live a few months in the apocalypse.\nYour camp moves from place to place before settling at an old school building.\nAfter living there for a month, you accidentally shoot yourself with a crossbow while attempting to load it.\nAt least you tried.')
	if score in range(20,25):
		print('You would live a few years in the apocalypse.\nYour group settles at a town in Tennessee, fortifying it so that it can withstand a horde.\nWhile on a run, you fall through a floor and break your leg, attracting zombies and getting eaten.\nYou will be remembered.')
	if score in range(25,31):
		print('You would live for a really long time in the apocalypse.\nBeing the leader of your group, you settle at a town near the beach, where hardly any hordes pass through.\nYou help build a utopia named Replit.\nAt the age of 79, you pass away in your sleep.\nThere was a statue of you built.')
	input('\nPress enter to take the quiz again ')