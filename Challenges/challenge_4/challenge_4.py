

def knapsack(capacity, items, n):
    '''
    A  method to determine the maximum value of the items included in the knapsack
  without exceeding the capacity  C

      Parameters:
      C= 50
      items = (("boot", 10, 60),
           ("tent", 20, 100),
           ("water", 30, 120),
           ("first aid", 15, 70))
      Returns: max value

    inputs: Array of tuples, weights, item values and the maximum capacity of the bag
    output: the max value the bag may contain
    '''

    if (n == 0 or capacity == 0):
        return 0

    if (items[n-1][1] > capacity):
        # print(items[n-1][1])
        return knapsack(capacity, items, n-1)

    else:
        return max(items[n-1][2] + knapsack(capacity - items[n-1][1], items, n-1 ),
                    knapsack(capacity, items, n-1))



if __name__ == "__main__":


    items = (("boot", 10, 60),
        ("tent", 20, 100),
        ("water", 30, 120),
        ("first aid", 15, 70))

    print(knapsack(50, items, len(items)))
    # Capacity of knapsack: 50
    # The value of the optimal solution to the knapsack problem is V=230
