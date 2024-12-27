import sys
import os
sys.path.insert(0, '../')

import nltk
nltk.download('punkt')

from models.intent_identifier import IntentIdentifier
from models.response_generator import ResponseGenerator
from utils.nlp_utils import tokenize_input
from db.database import Database

# Ensure paths for schema and seed data files are correct
SCHEMA_FILE = '../db/schema.sql'
SEED_DATA_FILE = '../db/seed_data.sql'

# Create a database object
db = Database()

def setup_database():
    try:
        # Connect to the database
        db.connect()

        # Create tables in the database using schema
        with open(SCHEMA_FILE, 'r') as schema_file:
            schema_sql = schema_file.read()
            db.execute_script(schema_sql)

        # Seed data into the database
        with open(SEED_DATA_FILE, 'r') as seed_file:
            seed_sql = seed_file.read()
            db.execute_script(seed_sql)

        print("Database setup completed successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}. Ensure the schema and seed files are in the correct path.")
    except Exception as e:
        print(f"An error occurred during database setup: {e}")
    finally:
        db.close_connection()

def display_data():
    try:
        # Connect to the database
        db.connect()

        # Retrieve data from the database
        rows = db.retrieve_data('medical_faq')
        for row in rows:
            print(row)

    except Exception as e:
        print(f"An error occurred while retrieving data: {e}")
    finally:
        db.close_connection()

def main():
    intents_file = '../data/intents.json'
    responses_file = '../data/responses.json'

    intent_identifier = IntentIdentifier(intents_file)
    response_generator = ResponseGenerator(responses_file)

    while True:
        user_input = input("User: ")
        tokens = tokenize_input(user_input)
        intent_name = intent_identifier.identify_intent(tokens)
        response = response_generator.generate_response(intent_name)
        print("Chatbot: ", response)

if __name__ == '__main__':
    # Setup the database
    setup_database()

    # Optionally, display the data
    display_data()

    # Start the chatbot
    main()
