import gender_guesser.detector as gender
import pandas as pd
import re

df = pd.read_csv('filtered_titlemeta.tsv', sep='\t', encoding='utf-8')

detector = gender.Detector()