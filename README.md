CLTK Latin sentence tokenizer
=============================

Training sets and and sentence tokenizer for the Latin language, for use with [Classical Language Toolkit](https://github.com/kylepjohnson/cltk).

For instructions on making a new sentence trainer, see [instructions in the CLTK docs](http://docs.cltk.org/en/latest/classical_latin.html#sentence-tokenization).

Contents
--------

`latin.pickle`: the actual sentence tokenizer

`latin.tar.gz`: this is `latin.pickle` compressed and what is fetched by the cltk corpus importer

`models/`: original texts and training sentences

`sentence_tokenizer.py`: a script which generates `latin.pickle`

`tokenized_output.txt`: example output from the trainer.

`training_sentences.txt`: the combined output of the training sentences in `models`

`transformer.py`: a quick and dirty script with which I cleaned up Cicero's *Catalinarians* (12,236 words) into `training_sentences.txt`. In it, each sentences starts a new line


