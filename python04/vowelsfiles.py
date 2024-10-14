#!/bin/env python3
# Read a string from STDIN until *
# Show the frequency of vowels formatted as:
# vowel --> frequency
# Write results to txt file then read from file and Show
# Write results to csv file then read from file and show 
# Write results to json file then read from file and show
import csv
import pandas 
import json

def frequency(c,string):
    return string.lower().count(c)   

def frequencies(string):
    data = {}
    for c in "aeiou":
        data[c] = frequency(c,string)
    return data

def show(data):
    for key in data:
        print(f'{key} --> {data[key]}')

def save_to_text(structure):
    handler = open('data.txt','w')
    for data in structure:
        for key in data.keys():
            handler.write(f'{key} --> {data[key]}')
            handler.write('\n')
    handler.close()

def read_from_txt():
    handler = open('data.txt','r')
    content = handler.read()
    print(content)
    handler.close()

def save_to_csv(structure):
    header = ['Vowel', 'Freqency']
    with open('data.csv','w') as handler:
        writer = csv.writer(handler)
        writer.writerow(header)
        for data in structure:
            for key in data.keys():
                writer.writerow([key,data[key]])

def read_from_csv():
    df = pandas.read_csv('data.csv')
    print(df)

def save_to_json(structure):
    handler = open('data.json','w')
    json.dump(structure,handler,indent=2)
    handler.close()

def read_from_json():
    handler = open('data.json','r')
    content = json.load(handler)
    print(json.dumps(content,indent=4))
    handler.close()

def run():
    structure = []
    s = input('String: ')
    while s != '*':
        data = frequencies(s)
        structure.append(data)
        # show(data)  
        save_to_text(structure) 
        save_to_csv(structure) 
        save_to_json(structure)      
        s = input('String: ')
    read_from_txt()
    read_from_csv()
    read_from_json()
run()




