from django.shortcuts import render
from bikesantiago.models import Estacion

import requests
import pandas as pd


def ver_estaciones(request):

    lista_estaciones = Estacion.objects.all().order_by('uid')

    return render(request, 'bikesantiago/ver_estaciones.html', {'estaciones': lista_estaciones})


def actualizar_estaciones(request):

    # Se eliminan todas las entidades existentes para evitar duplicados
    Estacion.objects.all().delete()

    # Cargado de datos
    r = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    resultado = r.json()

    estaciones = resultado.get('network')
    estaciones = estaciones['stations']

    df = pd.DataFrame(estaciones)

    df = df['extra'].apply(pd.Series)
    df['payment'].apply(pd.Series)

    # Cambio de formato de hora

    df['last_updated'] = pd.to_datetime(df['last_updated'], unit='s')
    df['last_updated'] = df['last_updated'].dt.tz_localize(
        'UTC').dt.tz_convert('America/Santiago')

    df['payment'] = [','.join(map(str, l)) for l in df['payment']]

    # Columna con valor 0
    df.drop(labels=['altitude'], axis=1, inplace=True)

    # Cambio de nombre de columnas
    df.columns = ['direccion', 'cant_bicicletas_e', 'bicicletas_e', 'ultima_actualizacion', 'cant_bicicletas_n',
                  'formas_pago', 'terminal_pago', 'codigo_postal', 'arrendando', 'devolviendo', 'slots', 'uid']

    # Cambios de formato para evitar problemas en django
    df['uid'] = df['uid'].astype(int)
    df['slots'] = df['slots'].astype(int)
    df['cant_bicicletas_n'] = df['cant_bicicletas_n'].astype(int)
    df['cant_bicicletas_e'] = df['cant_bicicletas_e'].astype(int)
    df['arrendando'] = df['arrendando'].astype(int)
    df['devolviendo'] = df['devolviendo'].astype(int)

    # Cargado de datos

    for index, row in df.iterrows():
        model = Estacion()

        model.uid = row['uid']
        model.ultima_actualizacion = row['ultima_actualizacion']
        model.direccion = row['direccion']
        model.codigo_postal = row['codigo_postal']
        model.slots = row['slots']
        model.cant_bicicletas_n = row['cant_bicicletas_n']
        model.bicicletas_e = row['bicicletas_e']
        model.cant_bicicletas_e = row['cant_bicicletas_e']
        model.arrendando = row['arrendando']
        model.devolviendo = row['devolviendo']
        model.terminal_pago = row['terminal_pago']
        model.formas_pago = row['formas_pago']

        model.save()

    return render(request, 'bikesantiago/actualizar_estaciones.html')
