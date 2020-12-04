import csv
import os.path

filename = 'eradicated_diseases.csv'
fieldnames = ['Name of the Disease', 'Year of Last Occurrence', 'Number of Deaths', 'Founder of the Vaccine or Cure']

def save_file(fieldnames, filename):
    file_exists = os.path.isfile(filename)

    with open(filename, 'a') as csvfile:
        csvEntry = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if file_exists is False:
            csvEntry.writeheader()

        csvEntry.writerow({
            'Name of the Disease':input('What is the name of the disease\n'),
            'Year of Last Occurrence':input('When did this disease last occur\n'),
            'Number of Deaths':input('How many people died\n'),
            'Founder of the Vaccine or Cure':input('Who was the founder of the cure\n')
        })

    print('Details Saved in FIle')

def view_file(fieldnames,filename):
    with open(filename, 'r') as csvfile:
        csvReader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)

        eradicateddiseases = list(csvReader)

        for details in eradicateddiseases:
            print(f'{details["Name of the Disease"]:10}|{details["Year of Last Occurrence"]:4}|{details["Number of Deaths"]:15}|{details["Founder of the Vaccine or Cure"]:15}')

def search_file(filename):

    search=input('What disease would you like to search for\n').title()

    with open(filename, 'r') as csvfile:
        csvReader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)

        eradicateddiseases = list(csvReader)
        found=0
        for details in eradicateddiseases:
            if search == details['Name of the Disease']:
                print(f'{"Name of the Disease":25}|{"Year of Last Occurrence":25}|{"Number of Deaths":15}|{"Founder of the Vaccine or Cure":15}')
                print(f'{details["Name of the Disease"]:25}|{details["Year of Last Occurrence"]:25}|{details["Number of Deaths"]:15}|{details["Founder of the Vaccine or Cure"]:15}')
                found = 1
        if found==0:
            print("This Disease is Not in The Directory")


print('Eradicated Diseases Directory')
print('_'*30)

selection=0
while selection!=4:
    selection=int(input('''
    Enter Option Number
    -------------------
    1.) Add Eradicated Disease
    2.) View Eradicated Diseases
    3.) Search an Eradicated Disease
    4.) Exit
    '''))

    if selection == 1:
        save_file(fieldnames, filename)
    elif selection == 2:
        view_file(fieldnames, filename)
    elif selection == 3:
        search_file(filename)
    elif selection == 4:
        exit()
    else:
        print('Invalid Selection')
