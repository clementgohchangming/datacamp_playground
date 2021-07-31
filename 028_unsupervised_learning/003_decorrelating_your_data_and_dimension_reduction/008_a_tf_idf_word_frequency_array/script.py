# # Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Create a TfidfVectorizer: tfidf
tfidf = TfidfVectorizer()

# Apply fit_transform to document: csr_mat
csr_mat = tfidf.fit_transform(documents)

# scipy.sparse.csr.csr_matrix
# print(type(csr_mat))
# print(csr_mat)

# Print result of toarray() method
print(csr_mat.toarray())
# print(type(csr_mat.toarray()))

# Get the words: words
words = tfidf.get_feature_names()

# Print words
print(words)

