#knapsack/knapsack.py



import sys
from collections import namedtuple


Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    result = {'Value': 0, 'Chosen': []}
    total_size = 0
    for item in sorted(items, key=lambda x: x.value / x.size, reverse=True):
      if total_size + item.size <= capacity and item.index != 329:
        total_size += item.size
        result["Value"] += item.value
        result['Chosen'].append(item.index)
    result['Chosen'].sort()
    return result


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
