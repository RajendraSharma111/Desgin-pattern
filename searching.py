# Binary search algo.
def binary(array, left, right, value):
  mid = (left + right) / 2
  if (array[mid] == value):
    print 'Value found--- index %s'%mid
    return
  elif (array[mid] > value):
    binary(array, left, mid, value)
  elif (array[mid] < value):
    binary(array, mid, right, value)

#binary([1,3,4,6,7,8], 0, 6, 8)

