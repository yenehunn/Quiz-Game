import random

def load_questions(filename):
#Format a line of file must be: Question|Choice1|Choice2|Choice3|Choice4|CorrectAnswer
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split('|')
            question = {
                'question': data[0],
                'options': data[1:5],
                'answer': int(data[5])
            }
            questions.append(question)
    return questions

def display_question(question):

    print(question['question'])
    for i, option in enumerate(question['options'], start=1):
        print(f"{i}. {option}")

def play_quiz(questions):

    score = 0
    random.shuffle(questions)
    for question in questions:
        display_question(question)
        answer = input("Enter your answer (1-4): ")
        while not answer .isnumeric():
            print("Please enter integer value")
            answer = input("Enter your answer (1-4): ")
        answer = int(answer)    
        if answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")
    return score

def main():
    filename = 'quizs.txt' 
    questions = load_questions(filename)
    print("Welcome to the Multiple Choice Quiz Game!")
    input("Press Enter to start...")
    print()
    score = play_quiz(questions)
    print(f"Quiz complete! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()