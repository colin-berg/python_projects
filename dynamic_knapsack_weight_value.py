def dynamic_knapsack(weight_cap, weights, values):
  rows = len(weights) + 1
  cols = weight_cap + 1
  # Set up 2D array
  matrix = [ [] for x in range(rows) ]

  # Iterates through every row
  for index in range(rows):
    # Initialize columns for this row
    matrix[index] = [ -1 for y in range(cols) ]

    # Iterates through every column
    for weight in range(cols):

      # Conditional to calculate what objects we can keep in the knapsack
      if index == 0 or weight == 0:
        matrix[index][weight] = 0
      elif weights[index - 1] <= weight:
        include_item = values[index - 1] + matrix[index - 1][weight - weights[index - 1]]

        exclude_item = matrix[index - 1][weight]

        matrix[index][weight] = max(include_item, exclude_item)
      else:
        matrix[index][weight] = matrix[index - 1][weight]
    

  # Returns the value of the bottom right of matrix
  return matrix[rows-1][weight_cap]

# Function tests:
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(dynamic_knapsack(weight_cap, weights, values))
