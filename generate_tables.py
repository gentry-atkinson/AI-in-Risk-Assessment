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

is_ml_used = {
    "Yes" : 40,
    "No" :14
}

ai_tools_used = {
    "Random Forest" : 6,
    "Logistic Regression"	: 6,
    "SVMs" : 3,
    "Gradient Boosting" : 3
}

ai_contributes_to_bias ={
    "Yes" : 42,
    "No" : 12
}

sources_of_bias = {
    "Training Data" : 34,
    "Actions by Developers" : 8,
    "Institutional Bias" : 4,
    "Proxy Variables" : 22,
    "Rationalization of Bias" : 8,
    "Data Size" : 2,
    "Removing Human Judgement" : 4,
    "Definitions of Fairness" : 5,
    "Human Interpretation" : 7,
    "Black Boxes" : 5,
    "Calibration" : 6,
    "Algorithmic Bias" : 2,
}

benefits_of_ai = dict(sorted(benefits_of_ai.items(), key=lambda item: item[1], reverse=True))
sources_of_bias = dict(sorted(sources_of_bias.items(), key=lambda item: item[1], reverse=True))

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

def generte_is_ml_used_pid_chart():
    plt.figure(figsize=(5, 5))
    plt.pie(
        is_ml_used.values(), 
        labels=is_ml_used.keys(), 
        autopct='%.0f%%', 
        startangle=90,
        colors=sns.color_palette('Pastel1', n_colors=len(top_six_risk_assessments)),
        wedgeprops={'edgecolor': 'gray'}
    )
    plt.title('Is ML Used for Risk Assessment', pad=20)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.tight_layout()
    plt.savefig('tables/is_ml_used.png')

def generate_ai_tools_bar_chart():
    plt.figure(figsize=(8, 6))
    sns.barplot(x=list(ai_tools_used.keys()), y=list(ai_tools_used.values()))
    plt.xticks(rotation=45, ha='right')
    plt.title('Count of AI Tools Used in Experiments', pad=20)
    # plt.xlabel('Benefit')
    # plt.ylabel('Number of Studies Mentioning Benefit')
    # place a numerical value above each bar
    for index, value in enumerate(ai_tools_used.values()):
        plt.text(index, value + 0.5, str(value), ha='center', va='bottom')
    # set the y-axis range to be slightly higher than the maximum value for better visualization
    plt.ylim(0, max(ai_tools_used.values()) + 2)
    plt.tight_layout()
    plt.savefig('tables/ai_tools_used_bar_chart.png')

def generate_ai_contributes_to_bias_pie_chart():
    plt.figure(figsize=(5, 5))
    plt.pie(
        ai_contributes_to_bias.values(), 
        labels=ai_contributes_to_bias.keys(), 
        autopct='%.0f%%', 
        startangle=90,
        colors=sns.color_palette('Pastel1', n_colors=len(ai_contributes_to_bias)),
        wedgeprops={'edgecolor': 'gray'}
    )
    plt.title('ARA Contributes to Bias', pad=20)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.tight_layout()
    plt.savefig('tables/ara_contributes_to_bias.png')

def generate_sources_of_bias_bar_chart():
    plt.figure(figsize=(8, 6))
    sns.barplot(x=list(sources_of_bias.keys()), y=list(sources_of_bias.values()))
    plt.xticks(rotation=45, ha='right')
    plt.title('Sources of Bias in AI Risk Assessment', pad=20)
    # plt.xlabel('Benefit')
    # plt.ylabel('Number of Studies Mentioning Benefit')
    # place a numerical value above each bar
    for index, value in enumerate(sources_of_bias.values()):
        plt.text(index, value + 0.5, str(value), ha='center', va='bottom')
    # set the y-axis range to be slightly higher than the maximum value for better visualization
    plt.ylim(0, max(sources_of_bias.values()) + 2)
    plt.tight_layout()
    plt.savefig('tables/sources_of_bias_bar_chart.png')

if __name__ == "__main__":
    sns.set_style("whitegrid")
    sns.set_palette('Greys')
    sns.set_theme(font_scale=1.5) 
    generate_top_six_ras_pie_chart()
    generate_benefits_of_ai_bar_chart()
    generte_is_ml_used_pid_chart()
    generate_ai_tools_bar_chart()
    generate_ai_contributes_to_bias_pie_chart()
    generate_sources_of_bias_bar_chart()