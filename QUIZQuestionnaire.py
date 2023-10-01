import time

questions = [
  {
    "question": "Whats always infront of you but cant be seen?",
    "options": ["A. mirror", "B. future", "C. mercury", "D. air"],
    "Correct_answer": "B"
  },
  {
    "question": "Whats the worlds smallest country?",
    "options": ["A. bangladesh", "B. vatican city", "C. morocco", "D. cape verde"],
    "Correct_answer": "B"
  },
  {
    "question": "A word i know that contains six letters,remove one letter and twelve remains?",
    "options": ["A. letters", "B. 12", "C. dozens", "D. a sign"],
    "Correct_answer": "C"
  },
  {
    "question": "I am always hungry and will die if not fed, but whatever i touch turns red?",
    "options": ["A. fire", "B. red paint", "C. flames", "D. fingers"],
    "Correct_answer": "A"
  },
  {
    "question": "what is the dryiest continent on earth?",
    "options": ["A. africa", "B. canada", "C. australia", "D. antarctica"],
    "Correct_answer": "D"
  },
{
    "question": "What is the name of the deepest point in the earths ocean?",
    "options": ["A. cove", "B. mariana's trench", "C. lagoon", "D. cave"],
    "Correct_answer": "B"
  },
  {
    "question": "what famous graffiti artist comes from bristol?",
    "options": ["A. John", "B. Banksy", "C. Joean", "D. Galil"],
    "Correct_answer": "B"
  },
  {
    "question": "when did they open the London underground?",
    "options":  ["A. 1874", "B. 1906", "C. 1863", "D. 1860"],
    "Correct_answer": "C"
  },
  {
    "question": "When was Netflix founded?",
    "options": ["A. 1856", "B. 1999", "C. 1842", "D. 1997"],
    "Correct_answer": "D"
  },
  {
    "question": "What part of the human body get oxygen directly from the air?",
    "options": ["A. eye cornea", "B. earholes", "C. skin pores", "D. bellybutton"], 
    "Correct_answer": "A"
  }, 
]

score = 0
#make timer that loops in the question
def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"TIME: {i} seconds")
        time.sleep(1)

# print out the question and options 
for question in questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    print()

#getting user input
    user_input = input("Answer: ").strip().upper()

    if user_input == question["correct_answers"]:
        score += 1
        print("CORRECT ANSWER!\n")
    else:
        print(f"WRONG ANSWER. Correct answer is {question['correct_answer']}.\n")  

#timer
    countdown_timer(4)
    print()

total_questions = len(questions)

print(f"Scored {score} out of {total_questions } questions.")
percentage_score = (score / total_questions ) * 100
print(f"Percentage score: {percentage_score:2f}%")