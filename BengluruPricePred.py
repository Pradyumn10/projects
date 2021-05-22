#%%
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib
from pandas.io import pickle
matplotlib.rcParams['figure.figsize'] = (20,10)
# %%
df1 = pd.read_csv('bengaluru_house_prices.csv')
# %%
df1
# %%
#EDA
df1.shape
# %%
#Data Cleaning Begins
df1.groupby('area_type')['area_type'].agg('count')
# %%
df1.columns
# %%
df2=df1.drop(['area_type', 'availability', 'society', 'balcony'],axis=1)
# %%
df2
# %%
#null values are very less compared to dataset size. so we remove them
df2.isnull().sum()
# %%
df3=df2.dropna()
# %%
df3.isnull().sum()
# %%
df3.shape
# %%
df3['size'].unique()
# %%
df3['bhk'] = df3['size'].apply(lambda x:int(x.split(' ')[0]))
# %%
df3
# %%
df3['bhk'].unique()
# %%
#finding out error
df3[df3.bhk>20]
#A house iwth 2400sqft cannot have 43 bedroom so thats an error
# %%
df3.total_sqft.unique()
# %%
#finding variations in total sqft column using this function

#is the value is float it will throw except otherwise return true
def is_float(x):
    try:
        float(x)
    except:
        return False 
    return True 
#%%
#looking for value which are not float
df3[~df3['total_sqft'].apply(is_float)].head(10)
# %%
#tackling the range values which will return avg value
def convert_sqft_to_num(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None
# %%
convert_sqft_to_num('2166')
# %%
convert_sqft_to_num('2100-2850')
# %%
df4 = df3.copy()
# %%
df4['total_sqft'] = df4['total_sqft'].apply(convert_sqft_to_num)
# %%
df4
# %%
df4.loc[30]
# %%
#Feature Engineering 
df5 = df4.copy()
# %%
df5['price_per_sqft'] = df5['price']*100000/df5['total_sqft']
# %%
df5
# %%
len(df5['location'].unique())
#we have lot of location which is a lot of data - if we keep all 
# locations we will have 1304 columns which is called as dimensionality 
# curse or high dimensional problem
# %%
#to solve this we will find other category
df5['location'] = df5['location'].apply(lambda x: x.strip())
#df5.location = df5.location.apply(lambda x: x.strip())
#%%
location_stats = df5.groupby('location')['location'].agg('count').sort_values(ascending=False)
location_stats
# %%
location_stats.head(50)
# %%
len(location_stats[location_stats<=10])
# %%
location_stats_less_than_10 = location_stats[location_stats<=10]
location_stats_less_than_10
# %%
len(df5.location.unique())
# %%
#if the location occurance is less than 10 we will replace that 
# name with other
df5.location = df5.location.apply(lambda x: 'other' if x in location_stats_less_than_10 else x)
# %%
len(df5.location.unique())
# %%
df5
# %%
#Outlier Removal
#A typical area for 1 bedroom is 300-400 sqft
df5[df5.total_sqft/df5.bhk<300].head()
#Removing outlier which have sqft less than 300
# %%
df5.shape
# %%
df6 = df5[~(df5.total_sqft/df5.bhk<300)]
# %%
#removed some basic outlier
df6.shape
# %%
df6.price_per_sqft.describe()
# %%
def remove_pps_outlier(df):
    df_out= pd.DataFrame()
    for key, subdf in df.groupby('location'):
        m=np.mean(subdf.price_per_sqft)
        st=np.std(subdf.price_per_sqft)
        reduced_df = subdf[(subdf.price_per_sqft>(m-st)) & (subdf.price_per_sqft<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out
#%%
df7 = remove_pps_outlier(df6)
df7.shape
#removed more outlier
# %%
def plot_scatter_chart(df,location):
    bhk2 = df[(df.location==location) & (df.bhk == 2)]
    bhk3 = df[(df.location==location) & (df.bhk == 3)]
    matplotlib.rcParams['figure.figsize'] =(15,10)
    plt.scatter(bhk2.total_sqft, bhk2.price, color='blue',label='2BHK',s=50)
    plt.scatter(bhk3.total_sqft, bhk3.price,marker='+', color='green', label='3BHK',s=50)
    plt.xlabel('Total Square Feet Area')
    plt.ylabel('Price')
    plt.title(location)
    plt.legend()
# %%
plot_scatter_chart(df7,'Rajaji Nagar')
# %%
plot_scatter_chart(df7,'Hebbal')
# %%
#at some places we have 2BHK value more than 3BHK value
#handling those kind of data
def remove_bhk_outlier(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby('location'):
        bhk_stats={}
        for bhk,bhk_df in location_df.groupby('bhk'):
            bhk_stats[bhk] = {
                'mean' : np.mean(bhk_df.price_per_sqft),
                'std' : np.std(bhk_df.price_per_sqft),
                'count' : bhk_df.shape[0]
            }
        for bhk, bhk_df in location_df.groupby('bhk'):
            stats = bhk_stats.get(bhk-1)
            if stats and stats['count']>5:
                exclude_indices = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
            
    return df.drop(exclude_indices, axis='index')
# %%
df8 = remove_bhk_outlier(df7)
# %%
df8.shape
# %%
plot_scatter_chart(df8,'Rajaji Nagar')
# %%
plot_scatter_chart(df8,'Hebbal')
# %%
import matplotlib
matplotlib.rcParams['figure.figsize'] = (20,10)
plt.hist(df8.price_per_sqft, rwidth=0.8)
plt.xlabel("Price Per Square Feet")
plt.ylabel('Count')
# %%
#it looks like a normal/ gaussian distribution
df8.bath.unique()
# %%
df8[df8.bath>10]
# %%
#removing outlier which will have bathroom more than bhk
plt.hist(df8.bath, rwidth=0.8)
plt.xlabel('Number of Bathroom')
plt.ylabel("Count")
# %%
df8[df8.bath>df8.bhk+2]
# %%
df9 = df8[df8.bath<df8.bhk+2]
# %%
df9.shape
# %%
#dropping feature for model
df10 = df9.drop(['size','price_per_sqft'],axis=1)
# %%
df10.head()
# %%
#Model Building
dummies = pd.get_dummies(df10.location)
# %%
df11 = pd.concat([df10,dummies.drop('other',axis=1)],axis=1)
# %%
df11
# %%
df12 = df11.drop('location',axis=1)
# %%
df12
# %%
#the df number is also the number of pipeline
X=df12.drop('price',axis=1)
y=df12['price']
# %%
X
# %%
y
# %%
from sklearn.model_selection import train_test_split as tts 
X_train, X_test, y_train, y_test = tts(X,y,test_size=0.2, random_state=10)
# %%
from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
# %%
model1.fit(X_train,y_train)
# %%
model1.score(X_test,y_test)
# %%
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
# %%
cv = ShuffleSplit(n_splits=5,test_size=0.2,random_state=0)
cross_val_score(LinearRegression(),X,y,cv=cv)
#Almost all the 5 splits are giving more than 80% accuracy
# %%
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
# %%
#finding the best parameter and model
#hyper parameter tuning
def find_best_model_using_GridSearch(X,y):
    algos = {
        'linear_regression' : {
            'model':LinearRegression(),
            'params':{
                'normalize' : [True,False]
            }
        },
        'lasso':{
            'model':Lasso(),
            'params':{
                'alpha':[1,2],
                'selection':['random','cyclic']
            }
        },
        'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params':{
                'criterion':['mse','friedman_mse'],
                'splitter':['best','random']
            }
        }
    }

    scores=[]
    cv= ShuffleSplit(n_splits=5,test_size=0.2,random_state=0)
    for algo_name , config in algos.items():
        gs = GridSearchCV(config['model'],config['params'],cv=cv,return_train_score=False)
        gs.fit(X,y)
        scores.append({
            'model':algo_name,
            'best_score':gs.best_score_,
            'best_params':gs.best_params_
        })
    return pd.DataFrame(scores,columns=['model','best_score','best_params'])
#%%
find_best_model_using_GridSearch(X,y) 
#best is linear regression
#we have already created the model through linear regression only
#%%
X.columns
#%%
np.where(X.columns=='Vishwapriya Layout')[0][0]
#it gives location number of that column
# %%
#creating predict function
def predict_price(location,sqft,bath,bhk):
    loc_index = np.where(X.columns==location)[0][0]
    x=np.zeros(len(X.columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk 
    if loc_index>=0:
        x[loc_index]=1
    return model1.predict([x])[0]
# %%
predict_price('1st Block Jayanagar',1000,3,3)
# %%
predict_price('1st Phase JP Nagar',1000,2,3)
# %%
import pickle
# %%
with open('bangluru_home_price_model.pickle','wb') as f:
    pickle.dump(model1,f)
# %%
import json
columns = {
    'data_columns' : [col.lower() for col in X.columns]   
}
with open('columns.json','w') as f:
    f.write(json.dumps(columns))
# %%
