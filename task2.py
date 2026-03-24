import pandas as pd

df0 = pd.read_csv(".\data\daily_sales_data_0.csv")
df1 = pd.read_csv(".\data\daily_sales_data_1.csv")
df2 = pd.read_csv(".\data\daily_sales_data_2.csv")

final_df = pd.concat([df0,df1,df2],axis=0)
transformed_df = final_df[final_df["product"]=="pink morsel"].copy()
transformed_df["price"] = transformed_df["price"].str.replace(r'[^\d.]','',regex=True).astype(float)
transformed_df["sales"] = transformed_df["price"] * transformed_df["quantity"]
transformed_df = transformed_df.drop(columns=["price","quantity"])
transformed_df = transformed_df[["sales","date","region"]]
transformed_df.rename(columns={"sales" : "Sales", "date" : "Date", "region" : "Region"},inplace=True)
transformed_df.to_csv('task2.csv', index=False)