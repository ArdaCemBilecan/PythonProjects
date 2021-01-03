import pandas as pd

url = "http://bit.ly/uforeports"

data = pd.read_csv(url)

#print(data)

print(data.columns)

print(data.head(10))


print(data.isnull().head(10)) 
print("\n")
print(data.isnull().sum()) # kaç adet null city var kaç adet colurs null .....  onları verir

print(data[data.City.isnull()]) #şehir bilgisi Null olanları verir

