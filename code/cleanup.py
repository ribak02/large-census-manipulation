"""Cleans up file. To use this module, simply type from cleanup import clean, and run the function clean(), giving it a dataframe and the name of the refined file.""" 

import pandas as pd
import re

from functools import reduce

def declare_error():
    declare_error.errorFound = True
declare_error.errorFound = False    # Default value

def regex_match(s,regex):
    """Regex for Person ID"""
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

def ensure_format(df):
    """Ensures that the format/data type of each column is correct."""
    
    df_refined = df.copy()
    
    for (heading, regex) in headings_formats:
        df_refined[heading] = df_refined[heading].map(lambda x : regex_match(x, regex))
    
    return df_refined

def ensure_unique(df):
    """Ensures that that all IDs are unique and no rows are duplicated."""
    duped_rows = df.duplicated()
    duped_ids = df["Person ID"].duplicated()
    
    has_duped_rows = duped_rows.any()
    has_duped_ids = duped_ids.any()
    
    if(has_duped_ids or has_duped_rows):
        declare_error()
        df = df.drop_duplicates()
        df = df.drop_duplicates(subset = ["Person ID"])
    return df

def ensure_valid(df):
    """Ensures that the dataframe does not contain any NaN values"""
    has_nan = df.isnull().values.any()
    
    if(has_nan):
        declare_error()
        df = df.dropna()
    return df

def ensure_logic(df):
    """Ensure that for each row the cells abide by the specifications of the Teaching File."""
    
    
    ##### Antirequisites stated in the variables pdf #####
    
    # Family Comp. cannot be -9 if person is NOT commune resident and NOT a student/child living away during term-time, and NOT a short-term resident.
    invalid_family_comp = (df["Family Composition"] == "-9") & (df["Residence Type"] != "C") & (df["Population Base"] == "1")
    # Country of birth cannot be -9 if person is NOT student/child living away at term time.
    invalid_birth_country = (df["Country of Birth"] == "-9") & (df["Population Base"] != "2")
    # Health cannot be -9 if person is NOT student/child living away at term time.
    invalid_health = (df["Health"] == "-9") & (df["Population Base"] != "2")
    # Ethnic group cannot be -9 if person is a resident of England/Wales and is NOT a student/child living away at term time.
    invalid_ethnicity = (df["Ethnic Group"] == "-9") & (df["Population Base"] != "2")   # The requirement to state the ethnicity is for residents of England and Wales,
                                                                                        # but the regions only list places in England and Wales, so this antirequisite for -9 is omitted here.
    # Religion cannot be -9 if person is NOT a student/child living away at term time. England/Wales resident antirequisite does not apply for reasons above.
    invalid_religion = (df["Religion"] == "-9") & (df["Population Base"] != "2")
    # Economic activity cannot be -9 if person is NOT under 16 and NOT a student/child living away at term time.
    invalid_economic_activity = (df["Economic Activity"] == "-9") & (df["Age"] != "1") & (df["Population Base"] != "2")
    # Occupation cannot be -9 if person is NOT under 16, NOT a student/child living away at term time, and has NOT never worked.
    invalid_occupation = (df["Occupation"] == "-9") & (df["Age"] != "1") & (df["Population Base"] != "2")   # Economic Activity does not include options that indicate if
                                                                                                            # someone has NEVER worked, therefore this antirequisite has not been included.
    # Industry cannot be -9 if person is NOT under 16 and NOT a student/child living away at term time. Never worked requisite not included for same reason above.
    invalid_industry = (df["Industry"] == "-9") & (df["Age"] != "1") & (df["Population Base"] != "2")
    # Hours per week cannot be -9 if person is NOT under 16, employed (interpreted as being an employee or self-employed), and NOT a student/child living away at term time.
    invalid_hours_worked = (df["Hours worked per week"] == "-9") & (df["Age"] != "1") & ((df["Economic Activity"] == "1") | (df["Economic Activity"] == "2")) & (df["Population Base"] != "2")
    # Social grade cannot be -9 if person is NOT under 16, NOT living in a communal place, and NOT a student/child living away at term time.
    invalid_social_grade = (df["Approximated Social Grade"] == "-9") & (df["Age"] != "1") & (df["Residence Type"] != "C") & (df["Population Base"] != "2")
    
    ##### Contradictions #####
    # Under-16s cannot marry in the UK
    under_16s_married = (df["Age"] == "1") & (df["Marital Status"] != "1")
    # Under-16s cannot work full-time in the UK
    under_16s_full_time = (df["Age"] == "1") & ((df["Hours worked per week"] == "3") | (df["Hours worked per week"] == "4"))
    # Unemployed people must have -9 for hours worked per week
    working_while_unemployed = (df["Economic Activity"] == "3") & (df["Hours worked per week"] != "-9")
    
    
    if(invalid_family_comp.any() or invalid_birth_country.any() or invalid_health.any() or invalid_ethnicity.any() or
       invalid_religion.any() or invalid_economic_activity.any() or invalid_occupation.any() or invalid_industry.any() or
       invalid_hours_worked.any() or invalid_social_grade.any() or under_16s_married.any() or under_16s_full_time.any() or
       working_while_unemployed.any()):
        
        declare_error()
        
        # Allows anything that isn't invalid
        df = df.loc[~invalid_family_comp]
        df = df.loc[~invalid_birth_country]
        df = df.loc[~invalid_health]
        df = df.loc[~invalid_ethnicity]
        df = df.loc[~invalid_religion]
        df = df.loc[~invalid_economic_activity]
        df = df.loc[~invalid_occupation]
        df = df.loc[~invalid_industry]
        df = df.loc[~invalid_hours_worked]
        df = df.loc[~invalid_social_grade]
        
        df = df.loc[~under_16s_married]
        df = df.loc[~under_16s_full_time]
        df = df.loc[~working_while_unemployed]
        
    return df
    

def clean(df, new_file_dir):
    """Takes a dataframe and a potential new file name. Cleans the dataframe to the project specifications if necessary and stores it as the given filename. Returns either the original or refined df."""
    df_refined = ensure_format(df)
    df_refined = ensure_unique(df_refined)
    df_refined = ensure_valid(df_refined)
    df_refined = df_refined.convert_dtypes()
    df_refined = ensure_logic(df_refined)
    
    if(declare_error.errorFound):
        df_refined.to_csv(new_file_dir, index = False)
        df_refined = pd.read_csv(new_file_dir)
        return df_refined
    else:
        return df
    
def clean_no_format_check(df, new_file_dir):
    """Copy of clean() without calling ensure_format()"""
    df_refined = df.copy()
    df_refined = ensure_unique(df_refined)
    df_refined = ensure_valid(df_refined)
    df_refined = df_refined.convert_dtypes()
    df_refined = ensure_logic(df_refined)
    
    if(declare_error.errorFound):
        df_refined.to_csv(new_file_dir, index = False)
        df_refined = pd.read_csv(new_file_dir)
        return df_refined
    else:
        return df

headings_formats = [("Person ID", r"^\d+$"), ("Region", r"^(E120{5}[1-9]|W920{5}4)$"), ("Residence Type", r"^C|H$"), ("Family Composition", r"^([1-6]|-9)$"),
                    ("Population Base", r"^[1-3]$"), ("Sex", r"^[1-2]$"), ("Age", r"^[1-8]$"), ("Marital Status", r"^[1-5]$"),
                    ("Student", r"^[1-2]$"), ("Country of Birth", r"^([1-2]|-9)$"), ("Health", r"^([1-5]|-9)$"), ("Ethnic Group", r"^([1-5]|-9)$"),
                    ("Religion", r"^([1-9]|-9)$"), ("Economic Activity", r"^([1-9]|-9)$"), ("Occupation", r"^([1-9]|-9)$"), ("Industry", r"^([1-9]|1[0-2]|-9)$"),
                    ("Hours worked per week", r"^([1-4]|-9)$"), ("Approximated Social Grade", r"^([1-4]|-9)$")]
