platform = input("Where do you play? FIDE, Chess.com or Lichess? ")

if platform.lower() == "fide":
    print("FIDE rating selected!")
elif platform.lower() == "chess.com":
    print("Chess.com rating selected!")
elif platform.lower() == "lichess":
    print("Lichess rating selected!")
else:
    print("Unknown platform!")

while platform.lower().strip() not in ["fide", "chess.com", "lichess"]:
    print("Unknown platform!")
    platform = input("Try again: ")

print("Good job!")

if platform.lower() == "fide":
    rating = int(input("What is your fide rating?"))

    while rating < 1000:
        print("It can't be negative!/smaller than 1000!")
        rating = int(input("Try again: "))

    print("Good job!")

    if 1800 <= rating <= 2500:
        print("Strong player!")
    elif rating > 2500:
        print("Amazing player!!!")
    else:
        print("Not bad buddy!")
    for i in range(1):
        print("Keep practicing!")

if platform.lower() == "chess.com":
    rating = int(input("What is your chess.com rating?"))

    while rating < 0:
        print("It can't be negative!!")
        rating = int(input("Try again: "))

    print("Good job!")

    if 1500 <= rating <= 2600:
        print("Strong player!")
    elif rating > 2600:
        print("Amazing player!!!")
    else:
        print("Not bad buddy!")
    for i in range(1):
        print("Keep practicing!")

if platform.lower() == "lichess":
    rating = int(input("What is your lichess rating?"))

    while rating < 0:
        print("It can't be negative!!")
        rating = int(input("Try again: "))

    print("Good job!")

    if 1500 <= rating <= 2000:
        print("Strong player!")
    elif rating > 2000:
        print("Amazing player!!!")
    else:
        print("Not bad buddy!")
    for i in range(1):
        print("Keep practicing!")

time = input("What is your favorite time control(Rapid, Blitz, Bullet or Hyperbullet)? ")

if time.lower() == "rapid":
    print("Rapid time control selected!")
elif time.lower() == "blitz":
    print("Blitz time control selected!")
elif time.lower() == "bullet":
    print("Bullet time control selected!")
elif time.lower() == "hyperbullet":
    print("Hyperbullet time control selected!")
else:
    print("Unknown time control!")

while time.lower().strip() not in ["rapid", "blitz", "bullet", "hyperbullet"]:
    time = input("Try again: ")

print("Good job!")

if time.lower() == "rapid":
    control = input("Choose your rapid control (10+0, 10+5, 15+10 or 30+0): ")

    if control == "10+0":
        print("Awesome!")
    elif control == "10+5":
        print("Awesome!")
    elif control == "15+10":
        print("Awesome!")
    elif control == "30+0":
        print("Awesome!")
    else:
        print("Unknown time control!")

    while control not in ["10+0", "10+5", "15+10", "30+0"]:
        control = input("Try again: ")

    print("Good job!")

if time.lower() == "blitz":
    control = input("Choose your blitz control (3+0, 3+2, 5+0, 5+3 or 5+5): ")

    if control == "3+0":
        print("Awesome!")
    elif control == "3+2":
        print("Awesome!")
    elif control == "5+0":
        print("Awesome!")
    elif control == "5+3":
        print("Awesome!")
    elif control == "5+5":
        print("Awesome!")
    else:
        print("Unknown time control!")

    while control not in ["3+0", "3+2", "5+0", "5+3", "5+5"]:
        control = input("Try again: ")

    print("Good job!")

if time.lower() == "bullet":
    control = input("Choose your bullet control (1+0, 1+1, 2+0, 2+1 or 2+2): ")

    if control == "1+0":
        print("Awesome!")
    elif control == "1+1":
        print("Awesome!")
    elif control == "2+0":
        print("Awesome!")
    elif control == "2+1":
        print("Awesome!")
    elif control == "2+2":
        print("Awesome!")
    else:
        print("Unknown time control!")

    while control not in ["1+0", "1+1", "2+0", "2+1", "2+2"]:
        control = input("Try again: ")

    print("Good job!")

if time.lower() == "hyperbullet":
    control = input("Choose your hyperbullet control (0.5+0 or 0.5+1): ")

    if control == "0.5+0":
        print("Awesome!")
    elif control == "0.5+1":
        print("Awesome!")
    else:
        print("Unknown time control!")

    while control not in ["0.5+0", "0.5+1"]:
        control = input("Try again: ")

    print("Good job!")

tactic = int(input("How many minutes did you study tactics every day?"))

while tactic < 0:
    print("The tactic is negative!")
    tactic = int(input("Try again: "))

print("Good job!")

if 60 <= tactic <= 90:
    print("Awesome!")
elif tactic > 90:
    print("Too much, isn't it?")
elif tactic < 0:
    print("It's can't be negative!")
else:
     print("Not enough!")
     for i in range(1):
        print("Keep practicing!")

opening = int(input("How many minutes did you study opening every day?"))

while opening < 0:
    print("The opening is negative!")
    opening = int(input("Try again: "))

print("Good job!")
if 60 <= opening <= 90:
    print("Awesome!")
elif opening > 90:
    print("Too much, isn't it?")
elif opening <0:
    print("It's can't be negative!")
else:
    print("Not Enough")
    for i in range(1):
        print("Keep practicing!")

middlegame = int(input("How many minutes did you study middlegame every day?"))

while middlegame < 0:
    print("The middlegame is negative!")
    middlegame = int(input("Try again: "))

print("Good job!")
if 60 <= middlegame <= 90:
    print("Awesome!")
elif middlegame > 90:
    print("Too much, isn't it?")
elif middlegame <0:
    print("It's can't be negative!")
else:
    print("Not Enough")
    for i in range(1):
        print("Keep practicing!")

endgame = int(input("How many minutes did you study endgame every day?"))

while endgame < 0:
    print("The endgame is negative!")
    endgame = int(input("Try again: "))

print("Good job!")
if 60 <= endgame <= 90:
    print("Awesome!")
elif endgame > 90:
    print("Too much, isn't it?")
elif endgame <0:
    print("It's can't be negative!")
else:
    print("Not Enough")
    for i in range(1):
        print("Keep practicing!")

puzzles = int(input("How many did you solve puzzles every day?"))

while puzzles < 0:
    print("The puzzles is negative!")
    puzzles = int(input("Try again: "))

print("Good job!")
if 20 <= puzzles <= 50:
    print("Awesome!")
elif puzzles > 50:
    print("Too much, isn't it?")
elif puzzles <0:
    print("It's can't be negative!")
else:
    print("Not Enough")
    for i in range(1):
        print("Keep practicing!")

study_time = tactic + opening + middlegame + endgame
print(study_time)

if 240 <= study_time <= 300:
    print("Super!")
elif study_time > 300:
    print("Too much, isn't it?")
elif study_time < 0:
    print("study time can't be negative!")
else:
    print("Not enough!")

player_preferences = platform, control
print(player_preferences)

player = platform, rating, control, tactic, opening, middlegame, endgame, puzzles, study_time
print(player)