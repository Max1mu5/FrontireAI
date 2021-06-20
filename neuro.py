import pandas as pd
from sklearn.cluster import KMeans
import sklearn
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer

def prep(line):
  line = line.lower()
  return line

def clst(vec, N):
  tfidf_vect = TfidfVectorizer(preprocessor=prep)
  tfidf = tfidf_vect.fit_transform(vec)
  kmeans = KMeans(n_clusters=N).fit(tfidf)
  return kmeans.labels_

def clst_val(n_class, names, N):
  vec = []
  for _ in range(N):
    vec.append([])
  c = 0
  for i in n_class:
    vec[i].append(names[c])
    c += 1
  return vec

def rec1(vec):
  b = False
  while not b:
    b = True
    for i in range(len(vec)):
      if len(vec[i]) > 70:
        k = int(len(vec[i]) / 2)
        vec.extend(clst_val(clst(vec[i], k), vec[i], k))
        vec.pop(i)
        b = False
  return vec

def main():
  data = pd.read_csv("data.csv", sep=",", error_bad_lines=False)

  c = 0
  for i in range(len(data['tag'])):
    data['tag'][i] += "_" + str(c)
    c += 1

  vec = clst_val(clst(data['tag'], 170), data['tag'], 170)
  vec = rec1(vec)


  values = [0]*len(vec)
  for cla in range(len(vec)):
    for it in vec[cla]:
      c = 0
      for df in data['tag']:
        if it == df: 
          values[cla] += data['cited'][c]
          break
        c += 1

  max_val = [0]*3
  max_val_index = [0]*3
  for cla in range(len(vec)):
    if values[cla] > max_val[0]:
      max_val[2] = max_val[1]
      max_val[1] = max_val[0]
      max_val[0] = values[cla]
      max_val_index[2] = max_val_index[1]
      max_val_index[1] = max_val_index[0]
      max_val_index[0] = cla
    elif values[cla] > max_val[1]:
      max_val[2] = max_val[1]
      max_val[1] = values[cla]
      max_val_index[2] = max_val_index[1]
      max_val_index[1] = cla
    elif values[cla] > max_val[2]:
      max_val[2] = values[cla]
      max_val_index[2] = cla
  

  ans = []
  for k in range(3):
    mx = 0
    name = ''
    for i in vec[max_val_index[k]]:
      c = 0
      for df in data['tag']:
        if i == df: 
          if (data['cited'][c] > mx):
            mx = data['cited'][c]
            name = i
            break
        c += 1
    ans.append(name)
  return ans

