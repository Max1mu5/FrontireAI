from pybliometrics.scopus import ScopusSearch
import csv
import time
import pandas as pd

start_time = time.time()

REQUEST_WORD = "tech technologies it ml ai informations"

start_time = time.time()
print("----- SEARCH -----")

scopus = ScopusSearch(REQUEST_WORD)

print("----- %s seconds -----" % (time.time() - start_time))
print('Number docs: ' + str(len(scopus.results)))



number = 0

DATA_YEARS = {}

print("preprocessing...")

for index in range(len(scopus.results)):
    try:
        if(len(scopus.results[index].authkeywords) > 0):
            """print('PUBLISH DATE: ' + str(scopus.results[index].coverDate.split('-')[0]))
            print('CITED: ' + str(scopus.results[index].citedby_count))
            print('KEY WORDS: ' + str(scopus.results[index].authkeywords))
            print('------------------------------------------------------------------------')"""
            print('.', end="")
            year = str(scopus.results[index].coverDate.split('-')[0])
            cited = str(scopus.results[index].citedby_count)
            keywords = scopus.results[index].authkeywords.split(' | ')

            
            if(int(cited) > 0):
                if(year in DATA_YEARS.keys()):
                    for k in keywords:
                        if(k in DATA_YEARS[year].keys()):
                            DATA_YEARS[year][k] = int(DATA_YEARS[year][k]) + int(cited)
                        else:
                            DATA_YEARS[year].update({k: cited})
                else:
                    DATA_YEARS.update({year: {}})
                    DATA_YEARS[year].update({k: cited for k in keywords})

            number += 1

    except:
        pass

print()
print("\nTOTAL RESULTS NUMBER: " + str(number) + "  ---  " + str(number / len(scopus.results)) + "\n")

for y in DATA_YEARS.keys():
    print(y)
    print(DATA_YEARS[y])
    print("----------------------------------------------------------------")


print("save into file data.csv ...")
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['year', 'tag', 'cited'])
    for y in DATA_YEARS.keys():
        for t in DATA_YEARS[y].keys():
            if(int(DATA_YEARS[y][t]) > 1):
                writer.writerow([y, t, str(DATA_YEARS[y][t])])

df = pd.DataFrame(data=DATA_YEARS)

print(df)

