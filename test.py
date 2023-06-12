import requests
from gensim import models
fasttext_model = models.fasttext.load_facebook_model(r'D:\fasttext\cc.en.300.bin.gz')
arr = ['dog', 'puppy', 'golden retrieve']
synonyms = {}

for a in arr:
# fasttext cosine similarity synonyms search, step 3
#     most_similarity = -1
#     for i in mood_list:
#         if most_similarity < fasttext_model.wv.similarity(mood_val, i):
#             most_similarity = fasttext_model.wv.similarity(mood_val, i)
#             result['moods'] = i