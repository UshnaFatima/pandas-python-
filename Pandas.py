import pandas as pd 
dataset=pd.read_csv("Student Data.csv")
print(dataset)

# df=pd.read_csv("C:/Users/Hp/Desktop/python(datascience)/LIBRARIES+MODULE/PANDAS/Student Data.csv")
# print(df) 




# PYTHON DICTIONARIES VS PANDAS
# PYTHON DICTIONARIES
dict={
    "name":["Student1","Student2","Student3","Student4","Student5","Student6"],
    "age":[21,20,20,20,20,20],
    "address":["lahore","karachi","kirachi","lahore","islamabad","karachi"]
}
print("\n",dict)
print("\n",dict.get("address"))
print("\n",dict["name"])

# PANDAS
print("\n",dataset["Name"])
print("\n",dataset["Discrete  math"])




# CREATING PANDAS DATAFRAME FROM DICTIONARY
dict={
    "name":["Student1","Student2","Student3","Student4","Student5","Student6"],
    "age":[21,20,20,20,20,20],
    "address":["lahore","karachi","kirachi","lahore","islamabad","karachi"]
}
df=pd.DataFrame(dict)
print("\n",df)




# CREATING A DATAFRAME FROM A 2-D NUMPY ARRAY
import numpy as np
array=np.random.randint(0,20, size=(4,5))
print("\n Numpy Array: \n",array)

df=pd.DataFrame(array)
print("\n Pandas Array: \n",df)

df=pd.DataFrame(data=array)
print("\n Pandas Array: \n",df)

# Name the columns lables
col_lables=["col1","col2","col3","col4","col5"]
df=pd.DataFrame(data=array,columns=col_lables)
print("\n Pandas Array: \n",df)

# Name the row lables
df=pd.DataFrame(data=array,index=["row1","row2","row3","row4"])
print("\n Pandas Array: \n",df)

row_lables=["row1","row2","row3","row4"]
df=pd.DataFrame(data=array,columns=col_lables,index=row_lables)
print("\n Pandas Array: \n",df)
print("\n", df["col2"])




# CREATING A SERIES FROM PYTHON LIST
series=["ushna","zainab","maham","ruqia","farwa"]
sr=pd.Series(data=series)
print("\n Pandas Series: \n",sr)
print(type(sr))

indices=["N1","N2","N3","N4","N5"]
sr=pd.Series(data=series,index=indices)
print("\n Pandas Series: \n",sr)
print(type(sr))

# NOTE: You can have empty string as an index

print(sr["N1"])

# You can create a series with NaN values, using np.nan, which is IEEE 754 floating point representation of Not a Number. NaN values can act as a placeholder for any missing numerical values in the array.

series2=[1,2,np.nan,5.6]
sr2=pd.Series(data=series2,index=["R1","R2","R3","R4"])
print("\n Pandas Series: \n",sr2)

# NOTE: the dtype of the series object is inferred from the data as float64

series2=[1,2,5,6]
sr2=pd.Series(data=series2,index=["R1","R2","R3","R4"],dtype=np.int16)
print("\n Pandas Series: \n",sr2)

# Optionally, you can assign a name to a series, which becomes attribute of the series object. Moreover, it becomes the column name, if that series object is used to create a Dataframe later

series=["ushna","zainab","maham","ruqia","farwa"]
sr=pd.Series(data=series,index=["R1","R2","R3","R4","R5"],name="maths department")
print("\n Pandas Series With Name: \n",sr)
print(type(sr))




# CREATING A SERIES FROM NUMPY ARRAY
sarr=pd.Series(data=np.arange(5))
print("\n Pandas Series FROM NUMPY ARRAY: \n",sarr)
print(type(sarr))

arr=np.array([1.2,3.4,5.6,7.8,9.10])
sar=pd.Series(data=arr)
print("\n Pandas Series FROM NUMPY ARRAY: \n",sar)
print(type(sar))




# CREATING A SERIES FROM PYTHON DICTIONARY
dict={
    "name": "ushna",
    "department":"maths",
    "age":"21",
    "location":"lahore"
}
dicsr=pd.Series(data=dict)
print("\n PANDAS SERIES FROM PYTHON DICTIONARY: \n",dicsr)

# NOTE: When you create a series from dictionary, it will automatically take the keys as index and the value as data




# CREATING A SERIES FROM SCALAR VALUE
scalar=pd.Series(data=37)
print("\n SCALAR VALUE:",scalar)




# CREATING AN EMPTY SERIES
empty_ser=pd.Series(dtype="float64")
print("\n EMPTY SERIES: \n ",empty_ser)

# NOTE: need to pass "dtype" else we get error




# ATTRIBUTES OF PANDA SERIES
# We can access certain properties called attributes of a series by using that property with the series name using dot  .  notation
mydict={
    0:"name",
    1:"age",
    2:"address",
    3:"street"
}
s=pd.Series(mydict, name="daata")

print(s.name)
print(s.index)
print(s.ndim)
print(s.shape)




# CHANGING INDEX OF A SERIES OBJECT
series2=["ushna","zainab","maham","ruqia","farwa"]
sr=pd.Series(data=series2)
print("\n Pandas Series: \n",sr)
print(sr.index)

sr.index=[10,9,8,7,6]
print("\n Pandas Series: \n",sr)
print(sr.index)




#IDENTIFICATION USING INTEGER INDICES OR BY POSITION
print(sr.loc[10])   # index
print(sr.iloc[2])   # position




# FANCY INDEXING
print(sr[[10,9]])
print(sr.loc[[10,9]])
print(sr.iloc[[1,2]])

# NEGATIVE INDEXING, WORK ONLY FOR ILOC
print(sr.iloc[-1])




# SELECTION/FILTERING/SUBSETTING OF SERIES OBJECT HAVING INTEGER INDICES
print(sr[1:4])         # positional indexing 
print(sr.loc[10:8])    # actual indexing
print(sr.iloc[1:4])    # positional indexing




# UNDERSTANDING STEP WITH SERIES OBJECT HAVING STRING INDICES
print(sr[0:4:2])




# ADDING TWO SERIES OBJECT WITH SAME INTEGER INDICES
list1=[1,2,3,4]
list2=[5,6,7,8]
s1=pd.Series(list1)
s2=pd.Series(list2)

print(s1)
print(s1.index)

print(s2)
print(s2.index)

s3=s1+s2
print(s3)
print(s3.index)




# ADDING TWO SERIES OBJECT HAVING DIFFERENT INTEGER INDICES
index1=[0,1,2,3]
index2=[0,2,3,5]
s4=pd.Series(list1,index=index1)
s5=pd.Series(list2,index=index2)

print(s4)
print(s4.index)

print(s5)
print(s5.index)

s6=s4+s5
print(s6)
print(s6.index)

"""
NOTE
Problem: While performing mathematical operations on series having mismatched indices, all missing values are filled in with NaN by default.
Solution: To handle this problem, instead of using the operators (+, -, *, /), an explicit call to s.add(), s.sub(), s.mul() and s.div() is preferred. 
"""

print(s4.add(s5,fill_value=0))
print(s4.add(s5,fill_value=4))  
