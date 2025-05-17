import pandas as pd

#list
list_name = ['Ariana', 'Vini', 'Anny']
print(f'list name: \n{list_name}')
print(f'first element: {list_name[0]}')

#dictionary
dictionary_person = {
    'name': 'Ariana',
    'age': '31',
    'city': 'boca raton'
}

print(f'dictionary person: {dictionary_person}')
print(f'first city: {dictionary_person['city']}')

#dictionary+list
list_dictionary = [
    {'name': 'Ariana', 'age': 31,'city': 'boca raton'},
     {'name': 'vini','age': 26,'city': 'cururu'},
     {'name': 'Anny','age': 21,'city': 'oz'}]

#data frame: bidimensional data estructure
df = pd.DataFrame(list_dictionary)
print(df)

#select column
print(f'{df['name']}\n')

#select several columns
print(f'{df[['name', 'city']]}\n')

#select lines by index
print(f'fisrt line\n {df.iloc[1]}\n')

#add new column
df['salary'] = [1500, 1500, 1500]
print(f'{df}\n')

#add new record
df.loc[len(df)] = {'name': 'dulce','age': 39,'city': 'oz', 'salary': 1500}
print(f'{df}\n')

#remove columns
df.drop('salary', axis=1, inplace=True)
print(f'{df}\n')

#filter by age
filter_age = df[df['age'] < 27]
print(f'filter by age:\n {filter_age}\n')

#saving the dataframe in a csv file
df.to_csv('data.csv', index=False)

#reading a csv file in a dataframe
df_read = pd.read_csv('data.csv')
print(f'csv reading:\n{df_read}\n')
