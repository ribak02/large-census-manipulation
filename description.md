# Large Census Manipulation

## Overview
This project focuses on data analysis using Python, specifically with **pandas**. It includes quality control, data refinement, descriptive analysis, plotting, and performance optimization. The following requirements have been completed:

- Quality control and data refinement
- Descriptive analysis of the data
- Plotting bar charts and pie charts
- Grouping data with `groupby` objects and 3D plotting
- Filtering dataframes using pandas queries and plotting
- Interactive plots using `ipywidgets`
- Analysis of an additional dataset: [Net Migration](https://statistics.gov.scot/resource?uri=http%3A%2F%2Fstatistics.gov.scot%2Fdata%2Fnet-migration)
- Use of virtual environments
- Map generation to display results
- Performance analysis and optimization

## Python - Group Project 2: Data Analysis with pandas

### Setup Instructions
For instructions to start the analysis, please refer to the included README file.

### Quality Control and Data Refinement
A refined version of the dataset, **"census2011_refined.csv"**, has been provided in the data folder. If the file is missing, follow the instructions in the report to generate a new refined file from the original dataset.

### Descriptive Analysis
This section provides statistical insights into the dataset, displaying data types, unique values, and occurrences for each variable.

### Graphs
Several charts and plots have been created to visualize the data:
- Bar charts for records by region and occupation
- Pie charts for age distribution and economic activity distribution

Interactive widgets have been used for improved user interaction and visualization.

### Queries
We performed analyses on:
- Economically active individuals by region and age
- Discrepancies in student status and economic activity
- Hours worked per week by students

### Groupby Objects and 3D Plots
We used groupby objects to display records by region, industry, occupation, and social grade, visualized using 3D plots.

### Maps
A map has been generated to display census submissions across different regions, visualizing the data geographically.

## Performance Analysis
The performance of the functions used in the analysis has been assessed. The **clean()** function was found to be the most time-consuming, primarily due to regex matching in the `ensure_format()` method. Recommendations for optimizing performance include replacing regex matching with more efficient validation methods.

## Summary
We have completed the following:
- Descriptive analysis
- Use of ipywidgets for interactive plots
- Analysis of an additional dataset (Net Migration)
- Performance analysis and optimization
- 2D and 3D plots
- Map visualization of data

## Problems Encountered
- Difficulties with creating 3D bar plots due to non-numeric values in `matplotlib`.
- Challenges with virtual environments, and different experiences across team members.

## Reproducibility and Reusability
The code is modular and designed to be reusable in different settings, such as future census analyses. The generic functions provided, such as `print_bars` and `print_pie`, can be reused in similar projects.

## Provenance
The project started with the provided **census2011.ipynb** Jupyter Notebook.
