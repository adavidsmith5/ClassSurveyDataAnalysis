import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
from datetime import datetime

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('ClassSurveyCredentials.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Class Survey 2020 (Responses)').sheet1

timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
courses = ['2A Integrated Math 3', '3-5AIntegrated Math 3', '6-8A Integrated Math 3', '9A Integrated Math 3', '10A Algebra 3/Trigonometry']
feel_about_subject = ['Confident', 'Somewhat confident - just need some time', 'Neutral - need more practice', 'Not confident - need some help', 'Completely lost - what kind of math is this?!']
extra_resources = ['Yes', 'No', "Didn't use them"]
smith_videos = ['Yes', 'No', "Didn't watch them"]
hours_of_study = ['0-1', '1-5', '5-10', '10+']
overall_course_load = ['Good', "Too much - feeling overwhelmed", "Too little - too easy, could complete in 10 minutes"]
outside_life_responses = ["Everything's fine", "Lots of work", "Busy at home", "Bored", "Missing friends", "Wish we could be at school", "I like working more at my own pace", "I feel less anxiety with nobody else around while I'm working"]
anything_to_tell = ['', "School is coming back!", "I'm miserable", "I need to get out of my house", "I need help in all of my classes.", "They trample everything in their path"]
set_up_office_hours = ['No', 'Yes']
office_hours_times = ['', '8/17 4pm', '8/20 8am', '8/21 3pm', '8/22 1am']
names = ['C, A', 'Smith, Anthony', 'Smith, Krista', 'Fake, Fake', 'Conzett, Graham', 'Pollack, Jackson', 'Frampton, Peter', 'Potter, Harry', 'Johnson, Luke', 'December, Annotated', 'Lloyd, Carly', 'Sandals, Lisa', 'Long, Flights', 'B, A', 'C, A', 'D, A', 'C, D', 'E, F', 'G, H', 'O, H', 'E, T', 'Q, R', 'P, S', 'V, B', 'C, S', 'J, K', 'X, Y', 'Z, A', 'Q, R', 'P, O', 'Y, O']

def outside_life(choices):
    outside_life_answers = ""
    number_of_selections = random.randint(1,8)
    if number_of_selections == 8:
        return ", ".join(choices)
    else:
        for i in range(number_of_selections):
            choice = random.randint(0, len(choices) - 1)
            if (i == 0):
                outside_life_answers = choices[choice]
            else:
                outside_life_answers += ", " + choices[choice]
            choices.pop(choice)
    
    return outside_life_answers


for i in range(260, 300):
    row = [timestamp, courses[random.randint(0,4)], feel_about_subject[random.randint(0,4)], extra_resources[random.randint(0,2)], smith_videos[random.randint(0,2)], hours_of_study[random.randint(0,3)], overall_course_load[random.randint(0,2)], outside_life(outside_life_responses[:]), anything_to_tell[random.randint(0,5)], set_up_office_hours[random.randint(0,1)], office_hours_times[random.randint(0,4)], names[random.randint(0,30)]]
    sheet.insert_row(row, i)

