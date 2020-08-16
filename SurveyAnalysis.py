from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import CleanData
import StudentConfidence
import OfficeHourRequests
import ConfidenceAndExtraResources
import ConfidenceAndSmithVideos
import StudentStudyHoursOverTime
import OfficeHourRequests
import AnythingElse

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('ClassSurveyCredentials.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Class Survey 2020 (Responses)').sheet1

surveyResults = pd.DataFrame(sheet.get_all_records())

#Cleaning data to make it easier to read
CleanData.change_column_names(surveyResults)


################################################################################

#Getting charts for student confidence
classes = ["2A Integrated Math 3", "3-5AIntegrated Math 3", "6-8A Integrated Math 3", "9A Integrated Math 3", "10A Algebra 3/Trigonometry"]
#StudentConfidence.class_confidence_chart(surveyResults, classes)


################################################################################

#Aggregating data for students requesting office hours
#students_requesting_office_hours = surveyResults['set_meeting'] == 'Yes'
#print(surveyResults[students_requesting_office_hours]['name'] + " " + surveyResults[students_requesting_office_hours]['meeting_time'])


################################################################################

#Getting chart for comparing student confidence to watching extra videos and resources
#ConfidenceAndExtraResources.confidence_and_extra_resources_chart(surveyResults)


################################################################################

#Getting chart for comparing student confidence to watching videos by the teacher
#ConfidenceAndSmithVideos.confidence_and_smith_videos_chart(surveyResults)


################################################################################

#Getting chart for a specific student and their study hours over time
#StudentStudyHoursOverTime.student_study_hours_over_time(surveyResults, "Smith, Krista")


################################################################################

#Getting list of students requesting office hour meeting. The return is a list of tuples
#office_hour_requests = OfficeHourRequests.get_office_hour_requests(surveyResults)

################################################################################

#Getting short answers to anything else on the students' minds. Returns a list of tuples
#that contains the name of the student and their response.
#students_other_thoughts = AnythingElse.get_students_other_thoughts(surveyResults)


plt.show()