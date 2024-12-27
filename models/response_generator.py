import json

class ResponseGenerator:
    def __init__(self, responses_file):
        self.responses = json.load(open(responses_file, 'r'))

    def generate_response(self, intent_name):
        for response in self.responses['responses']:
            if response['name'] == intent_name:
                return response['response']
        return "I'm not sure I understand your question. Can you please rephrase?"
