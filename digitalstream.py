""" A screensaver in the style of The Matrix Movies visuals from Al Sweigarts fantastic The big book of Small Python Projects"""

import random, shutil, sys, time

#Set constants
MIN_STREAM_LENGTH = 4  # Can be changed from 1-50
MAX_STREAM_LENGTH = 15 # Try changing to 100
PAUSE = 0.1 # Try changing to 0.0 or 2.0
STREAM_CHARS = ['0', '1'] # Try changing to other characters

# Density can range from 0.0 to 1.0:
DENSITY = 0.02 # Try changing to 0.10 or 0.30

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]

#To prevent windows from adding a newline automatically, prevent program from printing to last column
WIDTH -= 1

print('Digital Stream')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    # For each column, when the counter is 0, no stream is shown
    # Otherwise, it acts as a counter for how many times a 1 or 0 should be displayed in that column
    columns = [0] * WIDTH
    while True:
        # Set the counter for each column:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    #Restart stream on this column.
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
                
                # Display an empty space or a 1/0 character.
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print() # Print a newline at the end of the row of columns.
        sys.stdout.flush() # Make sure text appears on the screen
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program            
