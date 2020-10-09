#rock_paper_scissors/rps.py



import sys


def rock_paper_scissors(n):
  moves = ['rock', 'paper', 'scissors']
  output = []
  if n == 0:
    return [[]]
  if n == 1:
    return [[m] for m in moves]
  else:
    for x in rock_paper_scissors(n-1):
      output.append((x + [moves[0]]))
      output.append((x + [moves[1]]))
      output.append((x + [moves[2]]))
    return output


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
