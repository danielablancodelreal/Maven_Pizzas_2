import pandas as pd
from datetime import datetime

def extract():
    #Cambiamos el separador ";"

    orders = pd.read_csv('orders1.csv',sep=";",encoding='LATIN_1')
    order_details = pd.read_csv('order_details1.csv',sep=";",encoding='LATIN_1')

    print('\nÁnalisis del fichero: orders1.csv')
    calidad(orders)
    print('\nÁnalisis del fichero: order_details1.csv')
    calidad(order_details)
    
    return orders, order_details

def transform(orders, order_details):
    #Usamos la función fillna con el método ffill para que rellene los 
    #huecos con los valores anteriores
    for i in range(len(order_details)-1):
        order_details.fillna(method = 'ffill')
        
    print(order_details)

def calidad(df):

    #Esta función devuelve el número de Nulls y NaNs, así como el tipo de cada columna

    null_total = df.isnull().sum().sum()
    null_columna = df.isnull().sum()

    print('\nCantidad de nulls en total:\n{}'.format(null_total))
    print('\nCantidad de nulls por columnas:\n{}'.format(null_columna))

    nan_total = df.isna().sum().sum()
    nan_columna = df.isna().sum()

    print('\nCantidad de NaN en total:\n{}'.format(nan_total))
    print('\nCantidad de NaN por columnas:\n{}'.format(nan_columna))

    tipos = df.dtypes

    print("\nTipos de datos por columnas:\n{}".format(tipos))

if __name__ == "__main__":

    orders, order_details = extract()
    transform(orders, order_details)


