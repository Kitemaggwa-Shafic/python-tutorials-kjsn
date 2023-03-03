from questions import Question

question_prompt =[
    "What color are apples?\n(a) Red/Green\n(b) Yellow\n(c) Orange\n\n",
    "What color are berries?\n(a) Yellow\n(b) Purple\n(c) Limegreen\n\n",
    "What color are mangoes?\n(a) Green\n(b)Mangeta \n(c)Yellow/Green\n\n"
]
 
questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "c")
 ]

# write a function to ask user

def run_test(questions):
    # loopingthrogh @ question and check ans
    score = 0
    for question in questions:
        question_answer = input(question.question_prompt)
        # checking answer
        if question_answer == question.question_answer:
            score =+ 1
            # 
    print("You got " + str(score) + " / "  + str(len(questions)) + " Questions correct")        
run_test(questions)
