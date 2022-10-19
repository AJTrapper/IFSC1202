population = []
inputfilename = "08.11 USPopulation.txt"
inputfile = open(inputfilename, 'r')
line = inputfile.readline()
while line != '':
    number = int(line)
    number = number * 1000
    population.append(number)
    line = inputfile.readline()
inputfile.close()
print("Year Population Change Percent Change".format())
print("{:4d} {:9d}     N/A    N/A".format(1950, (population[0])))
sumdiff = 0
maxdiff = population[1] - population[0]
maxyear = 1951
mindiff = population[1] - population[0]
minyear = 1951
for i in range(1, len(population)):
    diff = population[i] - population[i-1]
    percent = float(diff) / float(population[i-1]) * 100.0
    print("{:4d} {:9d} {:9d} {:1.2f}%".format(1950 + i, population[i], diff, percent))
    if diff > maxdiff:
        maxdiff = diff
        maxyear = 1950 + i
    if diff < mindiff:
        mindiff = diff
        minyear = 1950 + i
    sumdiff += diff
print("")
print("Average Change = {}".format(float(sumdiff) / float(len(population) - 1.0)))
print("Minimum Change = {} ({})".format(mindiff, minyear))
print("Maximum Change = {} ({})".format(maxdiff, maxyear))