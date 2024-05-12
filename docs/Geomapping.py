import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
import pandas as pd
import csv



'''

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")

ip_add = input("Enter IP: ")  # 198.35.26.96
printDetails(ip_add)
'''

csv_datei = '/Users/mglueck/Documents/Manuel /Privat/Netflix/netflix-report/IP_ADDRESSES/IpAddressesStreaming.csv'


def print_coordinates(ip):
    try:
        res = DbIpCity.get(ip, api_key="free")
        return {'IP Address': ip, 'Coordinates': res.latitude, 'Longitude': res.longitude}
    except Exception as e:
        print(f"Error fetching coordinates for IP {ip}: {e}")
        return None

def main():
    coordinates_list = []

    # Öffnen Sie die CSV-Datei und lesen Sie die IP-Adressen
    with open(csv_datei, 'r') as file:
        reader = csv.reader(file)
        # Überspringen Sie die Kopfzeile, falls vorhanden
        next(reader)
        # Durchlaufen Sie die Zeilen der CSV-Datei
        for row in reader:
            ip_address = row[3]  # Annahme: Die IP-Adresse befindet sich in der vierten Spalte
            coordinates = print_coordinates(ip_address)
            if coordinates:
                coordinates_list.append(coordinates)

    # Erstellen Sie ein DataFrame aus der Liste der Koordinaten
    df = pd.DataFrame(coordinates_list)

    # Speichern Sie das DataFrame in eine CSV-Datei
    df.to_csv('coordinates.csv', index=False)

    # Anzeigen des DataFrames
    print(df)

if __name__ == "__main__":
    main()