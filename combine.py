import os
import pandas as pd
from os import walk

_, _, filenames = next(walk('datasets'))

mergeDF = pd.DataFrame()

os.chdir('datasets')

for file in filenames:
	bufferDF = pd.read_csv(file)
	bufferDF['account'] = file.split('.')[0]
	mergeDF = mergeDF.append(bufferDF, ignore_index=True)

os.chdir('..')
mergeDF.to_csv("combine.csv")