def get_students_other_thoughts(surveyResults):
    students_other_thoughts = surveyResults.loc[surveyResults.other_thoughts.str.len() > 0]
    students_thoughts = list(zip(students_other_thoughts.name, students_other_thoughts.other_thoughts))
    return students_thoughts