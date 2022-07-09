#import python modules
import pandas as pd
#try and except to let user know whether file name is available
try:
    #input file name and use pandas to parse through mutiple sheets using hash method
    filename = input('Enter file name: ')
    xls = pd.ExcelFile(filename)
    sheet_names = xls.sheet_names
    sheet_to_df_map = {}
    for sheet_name in xls.sheet_names:
        sheet_to_df_map[sheet_name] = xls.parse(sheet_name)
    #using the created hash pull sheet names and parse through them to identify course numbers 
    for key in sheet_to_df_map:
        df = pd.read_excel(filename, sheet_name = key)
        #data cleaning
        df.iloc[0].values.tolist()
        df.columns = df.iloc[0].values.tolist()
        df = df.iloc[1: , :]
        counts = {}
        for number in df['Class Nbr']:
            counts[number] = counts.get(number, 0) + 1
        #print user results of data parsing
        print(f'There are {len(counts)} unique classes for {key}. Below is the count of each of the class numbers:')
        print(counts)
except:
    print('Error in reading file!')
