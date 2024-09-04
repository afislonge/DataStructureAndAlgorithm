def twoSum(nums, target):

  # dictionary to hold the two possible variable summed

  result = {}

  # traverse the list
  for i, num in enumerate(nums):
    # subtract each num from target to get two number summed to get the target
    deduct = target - num
    # check if deduct is one of the num in the result dic
    if deduct in result:
      return [result[deduct], i] # reutrn the index of the two nums
    
    result[num] = i # add object to dic

def main():
  nums = [2,7,11,15]
  target  = 9
  # Output: [0,1]

  result = twoSum(nums, target)
  print(result)

if __name__ == '__main__':
  main()

