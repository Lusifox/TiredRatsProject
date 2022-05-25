import pickle


F = open('datafile.pkl', 'wb')
D = {1: 'I', 2: 'am', 3: 'Ghoul'}
pickle.dump(D, F)
F.close()

S = open('datafile.pkl', 'rb')
K = pickle.load(S)
print(sorted(K.items(), reverse=True))
S.close()