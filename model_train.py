#import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

#read data from csv
ds=pd.read_csv('/home/SALARY.csv')
#reshape the data 
x=ds['YearsExperience'].values.reshape(-1,1)
y=ds['Salary']

#storing LR object
LR=LinearRegression()
model=LR.fit(x,y)

print("""  ==============================================
           #####  Welcome to Salary Predictor App  ######
                ==================================  \n
                  >>>>>>>>>>>>>>>>>>>>>>>>>>>>
                |   Press 'q' to exit this app   |
                  <<<<<<<<<<<<<<<<<<<<<<<<<<<<  \n  """)
while(True):
  year=input('Enter no of year : ')
  
  if int(s) == 'q' :
     exit()
  year=float(year)
  sal=model.predict([[year]])
  print("Predicted Salary is :", sal , "\n")
