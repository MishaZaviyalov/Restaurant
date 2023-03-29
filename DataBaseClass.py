import pyodbc

def Con():
    Server_Name = r'DESKTOP-GSTE41V\MPTSERVER'
    Data_Base = 'Restaurant_Database'
    username = 'sa'
    password = '123'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + Server_Name + ';DATABASE=' + Data_Base + ';UID=' + username + ';PWD=' + password + ';Trusted_Connection=no;')
    return connection


# Строка возвращает списка кортежа item[0].Login
def Read(query: str):
    cursor = Con().cursor()
    cursor.execute(query)
    CollectionInfo = cursor.fetchall()
    Con().close()
    return CollectionInfo


def Write(query: str):
    cursor = Con().cursor()
    cursor.execute(query)
    cursor.commit()
    cursor.close()
    Con().close()
