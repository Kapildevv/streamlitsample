import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.datasets import load_iris
import seaborn as sns



col_names=['a','b','c']
data=pd.DataFrame(np.random.randint(30,size=(30,3)),columns=col_names)

'line graph:'
st.line_chart(data)

'Bar graph:'
st.bar_chart(data)

animals=['Cat','Dog','Cow']
heights=[10,20,30]

'pie chart:'
fig, ax = plt.subplots()
ax.pie(heights,labels=animals)

st.pyplot(fig)

rows=np.random.randn(1,1)
'Growing line chart:'
chart=st.line_chart(rows)
for i in range(1,100):
    new_rows=np.random.randn(1,1)
    chart.add_rows(new_rows)
    time.sleep(0.05) 


values=np.random.randn(10)
'Line chart using matplotlib:'
fig,ax=plt.subplots()
ax.plot(values)
st.pyplot(fig)

'Age Vs Height:'
name=['John','Mary','Sam','Anna','Tom']
age=[23,45,31,22,36 ]      
heights=[5.7,6.0,5.8,5.5,5.9]

fig,ax=plt.subplots()
x=np.arange(len(heights))
width=0.30

ax.bar(x-width/2,width, color='red')
ax.bar(x+width/2,heights,width,color='orange')

ax.legend(['Age','Height'])
ax.set_xticks(x)
ax.set_xticklabels(name)       

st.pyplot(fig)


'Distribution of heights:'
explode = (0.2, 0.1, 0.1, 0.1,0.1)
plot_pie, ax = plt.subplots()
ax.pie(heights, explode=explode, labels=name, autopct='%1.1f%%', shadow=True, startangle=140)
ax.axis('equal')
st.pyplot(plot_pie)


iris_data = load_iris()
data=pd.DataFrame(iris_data.data,columns=iris_data.feature_names)

fig1=plt.figure()
sns.histplot(data=data,bins=20)
st.pyplot(fig1)

fig2=plt.figure()
sns.boxplot(data=data)
st.pyplot(fig2)

fig3=plt.figure()
sns.scatterplot(data=data) 
st.pyplot(fig3)



