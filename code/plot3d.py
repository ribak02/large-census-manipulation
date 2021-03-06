"""Code to generate 3d plots."""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_plot(title, df, x, y, z, x_dict = None, y_dict = None, z_dict = None):
    """Generate 3d plot, requires a title, a dataframe, names of x, y, and z axes, and variable-name dictionaries for x, y and z (optional)."""
    graph = plt.figure(figsize=(10,10))
    ax = plt.axes(projection ='3d')

    ax.set_title(title)

    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    
    # Change -9 to 0 such that there is equal spacing between axis ticks.
    x_values = df[x].map(lambda a : 0 if a == -9 else a)
    y_values = df[y].map(lambda a : 0 if a == -9 else a)
    z_values = df[z].map(lambda a : 0 if a == -9 else a)

    ax.bar(x_values, z_values, y_values, zdir='y', color=['r','g','b'], alpha=0.8, edgecolor = "black")
    
    if(x_dict != None):
        ax.set_xticks(x_values)
        ax.set_xticklabels(map((lambda a : x_dict[a]), df[x]), rotation = 45, ha="right", rotation_mode="anchor")
    if(y_dict != None):
        ax.set_yticks(y_values)
        ax.set_yticklabels(map((lambda a : y_dict[a]), df[y]), rotation = -15, ha="left", rotation_mode="anchor")
    if(z_dict != None):
        ax.set_zticks(z_values)
        ax.set_zticklabels(map((lambda a : z_dict[a]), df[z]))

    plt.show()

def flatten(series, column_1 = "Column 1", column_2 = "Column 2", column_3 = "Column 3"):
    """Takes a series with a format ((column_1, column_2), column_3) generated by groupby().Column1.count() and generate a df with a records count column to make it usable for generate_plot."""
    df = pd.DataFrame({ column_1 : [],
                        column_2 : [],
                        column_3 : []
                        })
    for ((c1, c2), c3) in series.items():
        df = df.append(pd.DataFrame({column_1 : [c1], column_2 : [c2], column_3 : [c3] }), ignore_index=True)
    return df.convert_dtypes()
