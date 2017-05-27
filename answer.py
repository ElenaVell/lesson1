def get_answer(question):
    answers={'привет':'И тебе привет','как дела?':'лучше всех!','пока':'увидимся'}
    if question not in answers:
        print('Спроси что-то другое')
    else:
        return answers[question]
question=input().lower()
print(get_answer(question))
