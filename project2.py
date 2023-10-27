import random



            
            
questions = [
    {
        "question":"Who is the President of Nigeria?",
        "options":["a) Tinubu", "b) Obasanjo", "c) Peter Obi", "d) Obaseki"],
        "correct_ans": "a"     
    },
    {
        "question":"Capital of China?",
        "options":["a) Abuja", "b) Cairo", "c) Hong Kong", "d) Jerusalem"],
        "correct_ans": "c"
    },
    {
        "question":"Who is the President of USA",
        "options":["a) Obasanjo", "b) Putin", "c) Joe Biden", "d) Donald Trump"],
        "correct_ans": "c"
    },
    {
        "question":"Who was the first President of Nigeria",
        "options":["a) Buhari", "b) Gadaffi", "c) Naira Marley", "d) Asikiwe"],
        "correct_ans": "d"
    },
    {
        "question":"What are the primary colors",
        "options":["a) Red, Blue and Green", "b) Red, Green and purple", "c) White, Black and Brown"],
        "correct_ans": "a"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "correct_ans": "b"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["a) Elephant", "b) Giraffe", "c) Blue Whale", "d) Lion"],
        "correct_ans": "c"
    },
    {
        "question": "What is the capital of France?",
        "options": ["a) Paris", "b) London", "c) Berlin", "d) Madrid"],
        "correct_ans": "a"
    },
    {
        "question": "Which country colonised Nigeria?",
        "options": ["a) USA", "b) Great Britain", "c) France", "d) Italy"],
        "correct_ans": "b"         
    }, 
    {
        "question": "Where does the pope stays?",
        "options": ["a) Paris", "b) Las vegas", "c) Berlin", "d) Rome"],
        "correct_ans": "d"        
    }   
]

random_questions = random.sample(questions, 5)

score = 0

for i, x in enumerate(random_questions, start=1):
    print("No.", i, ":", x["question"])
    for y, z in enumerate(x["options"], start=1):
        print(z)
    while True:
        user_choice = input("Enter the letter of your answer (a/b/c/d): ")
        if user_choice in ["a","b","c","d","A","B","C","D"]:
            if user_choice.lower() == x["correct_ans"]:
                score += 1
            break    
        else:
            print("Input a valid option (a/b/c/d) ")
print("You scored", score, "out of 5 questions.")          

