import pandas as pd
import matplotlib.pyplot as plt
import os


def analyze_data():
    file = 'measures.csv'
    if not os.path.exists(file):
        print('El archivo especificado no existe...')
        return

    df = pd.read_csv(file, index_col=None, header=0, parse_dates=True, float_precision='round_trip')
    df['measure_value'] = df['measure_value'].astype(int)

    # dataframe para obtener número que  más veces se repite del rango reportado
    df_max_measure_x_range = df.groupby(['measure_value']).size().reset_index(name='counts')
    df_max_measure_x_range = df_max_measure_x_range.sort_values(by=['counts'])
    df_max_measure_x_range.plot.bar(x='measure_value', y='counts', rot=0)

    # consumo max por dispositivo
    df_max_consumption_x_device = df.groupby(['device_id'])['measure_value'].max().reset_index(name='max_measure')
    df_max_consumption_x_device.plot.barh(x='device_id', y='max_measure')

    # numero de lecturas por dispositivo
    df_num_measures_x_device = df.groupby(['device_id']).size().reset_index(name='measures_x_device')
    df_num_measures_x_device.plot.barh(x='device_id', y='measures_x_device')

    # consumo promedio por dispositivo
    df_mean_consumption_x_device = df.groupby(['device_id'])['measure_value'].mean().reset_index(name='mean_consumption')
    df_mean_consumption_x_device.plot.barh(x='device_id', y='mean_consumption')

    # se transforma la fecha registrada a formato ddmmyyyyHHMM para obtener el numero de mediciones por minuto
    df['measure_date'] = pd.to_datetime(df.measure_date)
    df['_date'] = df['measure_date'].dt.strftime('%d%m%Y%H%M')
    df_num_measure_x_minute = df.groupby(['_date']).size().reset_index(name='counts')

    df_num_measure_x_minute.plot.barh(x='_date', y='counts')

    plt.show()


if __name__ == '__main__':
    analyze_data()