#1
i=1
while i<=5:
    print(i)
    i=i+1
    
#2
total_sum=0
num=int(input("enter a number to add"))
while num !=0:
    total_sum+=num
    num=int(input("enter a number to add"))
print("the total sum is", total_sum)

#3
for i in range(1,21):
    if i % 2 !=0:
        print(i)

#4
num=int(input("enter a number :"))
for i in range(1,11):
    print(f"{num} * {i} ={num * i}")
    
#5
for i in range(10,0,-1):
    print(i)
    
#6
numbers=[12,45,9,67,34,89,21]
largest=max(numbers)
print("the largest number in the list in:",largest)

#7
for i in range(1,21):
    if i % 2== 0:
        print(i)        