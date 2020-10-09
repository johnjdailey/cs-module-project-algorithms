#making_change/making_change.py



import sys


def making_change(amount, denominations):
  if amount <=0:
    return 1

  possibilities = [0 for x in range(amount+1)]
  possibilities[0] = 1
  
  for i in range(0, len(denominations)):
      for j in range(denominations[i], amount+1):
        possibilities[j] += possibilities[j-denominations[i]]
  return possibilities[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
