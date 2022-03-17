"""Profiler for functions in census2011.ipynb."""
import cProfile
import time

# Testing functions from these files:
from cleanup import *
from plot3d import *
from queries import *
from variables import *

def run_profile(functions):
    """Takes a list of pairs of function names and functions (in string form) and profiles the functions."""
    for (function_name, function) in functions:
        cProfile.run(function)
        print("")
        print("Finished profiling:", function_name)
        print("======================================")
        print("")
    
def timer(functions, threshold):
    """Performs a series of functions, at the end it will print out the results of whether or not the time taken for each function meets the threshold.
       Takes in a list of pairs of function names and functions, and a threshold int in seconds.
       Returns a list of tuples of function names, booleans (whether or not the threshold has reached) and the time taken."""
    result = []
    for (function_name, function) in functions:
        start = time.time()
        function()
        end = time.time()
        
        time_taken = end-start
        threshold_reached = time_taken > threshold
        print("timer(): Finished running", function_name)
        
        result.append((function_name, threshold_reached, time_taken))
    print("")
    return result

def is_satisfactory(results):
    """Takes timer() results and prints an appropriate message for each."""
    for (name, threshold_reached, time) in results:
        result = name + " : took " + str(time) + " seconds"
        if threshold_reached:
            result += ", which is above the given threshold."
        else:
            result += ", which is below the given threshold."
        print(result)
