import pandas

data=pandas.read_csv('50_states.csv').state
if 'new york'.capitalize()==data[33]:
    print('correct')
else:
    print(data[33].lower())