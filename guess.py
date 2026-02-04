tries=10000

for u in range(0,10):
   print(u,u,u,u)
print("tries ",tries-u)   
for j in range(0,7):
    print(j,j+1,j+2,j+3)
print("tries ",tries-u-j)   
for h in range(0,9):
    print(h+1,0,0,0)
print("tries ",tries-u-j-h)  
for y in range(0,9):
    print(0,y+1,0,0)
print("tries ",tries-u-j-y-h) 
for q in range(0,9):
    print(0,0,q+1,0)
print("tries ",tries-u-j-y-h-q) 
for f in range(0,9):
    print(0,0,0,f+1)
print("tries ",tries-u-j-y-h-q-f) 
