from __future__ import print_function

"""""""""""""""""""""""""""""""""""""""""""""
    Code 2 - Dynamic Algorithm

    Assignment  5 -  Algorithm Report
    Due         July 26, 2023
    University  Dakota State University
    Student     Kiera Conway

"""""""""""""""""""""""""""""""""""""""""""""

""" ===== Script Module Importing ===== """
# Python Standard Libraries
import random                           # pseudo-random number generator
from operator import attrgetter         # intrinsic operator functions

# Python 3rd Party Libraries
from prettytable import PrettyTable     # display data in table format


""" ===== Defining Script Globals ===== """
n = -1                  # number of items
max_capacity = -1       # knapsack capacity
knapsack = []           # knapsack contents
knap_weight = 0         # knapsack weight after added items
knap_value = 0          # knapsack value after added items

""" ===== Defining Script Classes ===== """


#
# Class:        Item
#
# Purpose:      __init__ -  initialize Item object parameters
#
class Item:

    def __init__(self, number, weight, value):
        """ Initialize Item object """
        self.number = number
        self.weight = weight
        self.value = value


""" ===== Defining Script Functions ===== """


def dynamic_knapsack(item_list):
    """ Function Initialization """
    # Initialize Variables
    DP = []                 # DP optimal solution table
    current_weight = 0
    current_value = 0
    global knapsack, knap_weight, knap_value     # declare modified globals

    # Initialize DP Table
    for i in range(n + 1):
        # Create a capacity row and init to 0
        DP.append([0 for each in range(max_capacity + 1)])

    """ Bellman Recursion: Fill in DP table """
    for each_item in range(1, n+1):
        for each_capacity in range(max_capacity+1):
            current_weight = item_list[each_item - 1].weight
            current_value = item_list[each_item - 1].value

            # If Adding Current Item Exceeds Capacity
            if each_capacity < current_weight:
                # Set cell to the previous best solution
                DP[each_item][each_capacity] = DP[each_item - 1][each_capacity]     # current cell = above cell

            else:
                # Set cell to max(cell above current cell, best value for the remaining capacity)
                DP[each_item][each_capacity] = max(DP[each_item - 1][each_capacity],
                                                   DP[each_item - 1][each_capacity - current_weight] + current_value)

    """ Reconstruction: Determine items in the knapsack """
    current_item = n                    # set current item to last cell
    current_capacity = max_capacity     # set current capacity to last cell

    # Iterate backwards through table
    while current_item > 0 and current_capacity > 0:

        # If current cell is different from cell above
        if DP[current_item][current_capacity] != DP[current_item-1][current_capacity]:

            # included current_item in knapsack
            knapsack.append(item_list[current_item - 1])            # append item to knapsack list
            knap_weight += item_list[current_item - 1].weight    # update weight
            knap_value += item_list[current_item - 1].value      # update value
            current_capacity -= item_list[current_item - 1].weight  # update capacity

        current_item -= 1   # decrement cell

    """ Return optimal solution value """
    return DP[n][max_capacity]

""" ===== Main Script Starts Here ===== """
if __name__ == '__main__':

    """
    #
    # Program Initialization
    #
    """

    ''' Initial Variables '''
    # Create Table Objects and Define Headings
    all_tbl = PrettyTable(["Item", "Weight", "Value"])      # all possible items
    knap_tbl = PrettyTable(["Item", "Weight", "Value"])     # knapsack items only
    summary_tbl = PrettyTable(header=False)                 # knapsack summary

    random.seed()

    # Set Number of Items
    n = random.randint(3, 10)

    ''' Create List '''
    # Create a Random List of n Items
    items_list = []
    for i in range(n):
        item = Item(i,
                    random.randint(1, 10),
                    random.randint(1, 100))
        items_list.append(item)

    ''' Set Capacity '''
    # Calculate Total and Max Weights
    total_weight = sum(item.weight for item in items_list)
    max_weight = max(item.weight for item in items_list)

    # Set Capacity to Greater Value
    max_capacity = max(int(total_weight * 0.6), max_weight)

    """
    #
    # Dynamic Programming Algorithm
    #
    """
    ''' Call DP Function '''
    optimal_value = dynamic_knapsack(items_list)


    """
    #
    # Program Termination
    #
    """
    ''' Add Item Values to Tables '''
    # Table for All Items
    for each in items_list:
        all_tbl.add_row([each.number, each.weight, each.value])

    # Table for Knapsack Items Only
    for each in knapsack:
        knap_tbl.add_row([each.number, each.weight, each.value])

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

    knap_tbl.vrules = 0
    knap_result = knap_tbl.get_string()
    print(knap_result)
    print()

    # Table for Knapsack Summary
    print("Knapsack Summary:")
    summary_tbl.vrules = 0
    summary_tbl.hrules = 0
    summary_tbl.align = "l"
    summary_result = summary_tbl.get_string()
    print(summary_result)
    print()

    ''' Print End of Script Message '''
    print("\nScript End")

""" ===== End of Main Script ===== """