import numpy as np
import pandas as pd
import xlrd
import openpyxl

#zadanie1

# xlsx = pd.ExcelFile('imiona.xlsx')
# dan = pd.read_excel(xlsx, header=0)
# print(dan)
#
# #zadanie2
#
# print(dan[dan['Liczba'] < 1000])
# print(dan[dan.Imie == 'ANGELIKA'])
# print(sum(dan['Liczba']))
# print(sum(dan['Liczba'] &((dan.Rok) > 2004) & ((dan.Rok) < 2011)))
# print(sum(dan['Liczba'] & ((dan.Plec)== 'M') & ((dan.Rok) == 2000)))
# print(dan.groupby(['Rok']).agg({'Liczba': ['max']}))
# print(dan.groupby(['Rok', 'Plec']).agg({'Liczba': ['max']}))

#zadanie3

dan1 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
nazwiska = dan1['Sprzedawca']
nazwiska = nazwiska.unique() # unikalne
unik = pd.Series(nazwiska)
print(unik)
dan1['Utarg'] = dan1['Utarg'].astype(float)
print(dan1.sort_values(by=['Utarg'], ascending=False).head(5))
print(dan1['Sprzedawca'].value_counts())
print(dan1['Kraj'].value_counts())
dan1['Data zamowienia'] = dan1['Data zamowienia'].astype('datetime64[ns]')
suma_zamowien_polska = dan1[(dan1['Kraj'] == 'Polska') &(dan1['Data zamowienia'].dt.year == 2005)]
print(suma_zamowien_polska.groupby('Kraj').agg({'Utarg':['sum']}))
rokczw = dan1[(dan1['Data zamowienia'].dt.year == 2004)]
print(rokczw['Utarg'].mean())
rokpiaty = dan1[(dan1['Data zamowienia'].dt.year == 2005)]
print(rokpiaty['Utarg'].mean())
rokczw.to_csv('zamówienia_2004.csv')
rokpiaty.to_csv('zamówienia_2005.csv')

