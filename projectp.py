score = 0
def main_page():
    global score
    print("Who is the President of Nigeria?\na) Tinubu", "b) Obasanjo", "c) Peter Obi", "d) Obaseki")
    user_ans = str(input("Enter your answer a/b/c/d: "))
    correct_ans = "a"
    correct_ans_1 = "A"
    
    if user_ans == correct_ans or user_ans ==  correct_ans_1: score += 1
    else: score += 0         

main_page()
print("You scored ",score)

