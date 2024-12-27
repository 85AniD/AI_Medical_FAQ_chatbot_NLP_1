import sys
import os
import json
import nltk
from nltk.tokenize import word_tokenize

sys.path.insert(0, '../')
nltk.download('punkt')

from db.database import Database

# Ensure paths for schema and seed data files are correct
SCHEMA_FILE = '../db/schema.sql'
SEED_DATA_FILE = '../db/seed_data.sql'

# Create a database object
db = Database()

def setup_database():
    """
    Set up the database by creating tables and seeding data.
    """
    try:
        db.connect()

        with open(SCHEMA_FILE, 'r') as schema_file:
            schema_sql = schema_file.read()
            db.execute_script(schema_sql)

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
    """
    Display data from the 'medical_faq' table.
    """
    try:
        db.connect()
        rows = db.retrieve_data('medical_faq')
        for row in rows:
            print(row)

    except Exception as e:
        print(f"An error occurred while retrieving data: {e}")
    finally:
        db.close_connection()

class IntentIdentifier:
    def __init__(self, intents_file):
        self.intents = self._load_intents(intents_file)

    def _load_intents(self, filepath):
        with open(filepath, 'r') as file:
            return json.load(file)["intents"]

    def identify_intent(self, user_input):
        """
        Identify the intent based on user input using pattern matching.
        """
        tokens = word_tokenize(user_input.lower())
        for intent in self.intents:
            for pattern in intent["patterns"]:
                pattern_tokens = word_tokenize(pattern.lower())
                if set(tokens).intersection(pattern_tokens):
                    return intent["name"]
        return "default"

class ResponseGenerator:
    def __init__(self, responses_file):
        self.responses = self._load_responses(responses_file)

    def _load_responses(self, filepath):
        with open(filepath, 'r') as file:
            return json.load(file)["responses"]

    def generate_response(self, intent_name):
        """
        Generate a response based on the identified intent.
        """
        for response in self.responses:
            if response["name"] == intent_name:
                return response["response"]
        return "I'm sorry, I didn't understand that."

def main():
    intents_file = '../data/intents.json'
    responses_file = '../data/responses.json'

    intent_identifier = IntentIdentifier(intents_file)
    response_generator = ResponseGenerator(responses_file)

    while True:
        user_input = input("User: ")
        try:
            # Identify intent
            intent_name = intent_identifier.identify_intent(user_input)
            print(f"Debug: Identified intent - {intent_name}")

            # Generate response
            response = response_generator.generate_response(intent_name)
            print(f"Debug: Generated response - {response}")

            # Output chatbot response
            print("Chatbot:", response)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Setup the database
    print("Setting up the database...")
    setup_database()

    # Optionally, display the data
    print("\nDisplaying data from the database...")
    display_data()

    # Start the chatbot
    print("\nStarting the chatbot...")
    main()
