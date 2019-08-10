def knapsack(C, items, n):
  ''' A  method to determine the maximum value of the items included in the knapsack
without exceeding the capacity  C

    Parameters:
    C= 50
    items = (("boot", 10, 60),
         ("tent", 20, 100),
         ("water", 30, 120),
         ("first aid", 15, 70))
    Returns: max value
'''

def recursive_knapsack(items, capacity):
    '''
    inputs: Array of tuples, weights, item values and the maximum capacity of the bag
    output: the max value the bag may contain
    '''
    if len(items) == 0 or capacity == 0:
        return 0
    item = items[0]
    if item[0] > capacity:
        return recursive_knapsack(items[1:], capacity)
    value_without = recursive_knapsack(items[1:], capacity)
    value_with = recursive_knapsack(
        items[1:], capacity - item[0]) + item[1]
    return max(value_with, value_without)


if __name__ == "__main__":


items = (("boot", 10, 60),
         ("tent", 20, 100),
         ("water", 30, 120),
         ("first aid", 15, 70))
# Capacity of knapsack: 50
# The value of the optimal solution to the knapsack problem is V=230
