# -*- coding: utf-8 -*-
import pandas as pd

data =[10,20,30,40,"Arda"]

df = pd.DataFrame(data)
print(df)

print("-------------------------------")
data2 = [["Arda","Eskişehir",21],["Rana","Brno",26],["Oğuz","Sivas",23]]
# Colomları isimlendirme ve indexleri şekillendirme
df1 = pd.DataFrame(data2,columns=(["İsim","Şehir","Yaş"]),index=[1,2,3])
print(df1)

print("-------------------------------")

data3 = {"İsim":["Arda","Simay","Batu"],
         "Yaş":[21,22,21],
         "Şehir":["Eskişehir","Mersin","Edirne"]}

df2 = pd.DataFrame(data3)
print(df2)
print("-------------------------------")
#del df2["Yaş"]   Yaş kolonunu siler
#df2.pop("Yaş")  # Yaş kolonunu siler

print(df2.loc[2]) # 2 numarılı kayıtta kim varsa onu getir demek (indexler 0dan başlamıyorsa veya idler 1002 gibi olursa)

print(df2.iloc[1]) # Bu ise 1. indexte kim var onu getir demek
print("-------------------------------")
df3 = df2.append(df1) 
print(df3)
