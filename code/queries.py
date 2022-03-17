"""Module for the 'use panda to perform various queries' task."""

import pandas as pd
import matplotlib.pyplot as plt

def get_condition_by_column(df, condition, column):
    """Takes in a dataframe, condition, and a column name and returns the number of entries that satisfies the condition and separate them by the value of their column.
        Returns a list of pairs of the value of the given column and the number of entries for matching that value."""
    df_filtered = df.loc[condition]
    
    results = []
    for i in df[column].unique():
        num_of_entries = str(len(df_filtered[ df_filtered[column] == i ]))
        results.append((i, num_of_entries))
    
    return results

def fulfill(df, condition):
    """Get entries that fulfill the given condition."""
    df_filtered = df.loc[condition];
    return df_filtered

def print_pie(title, pairs, dictionary=None):
    """Takes a title, a list of pairs of labels and count, and generates a pie chart from the pairs. Optional: a dictionary to translate the census variables into English text."""
    ax = [count for (label, count) in pairs]
    if dictionary == None:
        labels = [str(label) + " (" + count + ")" for (label, count) in pairs]
    else:
        labels = [dictionary[label] + " (" + count + ")" for (label, count) in pairs]
    plt.pie(ax, labels=labels)
    plt.title(title)
    plt.show()

def print_bars(title, pairs, dictionary=None, y_label = "Records"):
    """Takes a title, a list of pairs of labels and count, and generates a bar chart from the given pairs. Optional: a dictionary to translate the census variables into English text.
       Also takes in an optional y_label which is used to label the y-axis."""
    x = []
    y = []
    for (label, count) in pairs:
        x.append(label)
        y.append(int(count))
        
    xy = zip(x, y)
        
    if dictionary == None:
        labels = [str(label) for (label, count) in xy]
    else:
        labels = [dictionary[label] for (label, count) in xy]
    
    plt.bar(labels, y)
    plt.xticks(rotation = 45, ha="right", rotation_mode="anchor")
    plt.title(title)
    plt.ylabel(y_label)
    plt.show()
