from chatterbot import ChatBot

chatbot = ChatBot(
    'A3S-Bot',read_only =True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors =['chatterbot.preprocessors.clean_whitespace'],
    filters = ['chatterbot.filters.RepetitiveResponseFilter'], 
    logic_adapters=[
        # 'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
# training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

#training_data = training_data_quesans + training_data_personal
training_data = training_data_quesans

trainer.train(training_data)

# Training With Corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

trainer_corpus.train(
    'chatterbot.corpus.english'
)
