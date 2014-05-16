CLTK Latin sentence tokenizer
=============================

Training sets and tokenizer for the Latin language, for use with [Classical Language Toolkit](https://github.com/kylepjohnson/cltk).

`transformer.py` is a quick and dirty script with which I cleaned up Cicero's *Catalinarians* (12,236 words) into `training_sentences.txt`. In it, each sentences starts a new line.

The actual tokenizer, when in use, is currently erring out at line 586 of `nltk/tokenize/punkt.py` with: `AttributeError: 'PunktTrainer' object has no attribute 'split'`.