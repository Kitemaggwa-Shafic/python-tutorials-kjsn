# 3:57:35
# Buildig a multiple Choice Quiz
# if, loops, classes and objects

# How can you represent the questios, prompts, answer etc
# you need to keep track of answers

# creating a class
class Question:
    def __init__(self, question_prompt, question_answer):
        self.question_prompt = question_prompt
        self.question_answer = question_answer