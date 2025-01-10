import pandas as pd
from rich import print as printc
from rich.console import Console
from psycopg2 import sql
from utills.dbConfig import dbConfig

console = Console()

# Load the CSV file to examine its structure and contents
file_path = '/home/m4gici4nh4ck3r/Desktop/GitHub/Route-Fuel-Prices-Calculation-API/auto_entry/fuel-prices-for-be-assessment.csv'
fuel_data = pd.read_csv(file_path)

printc("[green][+] CSV data loaded successfully![/green]")

# Function to insert fuel data into the database
def fuel_data_entry(fuel_data, cursor):
    for index, row in fuel_data.iterrows():
        insert_fuel_query = sql.SQL("""
            INSERT INTO calculator_fuelprice (opis_truckstop_id, truckstop_name, address, city, state, rack_id, retail_price)
            VALUES ({}, {}, {}, {}, {}, {}, {})
        """).format(
            sql.Literal(int(row['OPIS Truckstop ID'])),
            sql.Literal(row['Truckstop Name']),
            sql.Literal(row['Address']),
            sql.Literal(row['City']),
            sql.Literal(row['State']),
            sql.Literal(int(row['Rack ID'])),
            sql.Literal(float(row['Retail Price']))
        )
        cursor.execute(insert_fuel_query)
        printc(f"[cyan][+] Inserted row {index + 1}: {row['Truckstop Name']}[/cyan]")

def config():
    # Create a cursor object
    db = dbConfig()
    cursor = db.cursor()
    printc("[green][+] Insertion Started [/green]")

    try:
        # Insert fuel data
        printc("[green][+] Fuel data insertion started. [/green]")
        fuel_data_entry(fuel_data, cursor)
        printc("[green][+] Fuel data insertion completed. [/green]")

    except Exception as e:
        printc("[red][!] An error occurred while trying to insert data into the database.[/red]")
        console.print_exception(show_locals=True)

    # Commit the changes and close the connection
    db.commit()
    cursor.close()
    db.close()

    printc("[green][+] Insertion Completed and Committed. [/green]")


# Execute the configuration function
if __name__ == "__main__":
    config()
