
# Python Project

Data folder was too large to be added to git.

## Prerequisites:

This project requires the use of pandas, matplotlib, geopy, and folium.

To install all required dependencies and libraries you may use a virtual environment or just locally using the command:

    pip install -r requirements.txt

To install a virtual environment, open the terminal in the directory in which the project is unzipped:
Windows:
    1   python -m venv <name>                   (to create virtual environment)           
    2   <name>\Scripts\activate                 (to activate virtual environment)
    3   pip install -r requirements.txt         (to instal required libraries)
    
    After these steps, you can begin the analysis, simply type "deactivate" in the terminal to deactive the virtual environment.

Linux and MacOS:
    1   pip3 install virtualenv
    2   virtualenv <name>                       (to create virtual environment)
    3   source <name>/bin/activate              (to activate virtual environment)
    4   pip install -r requirements.txt         (to instal required libraries)
    5   pip install ipykernel
    6   python -m ipykernel install --user --name=<name>
    
    After these steps, you can begin the analysis, simply type "deactivate" in the terminal to deactive the virtual environment.


There should be 3 zip archives included within the "data" directory.
- census2011.csv.zip contains the original census data.
- census2011_refined.zip contains the refined data where any duplicate/contradictory entry is removed.
- migrationScotland.zip contains the additional data set.

To begin the analysis of the data used in the project, unzip the census2011_refined.zip archive.
If this file is not included, follow the instructions given in the "Quality Control and Data Refinement" of this report.

## Run the Analysis:
This report is a Jupyter Notebook file located in "code/census2011.ipynb", to open this file:
- Access the "code" directory from the terminal.
- Type "jupyter-notebook".
- Your web browser should open with the Jupyter Notebook client, access the file "census2011.ipynb" from the client.
- If you are using a virtual environment, go to Kernel ->
                                                Change kernel ->
                                                <name of virtual environment>

Run the Analysis (additional data set):
This report is a Jupyter Notebook file located in "code/migrationScotland.ipynb", to open this file:
- follow similar instructions as above but select the "migrationScotland.ipynb" from the client.
