import re

def is_valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if re.search(regex, email):
        return True
    return False

def is_valid_phone(phone):
    regex = '^[0-9]{10}$'
    if re.search(regex, phone):
        return True
    return False

def collect_user_info():
    name = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    
    if not is_valid_email(email):
        print("Invalid email address!")
        return None
    
    if not is_valid_phone(phone):
        print("Invalid phone number! It should be a 10 digit number.")
        return None
    
    return {
        "name": name,
        "lastname": lastname,
        "email": email,
        "phone": phone
    }

def ask_questions():
    questions = [
        {
            'question': 'What is the capital of India?',
            'choices': ['1. Delhi', '2. Bangalore', '3. Kolkata', '4. Gujrat'],
            'correct_answer': 1
        },
        {
            'question': 'What is 2 + 2?',
            'choices': ['1. 3', '2. 4', '3. 5', '4. 6'],
            'correct_answer': 2
        },
        {
            'question': 'Which city is called Silicon City in India?',
            'choices':['1. Belgam', '2. Bangalore', '3. Hyderbad', '4. Pune'],
            'correct_answer': 2
        },
        {
            'question': 'Compared to their body weight, what animal is the strongest?',
            'choices':['1. Dung Beetle','2. Elephant','3. Ant', '4.Cow'],
            'correct_answer':1
        }
        
    ]
    
    answers = []
    correct_answers = 0
    for q in questions:
        print(q['question'])
        for choice in q['choices']:
            print(choice)
        answer = int(input("Enter the number of your answer: "))
        answers.append(answer)
        if answer == q['correct_answer']:
            correct_answers += 1
    
    return answers, correct_answers, len(questions)

def main():
    print("Welcome to the Login System")
    user_info = None
    
    while not user_info:
        user_info = collect_user_info()
    
    print("User information collected successfully.")
    
    print("Now, let's proceed to the quiz.")
    answers, correct_answers, total_questions = ask_questions()
    
    print("Quiz submitted successfully!")
    print("Your answers were:", answers)
    print(f"You got {correct_answers} out of {total_questions} questions correct.")
    score = (correct_answers / total_questions) * 100
    print(f"Your score is: {score:.2f}%")

if __name__ == "__main__":
    main()
