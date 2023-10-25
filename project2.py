'''import random
value = input("Press any key to start or type quit to cancel")
while value != quit:
     print("Answer the following questions")
     break
score = 0'''
import random


def questions_list(question, options, correct_ans):
    print(question)
    for i, option in options:
        print(random(f"{i}.{option}"))
    user_answer = str(input("Enter your answer (a/b/c/d): "))
    try:
        if user_answer == correct_ans:
            return score +1
        else:
            return score +0
    except ValueError:
        print("Input the correct value")  
    except TypeError:
        print("Input the right value")
    except:
        print("Unknown Error")             
            
questions = [
    {
        "question":"Who is the President of Nigeria?",
        "options":["a) Tinubu", "b) Obasanjo", "c) Peter Obi", "d) Obaseki"],
        "correct_ans": "a" or "A"     
    },
    {
        "question":"Capital of China?",
        "options":["a) Abuja", "b) Cairo", "c) Hong Kong", "d) Jerusalem"],
        "correct_ans": "c" or "C"
    },
    {
        "question":"Who is the President of USA",
        "options":["a) Obasanjo", "b) Putin", "c) Joe Biden", "d) Donald Trump"],
        "correct_ans": "c" or "C"
    },
    {
        "question":"Who was the first President of Nigeria",
        "options":["a) Buhari", "b) Gadaffi", "c) Naira Marley", "d) Asikiwe"],
        "correct_ans": "d" or "D"
    },
    {
        "question":"What are the primary colors",
        "options":["a) Red, Blue and Green", "b) Red, Green and purple", "c) White, Black and Brown"],
        "correct_ans": "a" or "A"
    }
]
         
#print(questions[1]["question"])
score = 0
#for i, q in questions:
    #print(f"Question {i}:")
    #score += questions_list(q["question"], q["options"], q["correct_ans"])

#print(f"You scored {score} out of {len(questions)} questions.")
#questions()
