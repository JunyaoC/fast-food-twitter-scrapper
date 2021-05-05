from pymongo import MongoClient
from pprint import pprint
import pandas as pd
from tqdm import tqdm

client = MongoClient("127.0.0.1:27017")

db = client['fastfooddb']

combineDF = pd.read_csv("combine.csv")

dataset = combineDF.to_dict('records')

for record in tqdm(dataset):	
	db['tweet'].insert_one(record)