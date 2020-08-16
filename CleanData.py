#cleaning up some of the data to make it easier to read and use
column_names = {'Timestamp': 'timestamp',
                'Select Class': 'class',
                'How do you feel about the material covered this week?': 'confidence',
                'Did the extra resources help this week?': 'extra_resources',
                "Were Mr. Smith's extra videos helpful this week?": 'smith_videos',
                'How many hours did you spend studying or doing work on your own this week? (For all classes, not just this one)': 'hours_studying',
                'How has your overall course load been this week?': 'courseload',
                'How has your life outside of classwork been? (Select all that apply)': 'outside_life',
                'Is there anything else on your mind, school or home life?': 'other_thoughts',
                'Would you like to set up a time to meet one on one during office hours?': 'set_meeting',
                'What date and time works best for you? (I will send an email confirming the time, or showing my availability if there is a conflict.)': 'meeting_time',
                'Name (Last, First) Please enter it the same way every time, including capitalization.': 'name'
                }

def change_column_names(surveyResults):
    surveyResults.rename(columns=column_names, inplace=True)
    surveyResults['confidence'] = surveyResults['confidence'].replace(['Somewhat confident - just need some time','Neutral - need more practice','Not confident - need some help', 'Completely lost - what kind of math is this?!'], ['Somewhat confident','Need practice', 'Need help', 'Completely lost'])
    surveyResults['hours_studying'] = surveyResults['hours_studying'].replace(['0-1', '1-5', '5-10', '10+'], [0, 1, 5, 10])