import sys
import argparse
import numpy as np

# Setting up the argument parser
ap = argparse.ArgumentParser()
# Adding the argument for interactive test enviornment
ap.add_argument("-i", "--interactive", help='interactive testing enviornment', action='store_true')
# Adding the argument for report mode
ap.add_argument("-r", "--report", help='report mode', action='store_true')

# Getting the argument variables
args = vars(ap.parse_args())

def switchFunction(choice): 
	getValues = {
			1: '1',
			2: '2',
			3: '3',
			4: '4',
			5: '5',
			6: '6',
			7: '7',
			8: '8',
			9: 'Exitting'
		}
	print(getValues.get(choice))
	

# Entering the interactive mode
if args['interactive']:
	print('Entering interactive mode')
	# selecting the choice from the menu driven options
	choice = 0
	while(choice != 9):
		print('\n(1) Load Data\n\t-Asset data\n\t-Trade data\n\t-Serialised Data\n(2) Find and display asset\n(3) Find and display trade details\n(4) Find and display potential trade paths\n(5) Set asset filter\n(6) Asset overview\n(7) Trade overview\n(8) Save data (serialised)\n(9) Exit')
		choice = int(input())
		if choice > 9:
			print('\nInvalid choice, please try again')
		else:
			switchFunction(choice)
			

# Entering the report mode
elif args['report']:
	print('Entering report mode')

# Showing the usage information
else:
	ap.print_help(sys.stderr)
	sys.exit(1)

