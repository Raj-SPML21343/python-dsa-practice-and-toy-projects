# The goal is to calculate how many days the temp is above avg

# step1: write the user interface

num_of_days = int(input("How many day's temperature? "))
temps = []
for i in range(num_of_days):
    x = input(f"Day {i}'s high temp: ")
    temps.append(int(x))

# step2: calculate the avg temperature and print the number of days above avg.

avg_temp = sum(temps) / len(temps)
print("Output:")
print(f"Average = {round(avg_temp, 2)}")
days_above_avg = 0
for temp in temps:
    if temp > avg_temp:
        days_above_avg += 1

print(f"{days_above_avg} day(s) above average")
