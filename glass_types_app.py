import streamlit as st 
import pandas as pd 
import numpy as np 
from sklearn.svm import SVC 
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split 

@st.cache()
def load_data():
	file_path = "glass-types.csv"
    df = pd.read_csv(file_path, header = None)
    # Dropping the 0th column as it contains only the serial numbers.
    df.drop(columns = 0, inplace = True)
    column_headers = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'GlassType']
    columns_dict = {}
    # Renaming columns with suitable column headers.
    for i in df.columns:
        columns_dict[i] = column_headers[i - 1]
        # Rename the columns.
        df.rename(columns_dict, axis = 1, inplace = True)
    return df

glass_df = load_data() 

# Creating the features data-frame holding all the columns except the last column.
X = glass_df.iloc[:, :-1]

# Creating the target series that holds last column.
y = glass_df['GlassType']

# Spliting the data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

features_cols = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
@st.cache()
def prediction(model ,feat_column):
	glass_type = model.predict([feat_column])
	glass_type = glass_type[0]
	if glass_type==1:
		return "building windows float processed"
	elif glass_type==2:
		return "building windows non float processed"
	elif glass_type == 3:
		return "vehicle windows float processed"
	elif glass_type == 5:
		return "containers"
	elif glass_type == 6:
		return "tableware"

	else :
		return "headlamp"


st.title('glass type prediction app')
st.sidebar.title('glass type app')


