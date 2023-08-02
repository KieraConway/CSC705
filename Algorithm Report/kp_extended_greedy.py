from __future__ import print_function

"""""""""""""""""""""""""""""""""""""""""""""
    Code 1 - Greedy Algorithm

    Assignment  5 -  Algorithm Report
    Due         July 26, 2023
    University  Dakota State University
    Student     Kiera Conway

"""""""""""""""""""""""""""""""""""""""""""""

""" ===== Script Module Importing ===== """
# Python Standard Libraries
import random                           # pseudo-random number generator
from operator import attrgetter         # intrinsic operator functions
import sys
import getopt
import math
import time

# Python 3rd Party Libraries
from prettytable import PrettyTable     # display data in table format


""" ===== Defining Script Globals ===== """
n = -1                  # number of items
max_capacity = -1       # knapsack capacity
knapsack = []           # knapsack contents
DEBUG = False           # Debug Flag

""" ===== Defining Script Classes ===== """


#
# Class:        Item
#
# Purpose:      __init__ -  initialize Item object parameters
#               update_knap_status - updates if item is in knapsack
#
class Item:

    def __init__(self, number, weight, value, in_knapsack=False):
        """ Initialize Item object """
        self.number = number
        self.weight = weight
        self.value = value
        self.efficiency = value / weight if weight != 0 else -1
        self.in_knapsack = in_knapsack

    def update_knap_status(self, status):
        """ Update Item Knapsack Status """
        self.in_knapsack = status


""" ===== Defining Script Functions ===== """



#
# Function:     ext_greedy_knapsack()
#
# Purpose:      Solves the knapsack problem using the Extended Greedy Algorithm
#
# Parameters:   item_list - A list of Items available for the knapsack
#
# Return:       current_weight - Total weight of the items in knapsack
#               current_value  - Total value of the items in knapsack
#
# Side Effect:  global variable 'knapsack' is updated to store items
#
def ext_greedy_knapsack(item_list):
    # Initialize Variables
    current_weight = 0
    current_value = 0

    # Iterate List of Items
    for each in item_list:

        # If Adding Current Item Does Not Exceed Capacity
        if each.weight + current_weight <= max_capacity:

            # Add Item to Knapsack
            knapsack.append(each)
            each.update_knap_status(True)

            # Update Knapsack Values
            current_weight += each.weight
            current_value += each.value

    # Return Total Knapsack Values
    return current_weight, current_value

#
# Function:     usage()
#
# Purpose:      Displays the usage summary for the email address DFA simulation
#
def usage():
    print_line(95)
    print("A Greedy Algorithm Solution for KP\n "
          "ver 1.0, 2023\n "
          "Usage: python 3 kp_extended_greedy.py -h -v\n\n"
          " -n <items>   \t\t Set Item Amount \t\t|   Example: python 3 kp_extended_greedy.py -n 15\n\n",
          "-h  |  --help \t\t Display Usage summary \t|   Example: python 3 kp_extended_greedy.py -h\n",
          "-d  |  --debug \t Set Debug Mode \t\t|   Example: python 3 kp_extended_greedy.py -d\t")
    print_line(95)


#
# Function:     print_line(length)
#
# Purpose:      Prints a line of specified length using hyphens
#
# Parameters:   length - The length of the line to be printed
#
def print_line(length):
    print()
    for i in range(0, length):
        print("-", end='')  # Print Separator
    print("\n")


""" ===== Main Script Starts Here ===== """

#
# Function:     main()
#
# Purpose:      The driver function for the extended greedy algorithm.
#                   - initializes the list of items
#                   - determines the knapsack capacity,
#                   - sorts list in descending order by efficiency
#                   - call extended greedy algorithm to solve kp
#                   - formats and prints result table
#
if __name__ == '__main__':

    """
    #
    # Program Initialization
    #
    """
    # Record program starting time
    p_start_time = time.time()

    ''' Initial Variables '''
    # Create Table Objects and Define Headings
    all_tbl = PrettyTable(["Item", "Weight", "Value", "Efficiency"])      # all possible items
    knap_tbl = PrettyTable(["Item", "Weight", "Value", "Efficiency"])     # knapsack items only
    summary_tbl = PrettyTable(header=False)                 # knapsack summary
    random.seed()

    ''' Parse Command Line Input '''
    # Parse User Input
    try:
        opts, args = getopt.getopt(sys.argv[1:], "dhn:", ["debug", "help"])

        for opt, arg in opts:
            if opt in ['-d', '--debug']:
                DEBUG = True

            elif opt in ['-h', '--help']:
                usage()
                exit()

            elif opt in ['-n']:
                n = int(arg)

    except Exception as err:
        print(f'Invalid Input: {err}\n Restoring Default Settings ...\n\n')


    ''' Check if in DEBUG Mode '''
    if DEBUG:

        # Set Constant Number of Items, n
        n = 10

        # Create a Constant List of n Items
        items_list = [
            Item(0, 2, 10),
            Item(1, 3, 15),
            Item(2, 5, 8),
            Item(3, 4, 12),
            Item(4, 1, 6),
            Item(5, 6, 20),
            Item(6, 2, 14),
            Item(7, 7, 30),
            Item(8, 3, 25),
            Item(9, 4, 18),
        ]

    else:
        # If User Did Not Set n
        if n == -1:
            # Set Random Number of Items, n
            n = random.randint(3, 10)

        # Create a Random List of n Items
        items_list = []
        for i in range(n):
            item = Item(i, random.randint(1, 10), random.randint(1, 100))
            items_list.append(item)


    ''' Set Capacity '''
    # Caclulate Total and Max Weights
    total_weight = sum(item.weight for item in items_list)
    max_weight = max(item.weight for item in items_list)

    # Set Capacity to Greater Value
    max_capacity = max(int(total_weight * 0.6), max_weight)

    ''' Sort List in Descending Order '''
    # Sort Items by Efficiency in Descending Order
    items_list = sorted(items_list, key=attrgetter('efficiency'), reverse=True)
    
    """
    #
    # Greedy Algorithm
    #
    """
    ''' Call Extended Greedy Algorithm to Solve KP '''
    a_start_time = time.time()          # Record algorithm starting time
    knap_weight, knap_value = ext_greedy_knapsack(items_list)
    a_end_time = time.time()            # Record algorithm ending time

    """
    #
    # Program Termination
    #
    """
    ''' Add Item Values to Tables '''
    # Table for All Items
    for each in items_list:
        all_tbl.add_row([each.number,
                         each.weight,
                         each.value,
                         math.floor(each.efficiency)])

    # Table for Knapsack Items Only
    for each in knapsack:
        knap_tbl.add_row([each.number,
                          each.weight,
                          each.value,
                          math.floor(each.efficiency)])

    # Table for Knapsack Summary
    summary_tbl.add_row(["Total Value", knap_value])
    summary_tbl.add_row(["Total Weight", knap_weight])
    summary_tbl.add_row(["Total Capacity", max_capacity])

    ''' Print Tables '''
    # Table for All Items
    print(f"From the following {n} items: ")

    knap_tbl.vrules = 0
    all_result = all_tbl.get_string()
    print(all_result)
    print()

    # Table for Knapsack Items Only
    print(f"There {'was' if len(knapsack) == 1 else 'were'} "
          f"{len(knapsack)} "
          f"{'item' if len(knapsack) == 1 else 'items'} "
          f"added to the Knapsack: ")

    knap_tbl.sortby = "Item"
    knap_tbl.vrules = 0
    knap_result = knap_tbl.get_string()
    print(knap_result)
    print()

    # Table for Knapsack Summary
    print("Greedy Knapsack Summary:")
    summary_tbl.vrules = 0
    summary_tbl.hrules = 0
    summary_tbl.align = "l"
    summary_result = summary_tbl.get_string()
    print(summary_result)
    print()

    # Record program ending time
    p_end_time = time.time()

    # Print the runtime in seconds
    print(f"Algorithm runtime: {(a_end_time - a_start_time):.6f} seconds\n"
          f"Script runtime: {(p_end_time - p_start_time):.6f} seconds")

    ''' Print End of Script Message '''
    print("\nScript End")

""" ===== End of Main Script ===== """