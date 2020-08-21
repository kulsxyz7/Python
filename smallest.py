# pseudocode
# min(A,n)
# smallest = A[0] 
# for i = i to (n-1)
# if A[i] < smallest
# smallest = A[i]
# return smallest

def min(A,n):
  smallest = A[0]
  for i in range(n-1):
    if A[i] < smallest:
      smallest = A[i]
      return smallest

print(min([1, 2, 5,-99 , 0 ],10))