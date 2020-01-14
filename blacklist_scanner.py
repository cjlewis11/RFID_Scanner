import sys
from graphics import *


def load_blacklist():
	fo = open("blacklist.txt","r")
	names = fo.readlines()
	for ii in range(0,len(names)):
		names[ii] = names[ii].rstrip('\n')
	fo.close()
	return names

def check_blacklist(bl, name):
	for ii in range (0,len(bl)):
		if(name == bl[ii]):
			return False
	return True

def party_blacklist():
	win = GraphWin('Face', 600, 300) # give title and dimensions
	blacklist = load_blacklist()
	guests = open("guest_list.txt","a+")

	print("********************BLACK LIST SCANNER ******************")
	print("Hello, please swipe the guest's card as they come in.")
	print("This program will inform you if the guest is Blacklisted.")
	print("Please ensure that the swipe is valid and goes through.")
	print("*********************************************************\n")

	while(True):
		print("If you would like to quit, please type \"end\"")
		print("Please enter the person's name if they have no BuffOne type \"no\", then their name.")
		print("Remember: Green is Good, Yellow means again, Red means Blacklisted")
		text = input("Please swipe the card: ")
		validName = False

		if(text == "end"):
			return
		if(text.startswith(';') or "%E?" in text):
			win.setBackground('yellow')
			print("Please reswipe the card! \n\n ")
		if("=" in text and '/' in text):
				sections = text.split('=')
				for item in sections:
					if ('/' in item):
						name = item.replace('/',' ')
						name = name.lower()
						print(name)
						validName = True

		if(text == "no"):
			text = input("Please enter the name as (first last): ")
			name = text.lower()
			validName = True
		if(validName):
			if(check_blacklist(blacklist,name)):
				guests.write(name+"\n")
				print("\n Clear to Enter \n")
				win.setBackground('green')
			else:
				print("\n**********************************")
				print("*   This person is Blacklisted   *")
				print("**********************************\n")
				#win = GraphWin('Face', 600, 300) # give title and dimensions
				win.setBackground('red')
				message = Text(Point(win.getWidth()/2, 20), 'This person is Blacklisted! Swipe next card to continue.')

	message = Text(Point(win.getWidth()/2, 20), 'Please click anywhere to exit')
	win.getMouse()
	win.close()

def main():
	party_blacklist()

if __name__ == "__main__":
	main()
