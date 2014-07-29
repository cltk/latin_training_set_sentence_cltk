CLTK Latin sentence tokenizer
=============================

About
-----

Training sets and and sentence tokenizer for the Latin language, for use with [Classical Language Toolkit](https://github.com/kylepjohnson/cltk). Unless you are a CLTK developer, there is nothing you need from this repository. The main file here is `latin.pickle`, which you [import according to the docs here](http://docs.cltk.org/en/latest/import_corpora.html#cltk-sentence-tokenizer-latin).

The current training set is relatively small (~12K words, of Cicero's *Catilinarians*).

Use
---

For instructions on tokenizing sentences, see [instructions in the CLTK docs](http://docs.cltk.org/en/latest/classical_latin.html#sentence-tokenization).

To create a new training set (steps #1 and 2), do the following within this repository's root directory. Use steps #3 and 4 to test the output.

```python
In [1]: from sentence_tokenizer import train_from_file

In [2]: train_from_file('training_sentences.txt')
  Abbreviation: [47.2533] c
  Abbreviation: [0.9149] sp
  Abbreviation: [1.8298] ti
  Abbreviation: [0.9149] pl
  Abbreviation: [2.4870] d
  Abbreviation: [0.9149] cn
  Abbreviation: [14.0461] m
  Abbreviation: [12.4351] q
  Abbreviation: [2.4870] t
  Abbreviation: [0.3366] kal
  Abbreviation: [47.2533] l
  Abbreviation: [37.3053] p
  Rare Abbrev: fateatur.
  Rare Abbrev: ingravescet.
  Rare Abbrev: ceterorum.
  Sent Starter: [69.1803] 'nam'
  Sent Starter: [34.5212] 'itaque'
  Sent Starter: [56.3912] 'etenim'
  Sent Starter: [35.8697] 'sed'
  Sent Starter: [45.4307] 'nunc'
  Sent Starter: [60.3399] 'quodsi'

In [3]: from sentence_tokenizer import tokenize_sentences

In [4]: tokenize_sentences('models/cat1.txt')
['Quo usque tandem abutere, Catilina, patientia nostra?', 'quam diu etiam furor iste tuus nos eludet?', 'quem ad finem sese effrenata iactabit audacia?', 'Nihilne te nocturnum praesidium Palati, nihil urbis vigiliae, nihil timor populi, nihil concursus bonorum omnium, nihil hic munitissimus habendi senatus locus, nihil horum ora voltusque moverunt?', 'Patere tua consilia non sentis, constrictam iam horum omnium scientia teneri coniurationem tuam non vides?', 'Quid proxima, quid superiore nocte egeris, ubi fueris, quos convocaveris, quid consilii ceperis, quem nostrum ignorare arbitraris?', 'O tempora, o mores! Senatus haec intellegit.', 'Consul videt; hic tamen vivit.', 'Vivit?',]
```

Now that you have a customized `latin.pickle`, you may copy it to your local CLTK data directory at `~/cltk_data/compiled/sentence_tokens_latin/`. If you think your tokenizer is an improvement upon the CLTK's current, please submit a pull request along with the original training set.


Contents
--------

`latin.pickle`: the actual sentence tokenizer

`latin.tar.gz`: this is `latin.pickle` and `training_sentences.txt` compressed; what is fetched by the CLTK corpus importer

`models/`: original texts and training sentences

`sentence_tokenizer.py`: a script which generates `latin.pickle`

`tokenized_output.txt`: example output from the trainer.

`training_sentences.txt`: the combined output of the training sentences in `models`

`transformer.py`: a quick and dirty script with which I cleaned up Cicero's *Catalinarians* (12,236 words) into `training_sentences.txt`. In it, each sentences starts a new line


