n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667 
# i = 2

# num=int(input("enter a number"))
num = n
factors=[]
for i in range(1,num+1):
    if num%i==0:
       factors.append(i)

print ("Factors of {} = {}".format(num,factors))