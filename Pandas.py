#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[3]:


ser=pd.Series()
ser


# In[4]:


series=pd.Series([23,45,67,234,545])
series


# In[5]:


dataframe=pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]})
dataframe


# In[9]:


dic=pd.DataFrame({'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[22,45,75]})
print(dic)


# In[10]:


dic.dropna()


# In[11]:


dic.dropna(axis=1)


# In[15]:


dic.fillna(value=dic['C'].mean(),inplace=True)


# In[16]:


dic


# In[18]:


data={'Company':['Google','Google','Microsoft','Microsoft','Facebook','Facebook','Google','Google'],
     'Person':['Raghav','Aryan','Rudrapratap','Ramu','Rishab','Ritik','Deepash','Rohit'],
     'Sales':[200,120,540,650,125,780,1223,765],
     'Profit':[50,45,35,85,65,75,223,675]}
data=pd.DataFrame(data)
data


# In[23]:


data.groupby('Company')['Sales'].mean()


# In[24]:


data.groupby('Company')[['Sales','Profit']].sum()


# In[25]:


data.groupby('Company')[['Sales','Profit']].agg(['mean','sum'])


# In[27]:


data.groupby('Company')['Sales'].nlargest(1)


# In[28]:


Class_a=pd.DataFrame({'Math':[34,45,34,69],
                     'English':[57,69,79,88],
                     'Science':[64,89,90,45],
                     'Hindi':[78,98,59,69]},index=['Rudrapratap','Rohit','Raghav','Kritesh'])
Class_a


# In[29]:


Class_b=pd.DataFrame({'Math':[44,47,38,99],
                     'English':[37,49,77,48],
                     'Science':[74,39,70,85],
                     'Hindi':[58,99,69,59]},index=['Ravi','Ram','Rakesh','Keshav'])
Class_b


# In[30]:


Class_c=pd.DataFrame({'Math':[58,55,84,99],
                     'English':[55,69,72,68],
                     'Science':[69,39,92,75],
                     'Hindi':[79,68,59,79]},index=['Shivang','Palash','Palkesh','Anmol'])
Class_c


# In[31]:


Class=pd.concat([Class_a,Class_b,Class_c])
Class


# In[32]:


player_id=pd.DataFrame({'ID':[23,56,75,34,25,98,55],
                       'NAME':['Raghav','Rohit','Shivang','Pyush','Aditya','Anmol','Abhijeet']})
print(player_id)


# In[33]:


player_detail=pd.DataFrame({'ID':[23,56,75,34,25,98,55],
                           'Age':[23,22,13,24,26,21,24],
                           'Country':['INDIA','PAKISTHAN','AFGANISTAN','JAPAN','TOKYO','DUBAI','RUSSIA']})
print(player_detail)


# In[34]:


player=pd.merge(player_id,player_detail,on='ID')


# In[35]:


player


# In[36]:


left=pd.DataFrame({'A':['A0','A1','A2'],
                  'B':['B0','B1','B2']},index=['k0','k1','k2'])
print(left)


# In[37]:


right=pd.DataFrame({'C':['C0','C1','C2'],
                   'D':['D0','D1','D2']},index=['k0','k1','k3'])
print(right)


# In[38]:


left.join(right)


# In[39]:


right.join(left)


# In[40]:


right.join(left,how='outer')


# In[2]:


df=pd.DataFrame({'Dept':[1,2,3,4,5,6,7,8,9,10],
                'Empl_name':['Rajesh','Shankar','Shindu','Akshay','Rudra','Rohit','Shivam','Prashant','Prahar','Shyam'],
                'Salary':[4500,3450,4900,4800,2500,7800,8500,8700,4800,3800]})
print(df)


# In[3]:


def salary_hike(x):
    if x>3000:
        return np.ceil(x+(x*0.30))
    else:
        return np.ceil(x*1.5)


# In[4]:


df['New_salary']=df['Salary'].apply(salary_hike)
df


# In[7]:


df['Inceased_Salary']=df['New_salary']-df['Salary']
df


# In[8]:


print(df['New_salary'].sum())


# In[9]:


print(df.columns)


# In[11]:


df.sort_values(by='New_salary',ascending=False)


# In[12]:


df.drop(columns=['Salary'],axis=1,inplace=True)


# In[13]:


df


# In[14]:


ipl=pd.read_csv("https://raw.githubusercontent.com/training-ml/Files/main/matches.csv")
ipl


# In[16]:


ipl.head()
ipl.tail()
ipl.sample(n=10)


# In[17]:


url=pd.read_html('https://www.basketball-reference.com')
url


# In[18]:


# Data Manuplation


# In[21]:


date_range=pd.date_range('4/12/2022',periods=22,freq='D')
dates=pd.DataFrame(date_range,columns=['Date'])


# In[22]:


dates


# In[25]:


dates['Day']=dates['Date'].dt.day
dates['Month']=dates['Date'].dt.month
dates['year']=dates['Date'].dt.year


# In[26]:


dates


# In[27]:


df=pd.DataFrame({'DATE_TIME':['Jan 1 12:00 am','Jan 2 12:00 am']})
df


# In[28]:


df['Date']=pd.to_datetime(df['DATE_TIME'],format='%b %d %I:%M %p')
df


# In[41]:


raw_data=pd.DataFrame({'First_Name':['RAM','SHYAM',np.nan,'SEETA','RADHA','RAKESH','RADHE'],
                      'Last_Name':['SINGH','TOMAR',np.nan,'SINGH','GUPTA','PAL','KRISHANA'],
                      'Age':[12,32,np.nan,32,34,65,23],
                      'Sex':['M','M',np.nan,'F','F','M','M'],
                      'Unit_1':[45,np.nan,np.nan,56,78,45,78],
                      'Unit_2':[34,np.nan,np.nan,45,98,34,23]})
raw_data


# In[42]:


raw_data.dropna(axis=0)


# In[43]:


raw_data


# In[44]:


raw_data.isna().sum()


# In[45]:


raw_data.notnull().sum()


# In[47]:


raw_data_cleaned=raw_data.dropna(how='all')
raw_data_cleaned


# In[48]:


raw_data['Unit_1']=raw_data['Unit_1'].fillna(raw_data['Unit_1'].mean())
raw_data


# In[53]:


raw_data['Unit_2'].fillna(raw_data.groupby('Sex')['Unit_2'].transform('mean'),inplace=True)
raw_data


# In[54]:


raw_data['Total']=raw_data['Unit_1']+raw_data['Unit_2']
raw_data


# In[55]:


raw=raw_data.fillna(method='bfill')
raw


# In[2]:


raw_data.loc[2]=['HARRY','PORTER',28,'M',45.0,65.0,np.nan]
raw_data


# In[3]:


data={'Company':['Google','Google','Google','Google','Facebook','Facebook','Facebook','Facebook','Amazon','Amazon','Amazon','Amazon'],
      'Project':['1st','1st','2nd','2nd','1st','1st','2nd','2nd','1st','1st','2nd','2nd'],
      'Incharge':['Ram','Radhe','Rohit','Raghav','Suresh','Raman','Rudra','Shivang','Monika','Salabh','Prakhar','Pradeep'],
      'Sales':[59,34,25,67,78,12,98,42,56,90,56,99],
      'Profit':[98,78,45,73,56,99,38,26,45,91,99,34]}
df=pd.DataFrame(data,columns=['Company','Project','Incharge','Sales','Profit'])


# In[4]:


df


# In[9]:


df.set_index(['Company','Project','Incharge'],drop=True,inplace=True)


# In[11]:


df.swaplevel('Company','Project')


# In[13]:


df.sum(level='Company')


# In[15]:


train=pd.read_csv('https://raw.githubusercontent.com/training-ml/Files/main/titanic_train.csv')
train


# In[16]:


train.drop(columns=['Unnamed: 0'],axis=1,inplace=True)


# In[18]:


train['Survived'].unique()


# In[19]:


train['Survived'].replace({0:'Died',1:'Servived'},inplace=True)


# In[20]:


train


# In[21]:


train['Pclass'].unique()


# In[22]:


train['Pclass'].replace({1:'First_class',2:'Second_class',3:'Third_class'},inplace=True)


# In[23]:


train


# In[24]:


pd.crosstab(train['Pclass'],train['Sex'])


# In[25]:


pd.crosstab(train['Survived'],train['Sex'])


# In[26]:


train[train['Age'].isna()]


# In[30]:


missing=train[train.Age.isin([35])]
missing


# In[31]:


train[train.Age.notnull()]


# In[32]:


train[train['Fare']==max(train['Fare'])]


# In[33]:


train[train['Fare']==min(train['Fare'])]


# In[34]:


train[train['Pclass'].isin(['First_class'])&train['Sex'].isin(['male'])]


# In[35]:


matrix=np.matrix('23,45,78;33,21,56;78,57,98;45,34,22')
levels=['Rahul','Radhe','Rakesh','Rudra']
columns=['Age','Weight','Height']


# In[36]:


df=pd.DataFrame(data=matrix,index=levels,columns=columns)
df


# In[39]:


df[['Age','Height']]


# In[40]:


df[df['Height']>57]


# In[41]:


df.loc['Rahul']


# In[42]:


df.iloc[2]


# In[44]:


df.loc['Rudra',['Height','Weight']]


# In[45]:


df['Height']>80


# In[46]:


height1=df['Height']>80
height2=df['Weight']>20


# In[48]:


df[(height1 & height2)]


# In[53]:


df.reset_index(inplace=True)


# In[54]:


df['Proffesion']='Student Teacher Engineer Trainer'.split()


# In[55]:


df


# In[56]:


df.set_index('Proffesion')


# In[79]:


import sqlite3
db=sqlite3.connect('my_testbase.db')
cursor=db.cursor()


# In[81]:


cursor.execute("create table student_detail7(phone_number int primary key,student_name text,enrolled_date int,marks int)")
db.commit


# In[83]:


with open('Students_details.csv','r') as file:
    no_records=0
    for row in file:
        cursor.execute("insert into student_detail7 values(?,?,?,?)",row.split(","))
        db.commit()
        no_records+=1


# In[84]:


print(no_records)


# In[85]:


sql=cursor.execute("select* from student_detail")
for row in sql:
    print(row)


# In[86]:


cursor.description


# In[87]:


cursor.execute("select* from student_detail")
df=pd.DataFrame(sql)
print(df)


# In[88]:


list(df.columns)


# In[89]:


df.columns=[x[0] for x in cursor.description]
df


# In[ ]:




