import os
import psycopg2
from rich.console import Console

console = Console()

def dbConfig():
    try:
        # Get the database URL from the environment variable
        print(os.getenv('DB_USER'))
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT'),
            dbname=os.getenv('DB_NAME')
        )

        return conn

    except Exception as e:
        console.print_exception(show_locals=True)
        return None
