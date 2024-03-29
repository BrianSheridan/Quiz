import sys

def get_questions():
    try:
       with open('questions.txt') as f:
           lines = f.readlines()
    except:
        print('Questions ile not found.')
        sys.exit()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]


questions = get_questions()
score = 0
total = len(questions)
for question, answer in questions:
    guess = input(question)
    if guess == answer:
        score += 1
print('You got %s out of %s questions right' % (score, total))