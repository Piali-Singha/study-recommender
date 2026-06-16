questions = [
    {"question": "Which is NOT a data type?", "options":["bol","float","loop"], "answer":"loop","prize":"1000"},
    {"question": "what does len(hi) return?","options":["1","2", "3"], "answer": "2","prize":"2000"},
    {"question": "what keyword defines function?", "options":["def","func","fun"],"answer":"def","prize":"3000"},

]
prize_won = 0

for i, q in enumerate(questions):

    print(f"\nQuestion {i+1}: {q['question']}")
    for j, option in enumerate(q['options']):
        print(f"{j+1}. {option}")

    user_answer = input("your answer:").strip()

    if user_answer == q['answer']:
        prize_won = q['prize']
        print(f"Correct! prize so far: Rs:{prize_won}")
    else:
        print(f"Wrong! Correct answer was: {q['answer']}") 
        break

    print(f"\nYou are taking home Rs.{prize_won}")  

