from random import choice

questions = ["Why is the sky blue?", "Where is the toy?", "Can I have a cookie?"]


question = choice(questions)
answer = input(question).lower()

while answer != "Just because".lower():
    answer = input("Why?: ").strip().lower()

print("Oh....Okay")
