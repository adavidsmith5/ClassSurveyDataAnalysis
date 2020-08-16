import seaborn as sns

def confidence_and_extra_resources_chart(surveyResults):
    chart = sns.catplot("confidence", hue="extra_resources", data=surveyResults, kind="count",         order=['Confident','Somewhat confident','Need practice','Need help','Completely lost'], hue_order=['Yes', 'No', "Didn't use them"],palette="Paired")
    for axes in chart.axes.flat:
            axes.set_xticklabels(axes.get_xticklabels(), rotation=90)    