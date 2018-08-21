import csv
from prettytable import PrettyTable

with open('RealEstate.csv') as csvfile:
    csv.register_dialect("mydata",quotechar='"',skipinitialspace=True)
    reader = csv.DictReader(csvfile,dialect="mydata")

    def final_dict(user_input):
        for row in reader:
            city_dict = {}
            if row['Location'] == user_input:
                city = {row['Location']: row['Price']}
                city_dict.update(city)
                yield city_dict

    user_input = raw_input("check city: ").title()
    result = final_dict(user_input)

    isGeneratorEmpty = True
    sum = 0
    count = 0
    table = PrettyTable(['Location', '$ Price'])

    for i in result:
        isGeneratorEmpty = False
        for k,v in i.iteritems():
            sum = sum + float(v)
            count += 1
            table.add_row([k,v])

    if isGeneratorEmpty:
        print "Sorry, No location found for {}".format(user_input)
    else:
        avg = sum / count

        print "======================== \n Search for {} \n========================".format(user_input)
        print "{} \nWe have found {} properties. \nThe average price in {} is $ {}".format(table,count, user_input, avg)