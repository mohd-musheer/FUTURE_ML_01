import joblib

model=joblib.load('sales_predict.pkl')
date=[[2015,10,26]]
sales=model.predict(date)
print(f'Total Sales at {date} is : {round(sales[0],2)} $ ')