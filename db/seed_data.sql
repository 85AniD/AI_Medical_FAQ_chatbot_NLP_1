USE medical_faq_chatbot;

INSERT INTO users (username, email, password, role) VALUES
  ('ani', 'ani@gmail.com', 'ani123', 'user'),
  ('ram', 'ram@gmail.com', 'ram123', 'user'),
  ('admin_user', 'admin@gmail.com', 'admin123', 'admin');

INSERT INTO admins (username, email, password, role) VALUES
  ('admin_user', 'admin@gmail.com', 'admin123', 'admin');

INSERT INTO intents (name, description) VALUES
  ('greeting', 'A greeting intent'),
  ('symptoms', 'A symptoms intent'),
  ('medication', 'A medication intent');

INSERT INTO responses (intent_id, response) VALUES
  (1, 'Hello! How can I assist you today?'),
  (2, 'Sorry to hear that. Can you tell me more about your symptoms?'),
  (3, 'I''m not a doctor, but I can provide general information about medications.');

INSERT INTO user_queries (user_id, query) VALUES
  (1, 'Hello'),
  (2, 'I have a fever'),
  (1, 'What medication should I take?');

INSERT INTO query_responses (user_query_id, response_id) VALUES
  (1, 1),
  (2, 2),
  (3, 3);


  INSERT INTO medical_faq (question, answer) VALUES
    ('What is the treatment for COVID-19?', 'The treatment for COVID-19 is supportive care, which includes rest, hydration, and oxygen therapy.'),
    ('What are the symptoms of COVID-19?', 'The symptoms of COVID-19 include fever, cough, and shortness of breath.'),
    ('How can I prevent COVID-19?', 'You can prevent COVID-19 by washing your hands frequently, wearing a mask, and avoiding close contact with others.');

