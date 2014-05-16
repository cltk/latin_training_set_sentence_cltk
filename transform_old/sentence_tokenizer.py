#import nltk
from nltk.tokenize.punkt import PunktLanguageVars
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize.punkt import PunktTrainer
import os

def train_from_file(training_file):
    language_punkt_vars = PunktLanguageVars
    language_punkt_vars.sent_end_chars=('.', '?', ';', ':')
    with open(training_file) as f:
        train_data = f.read()
    trainer = PunktTrainer(train_data, language_punkt_vars)
    with open('latin.txt', 'w') as f:
        f.write(trainer)
    print(trainer)

def tokenize_sentences(input_file):
    with open('latin.txt') as f:
        train_data = f.read()
    language_punkt_vars = PunktLanguageVars
    trainer = PunktTrainer(train_data, language_punkt_vars)
    params = trainer.get_params()
    sbd = PunktSentenceTokenizer(params)
    with open(input_file) as f:
        to_be_tokenized = f.read()
    tokenenized_sentences = []
    for sentence in sbd.sentences_from_text(to_be_tokenized, realign_boundaries=True):
        tokenenized_sentences.append(sentence)
    file_output_name = 'sentences_tokenized_' + input_file
    with open(file_output_name, 'w') as f:
        f.write(str(tokenenized_sentences))
    print(tokenenized_sentences)