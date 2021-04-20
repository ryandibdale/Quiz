# opens a local csv file and pulls data based on user input

import csv
import random

quiz_data = open('quiz_sheet .csv',encoding='utf-8')
csv_data = csv.reader(quiz_data)
data_lines = list(csv_data)

for line in data_lines[:5]:
    print(line)

def welcome():
    print(
        "Welcome to the quiz!\nPress 1 for General Knowledge\nPress 2 for Music\nPress 3 for Sports\nPress 4 for TV\nPress 5 for Film\nPress 6 for Disney")

def select_catagory():
    while True:
        try:
            answer = int(input('Choose your category'))
        except:
            print('Choose a number between 1 and 6')
        else:
            break
    return answer

def generate_quiz(selection):
    all_questions = []

    if selection == 1:
        for lines in data_lines:
            if lines[0] == 'General':
                all_questions.append(lines)

    if selection == 2:
        for lines in data_lines:
            if lines[0] == 'Music':
                all_questions.append(lines)

    if selection == 3:
        for lines in data_lines:
            if lines[0] == 'Sports':
                all_questions.append(lines)

    if selection == 4:
        for lines in data_lines:
            if lines[0] == 'TV':
                all_questions.append(lines)

    if selection == 5:
        for lines in data_lines:
            if lines[0] == 'Film':
                all_questions.append(lines)

    if selection == 6:
        for lines in data_lines:
            if lines[0] == 'Disney':
                all_questions.append(lines)

    question_index = random.sample(range(len(all_questions)), 10)

    final_questions = []

    for index in question_index:
        final_questions.append(all_questions[index])

    return final_questions


def present_questions(q_list):
    correct = 0

    for items in q_list:
        print(items[1])
        input('Answer')
        print(items[2])
        answer = input('Did you get it right?')
        if answer == 'y':
            correct += 1
        else:
            pass

    print(f'Congratulations! Your score is {correct}')

if __name__ == '__main__':

    welcome()
    present_questions(generate_quiz(select_catagory()))
