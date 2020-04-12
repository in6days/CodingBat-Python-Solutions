#Medium warmup string/list problems with loops

#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  if n>=0:
    return n*str

#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3. Return n copies of the front;
def front_times(str, n):
    front = str[:3]
    if len(str) < 3:
        return n * str
    else:
        return n * front

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
    new_str = ''
    for i in range(len(str)):
        if i % 2 == 0:
            new_str = new_str + str[i]
    return new_str

#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result = result + str[:i + 1]
    return result

#Given a string, return the count of the number of times that a substring length 2 appears in the string and also
# as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
  count = 0
  for i in range(len(str)-2):
    if str[i:i+2] == str[-2:]:
      count = count + 1
  return count

#Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count = count+1
  return count

#Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.
def array_front9(nums):
    front9 = len(nums)
    if front9 > 4:
        front9 = 4
    for i in range(front9):
        if nums[i] == 9:
            return True
    return False

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
  array123 = [1, 2, 3]
  for i in range(len(nums)):
    if nums[i:i+3] == array123:
      return True
  return False

#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the
# same place in both strings.
def string_match(a, b):
  count = 0

  for i in range(min(len(a), len(b)) - 1):
    if a[i:i+2] == b[i:i+2]:
        count = count +1
  return count

#In6days
