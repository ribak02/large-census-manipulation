import pandas as pd
import re

from functools import reduce

def declare_error():
    declare_error.errorFound = True
declare_error.errorFound = False    # Default value

def regex_match(s,regex):
    #  """Regex for Person ID"""
    if not isinstance(s,str):
        if isinstance(s,float) and s == s:  # s != s for NaN
            if s - int(s) != 0:     # Must be whole numbers.
                declare_error()
            else:
                s = int(s)
        s = str(s)
    match = re.search(regex,s)
    if match != None:
        return match.group(0)
    else:
        declare_error()

def ensure_valid(df):
    """Ensures that the dataframe does not contain any NaN values"""
    has_nan = df.isnull().values.any()
    
    if(has_nan):
        declare_error()
        df = df.dropna()
    return df

def ensure_unique(df):
    """Ensures that no rows are duplicated."""
    duped_rows = df.duplicated()
    
    has_duped_rows = duped_rows.any()
    
    if(has_duped_rows):
        declare_error()
        df = df.drop_duplicates()
    return df

def ensure_formatting(df):
    """Ensures that the format/data type of each column is correct."""
    
    df_refined = df.copy()
    
    for (heading, regex) in headings_formats:
        df_refined[heading] = df_refined[heading].map(lambda x : regex_match(x, regex))
    
    return df_refined

def cleanup(df, new_file_dir):
    """Takes a dataframe and a potential new file name. Cleans the dataframe to the project specifications if necessary and stores it as the given filename. Returns either the original or refined df."""
    df_refined = ensure_formatting(df)
    df_refined = ensure_unique(df_refined)
    df_refined = ensure_valid(df_refined)
    df_refined = df_refined.convert_dtypes()
    
    if(declare_error.errorFound):
        df_refined.to_csv(new_file_dir, index = False)
        df_refined = pd.read_csv(new_file_dir)
        return df_refined
    else:
        return df

headings_formats = [("FeatureCode", r"^S120000[0-9][0-9]$"), ("DateCode", r"^[1-2][0-9][0-1][0-9]$"), ("Measurement", r"^Count$"), ("Units", r"^People$"), ("Value", r"^[-+]?[0-9]+$"), ("Sex", r"^((All)|(Male))|(Female)$"), 
                    ("Age", r"^((All)|(\d+-\d+\syears))|(90\syears\sand\sover)$")]
# headings_formats = [("Person ID", r"^\d+$"), ("Region", r"^(E120{5}[1-9]|W920{5}4)$"), ("Residence Type", r"^C|H$"), ("Family Composition", r"^([1-6]|-9)$"),
#                     ("Population Base", r"^[1-3]$"), ("Sex", r"^[1-2]$"), ("Age", r"^[1-8]$"), ("Marital Status", r"^[1-5]$"),
#                     ("Student", r"^[1-2]$"), ("Country of Birth", r"^([1-2]|-9)$"), ("Health", r"^([1-5]|-9)$"), ("Ethnic Group", r"^([1-5]|-9)$"),
#                     ("Religion", r"^([1-9]|-9)$"), ("Economic Activity", r"^([1-9]|-9)$"), ("Occupation", r"^([1-9]|-9)$"), ("Industry", r"^([1-9]|1[0-2]|-9)$"),
#                     ("Hours worked per week", r"^([1-4]|-9)$"), ("Approximated Social Grade", r"^([1-4]|-9)$")]