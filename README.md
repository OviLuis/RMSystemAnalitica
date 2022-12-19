# RMSystemAnalitica
Script de python para la analitica de las lecturas generadas por el simulador RMSystem. El script esta encargado de leer un archivo en CSV que puede ser descargado desde http://localhost:8000/down_load_csv_file/, y con los datos generar una serie de graficas donde se pueden visualizar los siguientes datos:

1. El número que más veces se repite de un rango reportado.
2. Número de datos se han reportado por minuto
3. Mayor consumo por dispositivo (medidor)
4. Número de lecturas por dispositivo
5. Valor promedio de lecturas reportadas por dispotivo


Para ejecutar el archivo localmente:

1. Instalar los requerimientos `pip install -r requirements.tx` en un ambiente virtual
2. En la raiz del proyecto guardar el archivo CSV obtenido de la ruta http://localhost:8000/down_load_csv_file/. El archivo debe tener el nombre `measures.csv`
3. ejecutar `python analitica.py` en una consola (cmd) de windows o en una terminar de linux.
