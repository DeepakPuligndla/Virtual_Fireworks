import sys
from fireCracker import start_fireworks

if __name__ == "__main__":
	print ("Hello! Welcome to fesival of firecrackers....")
	number_of_crackers = int(raw_input("Enter how many crackers you want to fire at once (limit:7): "))
	while number_of_crackers > 7:
		number_of_crackers = int(raw_input("Stupid! I told you limit is 7. Why are you entering above it. Enter Correctly.: "))
	print "So... You want", number_of_crackers, "at a time! Interesting.  Here we go...."
	firecrackers = start_fireworks(number_of_crackers)
		