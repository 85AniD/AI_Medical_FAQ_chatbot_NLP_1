import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class IntentIdentifier:
    def __init__(self, intents_file):
        self.intents = self._load_intents(intents_file)

    def _load_intents(self, filepath):
        with open(filepath, 'r') as file:
            return json.load(file)["intents"]

    def identify_intent(self, user_input):
        """
        Identify the intent based on user input using pattern matching.
        This method now prioritizes exact matches and keyword matching with scoring.
        """
        user_input = user_input.lower()

        # Dictionary to store score for each intent
        intent_scores = {intent["name"]: 0 for intent in self.intents}

        # First, try exact matching
        for intent in self.intents:
            for pattern in intent["patterns"]:
                if user_input == pattern.lower():
                    return intent["name"]  # If an exact match is found, return immediately

        # If no exact match is found, calculate score based on token overlap
        for intent in self.intents:
            for pattern in intent["patterns"]:
                pattern_tokens = set(word_tokenize(pattern.lower()))
                user_tokens = set(word_tokenize(user_input))

                # Count the number of matching tokens between the input and the pattern
                common_tokens = user_tokens.intersection(pattern_tokens)
                intent_scores[intent["name"]] += len(common_tokens)

        # Find the intent with the highest score
        best_intent = max(intent_scores, key=intent_scores.get)

        # If no matching intent found (score = 0), return default
        if intent_scores[best_intent] == 0:
            return "default"
        
        return best_intent
