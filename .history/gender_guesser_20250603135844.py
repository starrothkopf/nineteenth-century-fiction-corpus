import gender_guesser.detector as gender
import pandas as pd

df = pd.read_csv('filtered_titlemeta.tsv', sep='\t', encoding='utf-8')