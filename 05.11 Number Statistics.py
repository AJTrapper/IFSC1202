x = int(input("Enter a Value (zero to quit): "))
maximum = x
minimum = x
count = 0
sum = x
while x != 0:
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x
    x = int(input("Enter a Value (zero to quit): "))
    count = count +1
    sum = sum +x
print("Count: {}".format(count))
print("Sum: {}".format(sum))
print("Average: {}".format(sum/count))
print("Minimum:  {}".format(minimum))
print("Maximum:  {}".format(maximum))