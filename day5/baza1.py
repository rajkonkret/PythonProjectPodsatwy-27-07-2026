# baza danych - system przechowywnia i przetwarzania danch, silnik
# bazy relacyjne i nierelacyjne
# sql, nosql
# MS, oracle, postgres, mysql, db2, terradata,
# docker
# sqlite

import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza danych zostałą podłaczona")
except sqlite3.Error as e:
    print("Błąd:", e)
finally:
    if conn:
        conn.close()
        print('Podłączenie zostało zamknięte')
# Baza danych zostałą podłaczona
# Podłączenie zostało zamknięte

# pgadmin, dbeaver, sqldeveloper, TablePlus, DBBrowser
