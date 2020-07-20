# Hashing with linear and modified probing
Probing algorithms

**Linear probing**
Hashing function: 

       f1(x,i) = (h(x)+i) modulo n.  i = 0,1,...,n-1 , n = A.len , h(x) home address (checked location)

**Modified probing**
Hashing functions:

If ldown count <= lup count:

    f1(x,i) = (h(x)+i) modulo n.  i = 0,1,...,n-1 and n = A.len
  
else:

      f2(x,i) = (h(x)-i) modulo n.  i = 0,1,...,n-1 and n = A.len
