def mergelist(array_a, array_b):
  int_i = 0
  int_j = 0
  array_final = []
  while int_i < len(array_a) and int_j < len(array_b):
    if array_a[int_i] < array_b[int_j]:
      array_final.append(array_a[int_i])
      int_i+=1
    else:
      array_final.append(array_b[int_j])
      int_j+=1
  if int_i == len(array_a):
    array_final.extend(array_b[array_b[int_j]::])
  else:
    array_final.extend(array_a[array_a[int_i]::]) 
  return array_final
  
def divide(array_init):
  if len(array_init) != 1:
    left = divide(array_init[:len(array_init)//2])
    right = divide(array_init[len(array_init)//2:])
    return mergelist(left,right)
  return array_init

print(divide([1,3,8,1,2,9,14,3,4,5]))
