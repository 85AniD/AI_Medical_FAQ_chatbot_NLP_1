import sys
sys.path.insert(0, '../')

import nltk
nltk.download('punkt')

from models.intent_identifier import IntentIdentifier
from models.response_generator import ResponseGenerator
from utils.nlp_utils import tokenize_input


from db.database import Database

# Create a database object
db = Database()

# Connect to the database
db.connect()

# Create tables in the database
db.create_tables()

# Seed data into the database
db.seed_data()

# Retrieve data from the database
rows = db.retrieve_data('medical_faq')
for row in rows:
    print(row)

# Close the database connection
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
    main()
