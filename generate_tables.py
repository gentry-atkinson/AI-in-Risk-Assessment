# Author: Gentry Atkinson
# Date: 2026-02-26
# Organization: St. Edward's University
# Description: This script generates tables for the AI in Risk Assessment project.

import seaborn as sns
import matplotlib.pyplot as plt

top_six_risk_assessments = {
    'COMPAS' : 36,
    'PSA' : 19,
    'LSI-R' : 11,
    'VPRA' : 8,
    'CPRAT' : 8,
    'PCRA' : 4
}

benefits_of_ai = {
    'Efficiency': 36,
    'Reduction of Bias': 32,
    'Improved Predictions': 26,
    'Transparency': 13,
    'Objectivity' : 17,
    'Individuation' : 7,
    'Reducing Crime' : 8,
    'Reducing Incarceration' : 15,
    'Social or Justice Reform' : 12,
    'Eliminating Cash Bail' : 7
}

benefits_of_ai = dict(sorted(benefits_of_ai.items(), key=lambda item: item[1], reverse=True))

def generate_top_six_ras_pie_chart():
    plt.figure(figsize=(8, 8))
    plt.pie(
        top_six_risk_assessments.values(), 
        labels=top_six_risk_assessments.keys(), 
        autopct='%.0f%%', 
        startangle=90,
        colors=sns.color_palette('Pastel1', n_colors=len(top_six_risk_assessments)),
        wedgeprops={'edgecolor': 'gray'}
    )
    plt.title('Top 6 Risk Assessment Tools Discussed in Studies', pad=20)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.tight_layout()
    plt.savefig('tables/top_six_ras_pie_chart.png')

def generate_benefits_of_ai_bar_chart():
    plt.figure(figsize=(8, 6))
    sns.barplot(x=list(benefits_of_ai.keys()), y=list(benefits_of_ai.values()))
    plt.xticks(rotation=45, ha='right')
    plt.title('Benefits of AI in Risk Assessment', pad=20)
    # plt.xlabel('Benefit')
    # plt.ylabel('Number of Studies Mentioning Benefit')
    # place a numerical value above each bar
    for index, value in enumerate(benefits_of_ai.values()):
        plt.text(index, value + 0.5, str(value), ha='center', va='bottom')
    # set the y-axis range to be slightly higher than the maximum value for better visualization
    plt.ylim(0, max(benefits_of_ai.values()) + 5)
    plt.tight_layout()
    plt.savefig('tables/benefits_of_ai_bar_chart.png')

if __name__ == "__main__":
    sns.set_style("whitegrid")
    sns.set_palette('Greys')
    sns.set_theme(font_scale=1.5) 
    generate_top_six_ras_pie_chart()
    generate_benefits_of_ai_bar_chart()