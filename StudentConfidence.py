
import seaborn as sns


def class_confidence_chart(surveyResults, classes):
    chart = sns.catplot(
        data=surveyResults[surveyResults['class'].isin(classes)],
        x='confidence',
        order=['Confident','Somewhat confident','Need practice','Need help','Completely lost'],
        kind='count',
        palette=sns.color_palette("hsv"),
        row='class',
        aspect=3,
        height=3,
    )

    # #rotate the axes to make them readable
    for axes in chart.axes.flat:
        axes.set_xticklabels(axes.get_xticklabels(), rotation=90)