import csv
from pathlib import Path
import sys

import spacy

# We exclude the following components as we do not need them. 
nlp = spacy.load('zh_core_web_sm', exclude=['parser', 'ner'])
# Load the Chinese PyMUSAS rule based tagger in a separate spaCy pipeline
chinese_tagger_pipeline = spacy.load('cmn_dual_upos2usas_contextual')
# Adds the Chinese PyMUSAS rule based tagger to the main spaCy pipeline
nlp.add_pipe('pymusas_rule_based_tagger', source=chinese_tagger_pipeline)

# Get the input file from the first command line argument
input_file = Path(sys.argv[1]).resolve()
# Get the output file from the second command line argument
output_file = Path(sys.argv[2]).resolve()

# Open the text file
with input_file.open('r', encoding='utf-8') as input_fp:
    # Read in the text file
    input_text = input_fp.read()
    # Process the text using the spaCy pipeline
    output_doc = nlp(input_text)
    
    # Open the output TSV file
    with output_file.open('w', encoding='utf-8', newline='') as output_fp:
        # Specify the field names of the TSV file
        fieldnames = ['Token Index', 'MWE', 'MWE Start', 'MWE End',
                      'Token', 'POS', 'USAS']
        # Create a TSV writer
        tsv_writer = csv.DictWriter(output_fp, fieldnames=fieldnames,
                                    delimiter='\t')
        # Write the field names to the TSV file
        tsv_writer.writeheader()
        # For each token processed write the relevant information to the
        # TSV file
        for token in output_doc:
            mwe_start, mwe_end = token._.pymusas_mwe_indexes[0]
            is_mwe = False
            if (mwe_end - mwe_start) > 1:
                is_mwe = True
            
            tsv_writer.writerow({'Token Index': token.i,
                                  'MWE': is_mwe,
                                  'MWE Start': mwe_start,
                                  'MWE End': mwe_end,
                                  'Token': token.text,
                                  'POS': token.pos_,
                                  'USAS': token._.pymusas_tags,
                                 })
