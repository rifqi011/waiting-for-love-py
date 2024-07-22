import sys
from time import sleep

def printLyrics(): 
    lines = [
        ("Monday left me broken", 0.12),
        ("Tuesday i was through with hoping", 0.12),
        ("Wednesday my empty arms were open", 0.1),
        ("Thrusday waiting for love", 0.08),
        ("Waiting for love", 0.06)
    ]
    delays = [0.2, .1, .1, .2, 3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char,end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')

printLyrics()