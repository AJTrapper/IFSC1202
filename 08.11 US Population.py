# population list for population

population = []

# open input file for reading
inputfilename = "08.11 USPopulation.txt"
inputfile = open(inputfilename, 'r')
# read the imput file
line = inputfile.readline()
# check for end of file
while line != '':
    # convert input to an integer and muliply by 1000
    number = int(line)
    number = number * 1000
    # insert into list
    population.append(number)
    # read the next number
    line = inputfile.readline()
# close the input file
inputfile.close()
# print the heading
print("Year Population Change Percent Change".format())
# print first line (it is different from the rest)
print("{:4d} {:9d} N/A N/A".format(1950, (population[0])))
# diff is the diffence between the current year
# and the previous year
sumdiff = 0
maxdiff = population[1] - population[0]
maxyear = 1951
mindiff = population[1] - population[0]
minyear = 1951
# loop through the list - start at second entry
for i in range(1, len(population)):
    # Calculate the difference between the current year
    # and the previous year
    diff = population[i] - population[i-1]
    # Calculate the percent change
    percent = float(diff) / float(population[i-1]) * 100.0
    # Print the results
    print("{:4d} {:9d} {:9d} {:1.2f}%".format(1950 + i, population[i], diff, percent))
    # Determine if we have a new min or max, along with the year
    if diff > maxdiff:
        maxdiff = diff
        maxyear = 1950 + i
    if diff < mindiff:
        mindiff = diff
        minyear = 1950 + i
    sumdiff += diff
# Finished with loop - Print the trailer totals
print("")
print("Average Change = {}".format(float(sumdiff) / float(len(population) - 1.0)))
print("Minimum Change = {} ({})".format(mindiff, minyear))
print("Maximum Change = {} ({})".format(maxdiff, maxyear))