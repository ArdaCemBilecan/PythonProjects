import pandas as pd

url = "http://bit.ly/uforeports"

data = pd.read_csv(url)
data2 = pd.read_csv(url)
print(data.shape)

#data = data.dropna(how="any")  # Satırlarda NAN varsa o tür verileri siler.
#data = data.dropna(how="all") Eğer bütün kolon nan ise siler
data = data.dropna(subset=["City","Colors Reported"],how="any")
# City veya colors reported null ise bunu listeden at demek.
# all olsaydı 2si de nan ise at demek olacaktı
print(data.shape)

print("\n")
print("---------------------------------------------------------")
print("\n")

data2["Shape Reported"].fillna(value="Belirsiz",inplace=True)
# Nan olan verileri Belirsiz olarak değiştir. Bellekte de değişsin mi ? True

print(data2["Shape Reported"].value_counts(dropna=False))

print(data2.shape)   