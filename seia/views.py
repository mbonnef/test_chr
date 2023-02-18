from django.shortcuts import render
from seia.models import Proyecto

import pandas as pd
import requests
from bs4 import BeautifulSoup


def ver_proyectos(request):

    lista_proyectos = Proyecto.objects.all().order_by('no')

    return render(request, 'seia/ver_proyectos.html', {'proyectos': lista_proyectos})


def actualizar_proyectos(request):

    # Se eliminan todas las entidades existentes para evitar duplicados
    Proyecto.objects.all().delete()

    # Cargado de datos

    listado = []

    try:
        # for i, _ in enumerate(iter(bool, True), start=1): # Busca valores hasta el infinito
        for i in range(1, 11):

            url = 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_fila_actual=' + \
                str(i)
            # url = 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_fila_actual=1'
            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'lxml')
            # print(f'Extracción de url {url:}')

            for row in soup.find('table').find_all('tr'):
                extraido = ([x.text for x in row.find_all('td')])

                if len(extraido) > 1:
                    listado.append(extraido[0:9])

    except:
        pass

    columnas = ['Numero', 'Nombre', 'Tipo', 'Region', 'Tipologia', 'Titular',
                'Inversion', 'Fecha Presentacion - Fecha de Ingreso(*)', 'Estado']

    df = pd.DataFrame.from_records(listado, columns=columnas)

    # Conversión de formatos

    df['Numero'] = df['Numero'].astype(int)
    df['Inversion'] = df['Inversion'].str.replace(
        '.', '', regex=True).str.replace(',', '.', regex=True).astype(float)
    df['Fecha Presentacion - Fecha de Ingreso(*)'] = pd.to_datetime(
        df['Fecha Presentacion - Fecha de Ingreso(*)'])

    # Exporatción en JSON

    df.to_json('./seia/json/exportado.json')

    # Carga de datos en modelo

    for index, row in df.iterrows():
        model = Proyecto()

        model.no = row['Numero']
        model.nombre = row['Nombre']
        model.tipo = row['Tipo']
        model.region = row['Region']
        model.tipologia = row['Tipologia']
        model.titular = row['Titular']
        model. inversion = row['Inversion']
        model.fecha = row['Fecha Presentacion - Fecha de Ingreso(*)']
        model.estado = row['Estado']

        model.save()

    return render(request, 'seia/actualizar_proyectos.html')
