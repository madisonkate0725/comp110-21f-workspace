"""Twilight Quiz Project."""

from random import randint

__author__: "730331607" 


COWBOY_HAT: str = "\U0001F920"

SPARKLE: str = "\U0001F48E"

LOLZ_FACE: str = "\U0001F92A"

KUNG_FU_SKILLS: str = "\U0001F94A"

FIRE: str = "\U0001F525"

NESSIE: str = "\U0001F995"

ADRENALINE_RUSH: str = "\U0001F3CB"

SPIDER_MONKEY: str = "\U0001F577\U0001F435"

CACTUS: str = "\U0001F335"

OUTRUN: str = "\U0001F3C3"

FIGHT: str = "\U0001F91B"

KILL: str = "\U0001F635"

WOOZY_FACE: str = "\U0001F974"

TOFU: str = "\U0001F961"

BICEP: str = "\U0001F4AA"

DIVORCE: str = "\U0001F494"

HOT: str = "\U00002764"


def greet() -> None:
    """Print a welcome message."""
    name: str = input("What is your name? ")
    global player
    player: str = name
    print(f"{player}, welcome to the Twilight Quiz!")


def total_number_of_points(a: int) -> int:
    """Tally of number of points."""
    return(points)


def main() -> None:
    """Twilight quiz function."""
    greet()
    ready_to_play: int = int(input("Are you ready to play? 1 for Yes and 2 for No: "))
    question_1: int = 0
    question_2: int = 0
    question_3: int = 0
    question_4: int = 0
    question_5: int = 0
    while ready_to_play == 1:
        print("Enter the number of your answer choice: ")
        print("Where is your favoirite place to wallow in your sorrows about your love triangle with a werewolf and vampire?")
        print("1. La Push, Baby")
        print("2. On the ground in the woods")
        print("3. Listening to 'Rosyln' by Bon Iver on repeat")
        print("4. I wallow for no one")
        answer_1: int = int(input("Answer Choice: "))
        question_1 = question_1 + answer_1
        if answer_1 == 4:
            print("Game over! You are obviously not in the Twilight state of mind.")
        else:
            print("What team are you on?")
            print("1. Team Edward")
            print("2. Team Jacob")
            print("3. Team Charlie")
            print("4. Team Nobody: this is stupid")   
            answer_2: int = int(input("Answer Choice: "))
            question_2 = question_2 + answer_2
            if answer_2 == 4:
                print("Game over! You are obviously not in the Twilight state of mind.")
            else:
                print("Enter the number of your answer choice: ")
                print("What would be your special vampire power?")
                print("1. Mind reading")
                print("2. Shielding")
                print("3. Seeing the future")
                print("4. Not being cringy")
                answer_3: int = int(input("Answer Choice: "))
                question_3 = question_3 + answer_3
                if answer_3 == 4:
                    print("Game over! You are obviously not in the Twilight state of mind.")
                else:
                    print("Enter the number of your answer choice: ")
                    print("Who is your favorite non-main-character couple?")
                    print("1. Emmett and Rosalie")
                    print("2. Alice and Jasper")
                    print("3. Esme and Carlisle")
                    print("4. I don't like any of them")
                    answer_4: int = int(input("Answer Choice: "))
                    question_4 = question_4 + answer_4
                    if answer_4 == 4:
                        print("Game over! You are obviously not in the Twilight state of mind.")
                    else:
                        print("Enter the number of your answer choice: ")
                        print("Pick an iconic Twilight song: ")
                        print("1. A Thousand Years")
                        print("2. Turning Page")
                        print("3. Supermassive Black Hole")
                        print("4. All the songs suck")
                        answer_5: int = int(input("Answer Choice: "))
                        question_5 = question_5 + answer_5
                        if answer_5 == 4:
                            print("Game over! You are obviously not in the Twilight state of mind.")
                        else:
                            print("Congradulations, you made it! Your quote is: ")
        global points
        points: int = question_1 + question_2 + question_3 + question_4 + question_5
        if points <= 7:
            quote_number_1: int = randint(1, 3)
            if quote_number_1 == 1:
                print(f"This is the skin of a killer, Bella {SPARKLE}.")
            if quote_number_1 == 2:
                print(f"Where the hell have you been, loca {LOLZ_FACE}?!")
            if quote_number_1 == 3:
                print(f"Don't worry about the bears, Bella. My Kung Fu is strong {KUNG_FU_SKILLS}.")
        else:
            if points <= 10:
                quote_number_2: int = randint(1, 3)
                if quote_number_2 == 1:
                    print(f"Let's face it: I'm hotter than you {FIRE}.")
                if quote_number_2 == 2:
                    print(f"You nicknamed my daughter after the Loch Ness Monster {NESSIE}?!")
                if quote_number_2 == 3:
                    print(f"Um... I had an adrenaline rush. It's very common. You can Google it {ADRENALINE_RUSH}.")
            else:
                if points <= 12:
                    quote_number_3: int = randint(1, 3)
                    if quote_number_3 == 1:
                        print(f"You'd better hold on tight, spider monkey {SPIDER_MONKEY}.")
                    if quote_number_3 == 2:
                        print(f"Aren't people from Arizona supposed to be like, really tan {CACTUS}?")
                    if quote_number_3 == 3: 
                        print(f"Battle Scars {COWBOY_HAT}.")
                else:
                    if points < 13:
                        quote_number_4: int = randint(1, 3)
                        if quote_number_4 == 1:
                            print(f"As if you could outrun me {OUTRUN}. As if you could fight me off {FIGHT}. I was born to kill {KILL}.")
                        if quote_number_4 == 2:
                            print(f"You’re like my own personal brand of heroin {WOOZY_FACE}.")
                        if quote_number_4 == 3:
                            print(f"It's like a human only living on tofu. It keeps you strong, but you're never fully satisfied {TOFU}.")
                    else:
                        quote_number_5: int = randint(1, 3)
                        if quote_number_5 == 1:
                            print(f"Hello, biceps. You know, anabolic steroids are really bad for you {BICEP}.")
                        if quote_number_5 == 2:
                            print(f"I think you'll find the vampire-human divorce rate a little lower {DIVORCE}.")
                        if quote_number_5 == 3:
                            print(f"Dating an older woman. Hot {HOT}.")
        print(f"Your point total was: {total_number_of_points(points)}")
        ready_to_play = int(input("Do you want to play again? 1 for Yes or 2 for No: "))


if __name__ == "__main__":
    main()