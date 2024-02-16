print("--------------TASK 01-------------")
print("Enter the total number of cows")
total_cows=int(input())
print("--------------DAY 1-------------")
id_number=[]
milk_yield_morning_day_1=[]
print(f"In morning (Day 1)")
i=0
while i<total_cows:
    print(f"Enter the id number of the cow ")
    num=int(input())
    id_number.append(num)
    print(f"Enter the amount of milk given by cow id_number#{num} ")
    milk=float(input())
    milk_yield_morning_day_1.append(milk)
    i+=1
milk_yield_evening_day_1=[]
print(f"In evening (Day 1):")
i=0
while i<total_cows:
    print(f"Enter the milk got from cow id#{id_number[i]}")
    milk=float(input())
    milk_yield_evening_day_1.append(milk)
    i+=1
print("--------------DAY 2-------------")
milk_yield_morning_day_2=[]
print(f"In morning (Day 2)")
i=0
while i<total_cows:
    print(f"Enter the amount of milk given by cow id_number#{num} ")
    milk=float(input())
    milk_yield_morning_day_2.append(milk)
    i+=1
milk_yield_evening_day_2=[]
print(f"In evening (Day 2):")
i=0
while i<total_cows:
    print(f"Enter the milk got from cow id#{id_number[i]}")
    milk=float(input())
    milk_yield_evening_day_2.append(milk)
    i+=1


print("--------------DAY 3-------------")
milk_yield_morning_day_3=[]
print(f"In morning (Day 3)")
i=0
while i<total_cows:
    print(f"Enter the amount of milk given by cow id_number#{num} ")
    milk=float(input())
    milk_yield_morning_day_3.append(milk)
    i+=1
milk_yield_evening_day_3=[]
print(f"In evening (Day 3):")
i=0
while i<total_cows:
    print(f"Enter the milk got from cow id#{id_number[i]}")
    milk=float(input())
    milk_yield_evening_day_3.append(milk)
    i+=1

print("--------------DAY 4-------------")
milk_yield_morning_day_4=[]
print(f"In morning (Day 4)")
i=0
while i<total_cows:
    print(f"Enter the amount of milk given by cow id_number#{num} ")
    milk=float(input())
    milk_yield_morning_day_4.append(milk)
    i+=1
milk_yield_evening_day_4=[]
print(f"In evening (Day 4):")
i=0
while i<total_cows:
    print(f"Enter the milk got from cow id#{id_number[i]}")
    milk=float(input())
    milk_yield_evening_day_4.append(milk)
    i+=1

print("--------------DAY 5-------------")
milk_yield_morning_day_5=[]
print(f"In morning (Day 5)")
i=0
while i<total_cows:
    print(f"Enter the amount of milk given by cow id_number#{num} ")
    milk=float(input())
    milk_yield_morning_day_5.append(milk)
    i+=1
milk_yield_evening_day_5=[]
print(f"In evening (Day 5):")
i=0
while i<total_cows:
    print(f"Enter the milk got from cow id#{id_number[i]}")
    milk=float(input())
    milk_yield_evening_day_5.append(milk)
    i+=1

print("--------------DAY 6-------------")
milk_yield_morning_day_6=[]
print(f"In morning (Day 6)")
i=0
while i<total_cows:
    print(f"Enter the amount of milk given by cow id_number#{num} ")
    milk=float(input())
    milk_yield_morning_day_6.append(milk)
    i+=1
milk_yield_evening_day_6=[]
print(f"In evening (Day 6):")
i=0
while i<total_cows:
    print(f"Enter the milk got from cow id#{id_number[i]}")
    milk=float(input())
    milk_yield_evening_day_6.append(milk)
    i+=1


print("--------------DAY 7-------------")
milk_yield_morning_day_7=[]
print(f"In morning (Day 7)")
i=0
while i<total_cows:
    print(f"Enter the amount of milk given by cow id_number#{num} ")
    milk=float(input())
    milk_yield_morning_day_7.append(milk)
    i+=1
milk_yield_evening_day_7=[]
print(f"In evening (Day 7):")
i=0
while i<total_cows:
    print(f"Enter the milk got from cow id#{id_number[i]}")
    milk=float(input())
    milk_yield_evening_day_7.append(milk)
    i+=1

print("--------------TASK 02-------------")
i=1
while i<=total_cows:
    milk_vol_mor=milk_yield_morning_day_1[i-1]+milk_yield_morning_day_2[i-1]+milk_yield_morning_day_3[i-1]+milk_yield_morning_day_4[i-1]+milk_yield_morning_day_5[i-1]+milk_yield_morning_day_6[i-1]+milk_yield_morning_day_7[i-1]
    milk_vol_eve=milk_yield_evening_day_1[i-1]+milk_yield_evening_day_2[i-1]+milk_yield_evening_day_3[i-1]+milk_yield_evening_day_4[i-1]+milk_yield_evening_day_5[i-1]+milk_yield_evening_day_6[i-1]+milk_yield_evening_day_7[i-1]
    total_milk=milk_vol_mor+milk_vol_eve
    avg_milk=(milk_vol_mor+milk_vol_eve)/14
    print(f"The total volume of milk given by cow {id_number[i-1]} is {milk_vol_mor+milk_vol_eve}")
    print(f"The average milk produced by {id_number[i-1]} is {avg_milk}")
    if total_milk < 75 :
        print(f"The cow with id{id_number[i-1]} has produced les than 12 kg of milk for about four days ")
    i+=1

