A = [6,1,4,6,3,2,7,4]
K = 3
L = 2
def getapple(A,K):
  Alice = []
  sum = 0
  print(A)
  for (i,a) in enumerate(A):
    if(i<=len(A)-K):
      for j in range(K):
        sum = sum + A[j+i]
        if(j == K-1):
          Alice.append(sum)
          sum = 0
  
  print('Alice can get ',Alice)
  # Max arr Alice and detect index of arr and pop 3 before arr in A
  #find Max Alice and index 
  Alice_max_value = max(Alice)
  Alice_max_index = Alice.index(Alice_max_value)
  print('Max of Alice is ',Alice_max_value)

  #pop 3 in A by index Alice
  for i in range(K):
    A.pop(Alice_max_index+1)
  Bob = []
  sum = 0
  for (i,a) in enumerate(A):
    if(i<=len(A)-L):
      for j in range(L):
        sum = sum + A[j+i]
        if(j == L-1):
          Bob.append(sum)
          sum = 0
  print('Bob can get ',Bob)
  Bob_max_value = max(Bob)
  print('Max of Bob is ',Bob_max_value)
  print('Sum of Alice and Bob can get apple is', Alice_max_value+Bob_max_value)
  return Alice_max_value+Bob_max_value
  pass

print(getapple(A,K))