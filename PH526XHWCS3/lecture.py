import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering

os.chdir("A:\9github\hello-world\PH526XHWCS3")
whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")
whisky.head()
whisky.tail()
whisky.iloc[1:10]
whisky.iloc[5:10, 5:10]
whisky.columns

flavors = whisky.iloc[:, 2:14]
corr_flavors = pd.DataFrame.corr(flavors)
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()
plt.savefig("corr_whisky.pdf")

model = SpectralCoclustering(n_clusters=6,random_state=0)
model.fit(corr_whisky)
model.rows_
np.sum(model.rows_, axis=1)
np.sum(model.rows_, axis=0)
model.row_labels_

whisky["Group"] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.ix[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)

correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
correlations = np.array(correlations)

plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.colorbar()
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.colorbar()
plt.savefig("correlations.pdf")
