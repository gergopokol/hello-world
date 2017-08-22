numeric_data = (numeric_data - np.mean(numeric_data)) / np.std(numeric_data)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit(numeric_data).transform(numeric_data)