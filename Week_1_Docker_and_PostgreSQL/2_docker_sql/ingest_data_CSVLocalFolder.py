#!/usr/bin/env python
# coding: utf-8

import os
import argparse

from time import time

import pandas as pd
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    csv_path = params.csv_path
    
    # Überprüfen, ob die Dateiendung korrekt ist
    if not csv_path.endswith('.csv'):
        raise ValueError("Die Datei muss im CSV-Format sein.")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Lese CSV-Datei in Teilen
    df_iter = pd.read_csv(csv_path, iterator=True, chunksize=100000)

    df = next(df_iter)

    # Überarbeite die Datumsangaben
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Erstelle die Tabelle im Datenbank, wenn sie nicht existiert
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # Füge den ersten Chunk zur Tabelle hinzu
    df.to_sql(name=table_name, con=engine, if_exists='append')

    while True: 
        try:
            t_start = time()
            
            df = next(df_iter)

            # Überarbeite die Datumsangaben
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            # Füge den nächsten Chunk zur Tabelle hinzu
            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time()

            print('Chunk hinzugefügt, dauerte %.3f Sekunden' % (t_end - t_start))

        except StopIteration:
            print("Daten erfolgreich in die Postgres-Datenbank eingefügt.")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='Benutzername für Postgres')
    parser.add_argument('--password', required=True, help='Passwort für Postgres')
    parser.add_argument('--host', required=True, help='Host für Postgres')
    parser.add_argument('--port', required=True, help='Port für Postgres')
    parser.add_argument('--db', required=True, help='Datenbankname für Postgres')
    parser.add_argument('--table_name', required=True, help='Name der Tabelle, in der die Ergebnisse gespeichert werden sollen')
    parser.add_argument('--csv_path', required=True, help='Pfad zur CSV-Datei')

    args = parser.parse_args()

    main(args)
