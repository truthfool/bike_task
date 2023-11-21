import pandas as pd
from sqlalchemy import create_engine,text

def read_data(file_path):
    # Read the CSV or Excel file
    return pd.read_csv(file_path)  # For Excel, use pd.read_excel()

def change_data_types(df):
    # Change data types and check memory usage
    initial_memory = df.memory_usage().sum()

    # Convert columns to appropriate data types
    df['bike_name'] = df['bike_name'].astype(str)
    df['price'] = df['price'].astype(float)
    df['city'] = df['city'].astype(str)
    df['kms_driven'] = df['kms_driven'].astype(float)
    df['owner'] = df['owner'].astype(str)
    df['age'] = df['age'].astype(int)
    df['power'] = df['power'].astype(float)
    df['brand'] = df['brand'].astype(str)

    final_memory = df.memory_usage().sum()

    print(f"Memory usage before: {initial_memory / (1024 ** 2):.2f} MB")
    print(f"Memory usage after: {final_memory / (1024 ** 2):.2f} MB")

    return df

def connect_to_mysql(username, password, database_name,hostname):
    # Connect to MySQL database
    return create_engine(f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}')

def delete_existing_index(engine, table_name, index_name):
    # Delete existing index
    with engine.connect() as connection:
        stmt = text(f'DROP INDEX IF EXISTS {index_name} ON {table_name}')
        connection.execute(stmt)

def insert_data_into_mysql(df, engine, table_name):
    # Insert data into MySQL
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def create_index(engine, table_name, index_name):
    # Create index after data insertion
    with engine.connect() as connection:
        connection.execute(f'CREATE INDEX {index_name} ON {table_name}(bike_name)')

def main():
    # Step 1: Read the CSV or Excel file
    file_path = 'used_bikes.csv'  # Replace with your file path
    df = read_data(file_path)

    # Step 2: Change data types and check memory usage
    df = change_data_types(df)

    # Step 3: Dump data into MySQL database
    # Input your MySQL connection details
    username = input("Enter your MySQL username: ")
    password = input("Enter your MySQL password: ")
    database_name = input("Enter your MySQL database name: ")
    table_name = input("Enter your table name: ")
    index_name = input("Enter your index name: ")
    hostname = input("Enter host name: ")

    engine = connect_to_mysql(username, password, database_name,hostname)

    # Step 4: Delete existing index
    # delete_existing_index(engine, table_name, index_name)

    # Step 5: Insert data into MySQL
    insert_data_into_mysql(df, engine, table_name)

    # Step 6: Create index after data insertion
    # create_index(engine, table_name, index_name)

    # Close the database connection
    engine.dispose()

if __name__ == "__main__":
    main()
