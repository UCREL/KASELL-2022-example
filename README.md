# KASELL-2022-example

Example code for the presentation given at KASELL 2022. All of the example code assumes you want to tokenise, Part Of Speech tag, and Semantic tag with USAS tags Chinese text with the [spaCy small Chinese pipeline](https://spacy.io/models/zh#zh_core_web_sm) and the [Chinese PyMUSAS model](https://ucrel.github.io/pymusas/usage/how_to/tag_text#chinese). The spaCy pipeline tokenises and POS tags and the Chinese PyMUSAS model semantic tags the text. The PyMUSAS model in all examples is added to the spaCy pipeline as the PyMUSAS model is itself a spaCy extension.


## Install

Can be installed on all operating systems and supports Python version >=`3.7`, to install the relevant python requirements, spaCy small Chinese pipeline, and the Chinese PyMUSAS model:

``` bash
pip install -r requirements.txt
```

## Tagging Text from a file and outputting tagged text to TSV file

The [tag_text_from_file.py](./tag_text_from_file.py) Python script takes as input two command line arguments:

* `INPUT_FILE` -- File path to an input text file. Text should be in Chinese.
* `OUTPUT_TSV_FILE` -- File path to a TSV file that you would like the tagged data to be stored.

It will open and tag the text data stored at `INPUT_FILE` and output the tagged data in TSV format to the `OUTPUT_TSV_FILE`. The TSV file will contain the following fields:

* `Token Index` -- Index of the token.
* `MWE` -- Whether the token is part of a Multi Word Expression.
* `MWE Start` -- The start token index of the MWE.
* `MWE End` -- The end token index of the MWE.
* `Token` -- The token text.
* `POS` -- Part Of Speech (POS) tag of the token.
* `USAS` -- A list of USAS tags of the token, whereby the first USAS tag in the list is the most likely USAS tag.

We have an example text file within this repository, the same example file used in KASELL 2022 presentation, [input_file.txt](./input_file.txt) to tag this file and output the tagged data to `output_file.tsv`, run the following:

``` bash
python tag_text_from_file.py input_file.txt output_file.tsv
```

<details>

<summary>The `output_file.tsv` should contain the following:</summary>

``` tsv
Token Index	MWE	MWE Start	MWE End	Token	POS	USAS
0	False	0	1	截至	ADP	['Z99']
1	False	1	2	2016年	NOUN	['Z99']
2	False	2	3	4月	NOUN	['Z99']
3	False	3	4	，	PUNCT	['PUNCT']
4	True	4	8	国际	NOUN	['Z3']
5	True	4	8	货币	NOUN	['Z3']
6	True	4	8	基金	NOUN	['Z3']
7	True	4	8	组织	NOUN	['Z3']
8	False	8	9	共有	VERB	['N5', 'S1.1.2+', 'S5+', 'N1%', 'S5+c']
9	False	9	10	190	NUM	['N1']
10	False	10	11	个	NUM	['S2mf']
11	False	11	12	成员国	NOUN	['Z99']
12	False	12	13	（	PUNCT	['PUNCT']
13	False	13	14	包括	VERB	['A1.8+', 'A1.7+', 'N2', 'A11.1+', 'Q1.1/A1.6', 'X2.5+']
14	False	14	15	科索沃	PROPN	['Z99']
15	False	15	16	）	PUNCT	['PUNCT']
16	False	16	17	，	PUNCT	['PUNCT']
17	False	17	18	4	NUM	['N1']
18	False	18	19	个	NUM	['S2mf']
19	False	19	20	联合国	PROPN	['Z99']
20	False	20	21	会员国	NOUN	['Z99']
21	False	21	22	迄今	ADV	['M6', 'A2.2', 'N4', 'T1.1.1', 'T1.1.2']
22	False	22	23	仍	ADV	['C1', 'F2/O2', 'E3+/A2.1', 'E6+', 'M8', 'E3+', 'O4.5', 'T1.1.2', 'T2++', 'Z4']
23	False	23	24	未	ADV	['Z6']
24	False	24	25	加入	VERB	['A2.2', 'S5+', 'A1.8+', 'A1.1.1', 'H2', 'S1.1.1', 'Q4.3', 'S1.1.3+', 'T3-', 'N5+/A2.1', 'N2', 'O2', 'Q4.2/I2.2', 'A9-/I1', 'I2.2/I1', 'A2.1+', 'S7.4+', 'S7.1+']
25	False	25	26	：	PUNCT	['PUNCT']
26	False	26	27	古巴	PROPN	['Z2', 'Z2/S2mf']
27	False	27	28	、	PUNCT	['PUNCT']
28	False	28	29	朝鲜	PROPN	['Z2']
29	False	29	30	、	PUNCT	['PUNCT']
30	False	30	31	列支敦士登	PROPN	['Z99']
31	False	31	32	、	PUNCT	['PUNCT']
32	False	32	33	摩纳哥	PROPN	['Z2']
33	False	33	34	。	PUNCT	['PUNCT']
```

</details>