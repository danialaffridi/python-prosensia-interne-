def get_questions():
    return [
        {"question": "who win the cricket world cup in 1992 ?", "answer": "PAKISTAN"},
        {"question": "Who is the real pm of pakistan ?", "answer": "IMRAN KHAN"},
        {"question": "Who is destroying pakistan ?", "answer": "PAK ARMY"},
        {"question": "What is the trending meme sound ?", "answer": "CHIN TAPAK DAM DAM"}
    ]

def ask_question(question_data):
    question = question_data["question"]
    correct_answer = question_data["answer"]
    user_answer = input(question + " ").strip()
    
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        return False

def main():
    questions = get_questions()
    score = 0
    
    for q in questions:
        if ask_question(q):
            score += 1
    
    print(f"Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    main()
