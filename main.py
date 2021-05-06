import numpy as np
import pandas as pd
import xlrd
import openpyxl

#zadanie1

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

#zadanie2

print(df[df['Liczba'] < 1000])
print(df[df.Imie == 'ANGELIKA'])
print(sum(df['Liczba']))
print(sum(df['Liczba'] &((df.Rok) > 2004) & ((df.Rok) < 2011)))
print(sum(df['Liczba'] & ((df.Plec)== 'M') & ((df.Rok) == 2000)))
print(df.groupby(['Rok']).agg({'Liczba': ['max']}))
print(df.groupby(['Rok', 'Plec']).agg({'Liczba': ['max']}))

#zadanie3

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
nazwiska = df['Sprzedawca']
nazwiska = nazwiska.unique() # unikalne
unik = pd.Series(nazwiska)
print(unik)
df['Utarg'] = df['Utarg'].astype(float)
print(df.sort_values(by=['Utarg'], ascending=False).head(5))
print(df['Sprzedawca'].value_counts())
print(df['Kraj'].value_counts())
df['Data zamowienia'] = df['Data zamowienia'].astype('datetime64[ns]')
suma_zamowien_polska = df[(df['Kraj'] == 'Polska') &(df['Data zamowienia'].dt.year == 2005)]
print(suma_zamowien_polska.groupby('Kraj').agg({'Utarg':['sum']}))
rokczw = df[(df['Data zamowienia'].dt.year == 2004)]
print(rokczw['Utarg'].mean())
rokpiaty = df[(df['Data zamowienia'].dt.year == 2005)]
print(rokpiaty['Utarg'].mean())
rokczw.to_csv('zamówienia_2004.csv')
rokpiaty.to_csv('zamówienia_2005.csv')

