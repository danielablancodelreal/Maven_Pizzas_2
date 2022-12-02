import pandas as pd

def calidad(df):

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

if __name__ == '__main__':
    files = ['orders1.csv','order_details1.csv']

    for file in files:
        print('\nÁnalisis del fichero: {}'.format(file))
        df = pd.read_csv(file,sep=";",encoding='LATIN_1')
        calidad(df)