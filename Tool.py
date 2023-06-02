def question_answer_tool():
    question1 = "ENTER QUESTION"
    correct_answer1 = "ENTER SOLUTION"

    question2 = "ENTER QUESTION"
    correct_answer2 = "ENTER SOLUTION"

    answer1 = input(question1 + " ")
    if answer1.lower() == correct_answer1.lower():
        print("Correct!")
    else:
        print("Wrong! The correct answer is: " + correct_answer1)

    answer2 = input(question2 + " ")
    if answer2.lower() == correct_answer2.lower():
        print("Correct!")
    else:
        print("Wrong! The correct answer is: " + correct_answer2)

question_answer_tool()
