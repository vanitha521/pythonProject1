def cube(x,y,z,n):
#x=int(input())
#y=int(input())
#z=int(input())
#n=int(input())
  for i in range(0,x+1):
     for j in range(0,y+1):
         for k in range(0,z+1):
             if (i+j+k!=n):
                 print([i,j,k],end=",")
cube(2,2,2,7)
