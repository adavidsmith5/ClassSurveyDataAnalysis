import seaborn as sns
import matplotlib.pyplot as plt

def student_study_hours_over_time(surveyResults, student_name):
    student_results = surveyResults.loc[surveyResults['name'] == student_name]
    fig, ax = plt.subplots()
    sns.scatterplot(data=student_results, x='timestamp', y='hours_studying')
    fig.autofmt_xdate()