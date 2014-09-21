CLTK Latin sentence tokenizer
=============================

About
-----
This repository contains a training set and rule set for tokenizing sentences for Latin, for use with the [Classical Language Toolkit](https://github.com/kylepjohnson/cltk). Unless you want to create a new training set for Latin sentences, there is nothing you need from this repository.

To tokenize Latin sentences with the CLTK, first [import it and use according to the docs here](http://docs.cltk.org/en/latest/import_corpora.html#cltk-sentence-tokenizer-latin) and then see [instructions on tokenizing Latin sentences](http://docs.cltk.org/en/latest/classical_latin.html#sentence-tokenization).

`training_sentences.txt` is comprised Cicero's *Catilinarians* and is 12,245.

Use
---

To create a new training set, manually add tokenized sentences (with each sentence starting a new line) to `training_sentences.txt` and run `train_sentence_tokenizer.py`. The script outputs `latin.pickle`. To use this new file, copy it to your local CLTK data directory at `~/cltk_data/compiled/sentence_tokens_latin/`.

```shell
$ python train_sentence_tokenizer.py 
  Abbreviation: [14.0500] m
  Abbreviation: [0.9151] sp
  Abbreviation: [0.3367] kal
  Abbreviation: [47.2641] c
  Abbreviation: [47.2641] l
  Abbreviation: [12.4379] q
  Abbreviation: [1.8303] ti
  Abbreviation: [0.9151] pl
  Abbreviation: [37.3138] p
  Abbreviation: [2.4876] d
  Abbreviation: [0.9151] cn
  Abbreviation: [2.4876] t
  Sent Starter: [60.3538] 'quodsi'
  Sent Starter: [34.5304] 'itaque'
  Sent Starter: [69.1987] 'nam'
  Sent Starter: [35.8925] 'sed'
  Sent Starter: [45.4471] 'nunc'
  Sent Starter: [56.4065] 'etenim'
```

If you think your training set and tokenizer is an improvement over the CLTK's current, please submit a pull request.

LICENSE
-------
This software is, like the rest of the CLTK, licensed under the MIT license (see LICENSE). The texts for the training sentences comes [from the Latin Library](https://github.com/kylepjohnson/corpus_latin_library) and are their copyright now resides in the public domain [explained here](http://thelatinlibrary.com/about.html).
