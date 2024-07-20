# problem 1
"""Write a Python function result10 that takes a list of integers as an argument and
 returns a pair of numbers from the list that add up to 10.
 If no such pair exists, the function should return -1"""

number = [6,5,4,3,9,8,0]
def result10(number):
  for i in range(len(number)-1):
    for j in range(i+1,len(number)):
      if number[i]+number[j]==10:
        return number[i],number[j]
  return -1

print(result10(number))

# Problem 2
"""You are given an array of integers and a target integer.
 Write a Python function that rearranges the elements in the array 
 such that all instances of the target integer are moved to the end of the array,
 while maintaining the relative order of the other elements."""

number = [6,1,6,8,10,4,15,6,9,6]
def targetRIght(array,target):
  j = len(array)-1
  for i in range(len(array)):
    if i == j:
      break
    if array[j] == target:
      for j in range(len(array)-1,i,-1):
        if array[j] != target:
          break
    if array[i] == target:
      array[i] = array[j]
      array[j] = target
      j -= 1
  return array
print(targetRIght(number,6))

# another approach

def targetright(array,target):
  left = 0
  right = len(array)-1

  while left < right:
    while left < right and array[left] != target:
      left += 1
    while left < right and array[right] == target:
      right -= 1
    if left < right and array[left] == target:
      array[left] = array[right]
      array[right] = target
      left += 1
      right -= 1
  return array
print(targetright(number,6))
