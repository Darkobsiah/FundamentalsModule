import random
import time

names = ["Stoqn", "Slavi", "Nasko", "Kristiqn", "Slavi Trifanov",
         "Billy", "Krisko", "Rapuncel", "Pesho", "Boyko Borisov",
         "Mariqna", "Teodor", "Atanas", "Viktor", "Grisho Dimitrov",
         "Mike Tyson", "Vladimir Putin", "David Goggins", "The clasher",
         "Will Smith", "Pedro", "Elizabeth"]

places = ["South London", "Aytos", "the ghetto", "school",
          "Pazardjik", "Gabrovo", "Atlantic", "Sofia",
          "Arjentina", "Turkey", "BS KS", "the public house",
          "the area", "the arena", "the beach", "the prison"]

verbs = ["watches", "drinks", "drives", "starts arguing",
         "pissed a", "throws", "kisses", "kick", "punch",
         "takes", "pull up", "spit", "wears"]

nouns = ["stones", "cake", "chair", "toy", "laptop", "bikes", "ball", "mouse",
         "bar", "cat", "car", "building", "hat", "stick", "brick", "beer", "drees",
         "bank", "baseball", "bath", "bedroom", "bird", "book", "bonus", "bus", "business"]

adverbs = ["slowly", "diligently", "warmly", "coldly", "sadly", "slowly", "rapidly", "extremely",
           "angrily", "calmly", "significantly", "lovely", "downstairs", "proudly", "nearby", "soon",
           "cheerfully", "carelessly", "inside", "madly", "deeply", "curiously", "consciously", "later"]

details = ["near the river", "in the part", "at anonymous house", "at school", "in the shelf", "in his thoughts",
           "near the hospital", "down the bridge", "at the strip bar", "under the table", "up to the ceiling"
           "in the DeathZone", "in CS 1.6", "in GTA 5", "in the mountain"]


def random_word(words):
    return random.choice(words)


def start_the_program():
    print("\nHello, the fun now begins!")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    main()


def main():
    while True:
        random_name = random_word(names)
        random_place = random_word(places)
        random_verb = random_word(verbs)
        random_noun = random_word(nouns)
        random_adverb = random_word(adverbs)
        random_detail = random_word(details)
        print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}.")
        answer = input("Click [Enter] to generate a new one. WRITE [End] to end: \n")
        if answer.lower() == 'end':
            print()
            break
    random_noun = random_word(nouns)
    random_verb = random_word(verbs)
    print(f"Thank you for {random_verb} my new {random_noun}, haha.")


start_the_program()




