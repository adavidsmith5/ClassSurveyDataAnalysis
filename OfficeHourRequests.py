def get_office_hour_requests(surveyResults):
    student_results = surveyResults.loc[surveyResults['set_meeting'] == 'Yes']
    meeting_requests = list(zip(student_results.name, student_results.meeting_time))
    return meeting_requests