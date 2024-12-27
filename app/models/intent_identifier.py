import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

'''
class IntentIdentifier:
    def __init__(self, intents_file):
        self.intents = json.load(open(intents_file, 'r'))

    def identify_intent(self, user_input):
        tokens = word_tokenize(user_input)
        tokens = [t for t in tokens if t not in stopwords.words('english')]

        max_match = 0
        intent_name = None

        for intent in self.intents['intents']:
            patterns = intent['patterns']
            for pattern in patterns:
                pattern_tokens = word_tokenize(pattern)
                pattern_tokens = [t for t in pattern_tokens if t not in stopwords.words('english')]
                match = len(set(tokens) & set(pattern_tokens))
                if match > max_match:
                    max_match = match
                    intent_name = intent['name']

        return intent_name
'''


class IntentIdentifier:
    def __init__(self, intents_file):
        # Load intents data from file
        self.intents = self._load_intents(intents_file)

    def _load_intents(self, filepath):
        import json
        with open(filepath, 'r') as file:
            return json.load(file)

    def identify_intent(self, user_input):
        """
        Identify the intent based on tokenized user input.
        """
        if isinstance(user_input, list):
            # Join list into a single string if it was already tokenized
            user_input = " ".join(user_input)
        tokens = word_tokenize(user_input)
        # Logic to identify intent goes here
        # Example: return a dummy intent name for now
        return "default_intent"
