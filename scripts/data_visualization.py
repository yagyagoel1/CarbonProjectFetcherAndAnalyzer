import os
import sys


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))
from logger import logger

def wrap_text(text, max_words=4):
    if isinstance(text, int):  # Ensure the text is a string
        text = str(text)
    words = text.split()
    if len(words) > max_words:
        return '\n'.join([' '.join(words[i:i+max_words]) for i in range(0, len(words), max_words)])
    return text

def visualize_data(credits_by_country, credits_by_project_type, credits_by_year, highest_credit_project, lowest_credit_project,unified_df):
    plt.figure(figsize=(12, 8))
    top_10_df = unified_df.head(150)
    sns.scatterplot(data=top_10_df, x='Vintage', y='Credits Issued', hue='Project Type')# To create a scatter plotplt.title('Credits Issued vs Vintage by Project Type')
    plt.xticks(rotation=45)
    plt.title("Credits Issued vs Vintage by Project Type(Top 150)")
    plt.savefig("public/images/credits_vs_vintage_by_project_type.png")
    plt.clf()  # Clear the figure to avoid overlap

    pivot_table = unified_df.pivot_table(index='Vintage', columns='Country', values='Credits Issued', aggfunc='sum', fill_value=0)

    # Plot stacked bar plot
    pivot_table.plot(kind='bar', stacked=True, figsize=(12, 8))# To create a pivot Table
    plt.title('Credits Issued by Country and Vintage Year')
    plt.ylabel('Credits Issued')
    plt.xticks(rotation=45)
    plt.savefig("public/images/credits_by_country_and_vintage.png")
    plt.clf()  # Clear the figure to avoid overlap
    # Top 10 countries by credits issued and others
    top_countries = credits_by_country.nlargest(10, 'Credits Issued')  # Top 10 countries
    other_countries_sum = credits_by_country['Credits Issued'].sum() - top_countries['Credits Issued'].sum()  # Sum of others
    others_df = pd.DataFrame({'Country': ['Others'], 'Credits Issued': [other_countries_sum]})
    top_countries = pd.concat([top_countries, others_df], ignore_index=True)

    fig, ax = plt.subplots(figsize=(12, 8))
    top_countries.set_index('Country').plot(kind='bar', color='skyblue', ax=ax)
    plt.title('Top 10 Countries by Credits Issued and Others')
    plt.xlabel('Country')
    plt.ylabel('Credits Issued in Billons')
    
    # Add labels to each bar in the top countries chart
    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('public/images/top_10_countries_credits.png')
    plt.clf()  # Clear the figure to avoid overlap
    
    # Total credits issued by project type including others
    top_project_types = credits_by_project_type.nlargest(10, 'Credits Issued')  # Top 10 project types
    other_project_types_sum = credits_by_project_type['Credits Issued'].sum() - top_project_types['Credits Issued'].sum()  # Sum of others
    others_df = pd.DataFrame({'Project Type': ['Others'], 'Credits Issued': [other_project_types_sum]})
    top_project_types = pd.concat([top_project_types, others_df], ignore_index=True)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax2 = top_project_types.set_index('Project Type').sort_values(by='Credits Issued').plot(kind='barh', color='salmon', ax=ax)
    plt.title('Total Credits Issued by Project Type and Others')
    plt.xlabel('Credits Issued')
    plt.ylabel('Project Type')

    # Wrapping text for y-axis labels
    wrapped_labels = [wrap_text(label) for label in top_project_types['Project Type']]
    ax2.set_yticklabels(wrapped_labels)

    # Add labels to each bar in the project type chart
    for p in ax2.patches:
        width = p.get_width()
        ax2.annotate(f'{width:,.0f}', (width + 0.05, p.get_y() + p.get_height() / 2.),
                      ha='left', va='center')

    plt.tight_layout()
    plt.savefig('public/images/credits_by_project_type.png')
    plt.clf()  # Clear the figure to avoid overlap
    
    # Trend in credit issuance over time
    fig, ax = plt.subplots(figsize=(12, 8))
    credits_by_year.plot(x='Vintage', y='Credits Issued', kind='line', marker='o' ,color='red', ax=ax)
    plt.title('Trend in Credit Issuance Over Time')
    plt.xlabel('Year')
    plt.ylabel('Credits Issued')

    plt.tight_layout()
    plt.savefig('public/images/trend_in_credit_issuance.png')
    plt.clf()  # Clear the figure to avoid overlap
    
    # Highest and lowest credit issuance projects
    fig, ax = plt.subplots(figsize=(12, 8))
    data = pd.DataFrame({
        'Project': ['Highest Credit Issuance', 'Lowest Credit Issuance'],
        'Credits': [
            highest_credit_project['Credits Issued'],
            lowest_credit_project['Credits Issued']
        ]
    })
    


    # Plot bar chart
    ax.bar(data['Project'], data['Credits'], color=['violet', 'red'])
    
    # Add annotations
    for i, row in data.iterrows():
        plt.text(i, row['Credits'], f"{row['Credits']}", ha='center')
    
    plt.title('Highest and Lowest Credit Issuance')
    plt.xlabel('Project')
    plt.ylabel('Credits')
    
    plt.tight_layout()
    plt.savefig('public/images/highest_lowest_credit_issuance.png')
    plt.clf()  # Clear the figure to avoid overlap
    
    logger.info("Visualizations created successfully.")
