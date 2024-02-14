import mysql.connector
import pandas as pd
from sklearn.cluster import KMeans

if __name__ == '__main__':
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sic mundus creatus est',
            database='world'
        )
        print("Connection successful!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor = connection.cursor()

    query = "SELECT * FROM country"
    index_col = 'Code'
    df = pd.read_sql_query(query, connection, index_col=index_col)
    df.reset_index(drop=True, inplace=True)
    # print(df.head())
    df = df.dropna(subset=['Population'])
    df = df.dropna(subset=['LifeExpectancy'])
    X = df[['Population', 'LifeExpectancy']]
    labels = KMeans(7, random_state=0).fit_predict(X)
    print(labels)
    df['labels'] = labels
    print(df)
    print(df[['Continent', 'labels']].value_counts())
    df.to_json(r'trash.json')
    cursor.close()
    connection.close()