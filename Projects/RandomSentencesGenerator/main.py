import random
import time

names = ["Stoqn", "Slavi", "Nasko", "Kristiqn",
         "Billy", "Krisko", "Rapuncel", "Pesho",
         "Mariqna", "Teodor", "Atanas", "Viktor"]

places = ["South London", "Aytos", "the ghetto", "school",

          "Pazardjik", "Gabrovo", "Atlantic", "Sofia",
          "Arjentina", "Turkey", "BS KS"]

verbs = ["watches", "drinks", "drives", "starts arguing",
         "pissed a", "throws", "kisses", "kick", "punch",
         "takes", "do", "pull up", "spit", "wears"]

nouns = ["stones", "cake", "chair", "toy", "laptop", "bikes", "shower", "mouse",
         "bar", "cat", "car", "building", "hat", "stick", "brick", "beer", "drees"]

adverbs = ["slowly", "diligently", "warmly", "coldly", "sadly", "slowly", "rapidly", "extremely",
           "angrily", "calmly", "significantly", "lovely"]

details = ["near the river", "in the part", "at anonymous house", "at school", "in the shelf", "in his thoughts",
           "near the hospital", "down the bridge", "at the strip bar", "under the table", "up to the ceiling"
           "in the DeathZone", "in CS 1.6", "in GTA 5", "in the mountain"]


def random_word(words):
    return random.choice(words)


print("Hello, the fun now begins!")
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

counter = 0
while True:
    random_name = random_word(names)
    random_place = random_word(places)
    random_verb = random_word(verbs)
    random_noun = random_word(nouns)
    random_adverb = random_word(adverbs)
    random_detail = random_word(details)
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.")
    input("Click [Enter] to generate a new one.")
    counter += 1
    if counter % 3 == 0:
        answer = input("Write 'End' if you want the program to stop: ")
        if answer.lower() == "end":
            break

print("Thank you for using my new FunGenerator, haha")

