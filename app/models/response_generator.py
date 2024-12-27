'''
import json

class ResponseGenerator:
    def __init__(self, responses_file):
        self.responses = json.load(open(responses_file, 'r'))

    def generate_response(self, intent_name):
        for response in self.responses['responses']:
            if response['name'] == intent_name:
                return response['response']
        return "I'm not sure I understand your question. Can you please rephrase?"
'''

import json

class ResponseGenerator:
    def __init__(self, responses_file):
        self.responses = self._load_responses(responses_file)

    def _load_responses(self, filepath):
        """
        Load responses from a JSON file.
        """
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: The responses file contains invalid JSON.")
            return {}

    def generate_response(self, intent_name):
        """
        Generate a response based on the identified intent.
        """
        return self.responses.get(intent_name, "I'm sorry, I didn't understand that.")
