# Databricks notebook source
import pandas as pd
df=pd.read_csv("/Workspace/Users/priyanshbobade@gmail.com/Spotify Analytics/track_data_final.csv")


# COMMAND ----------

df.shape

# COMMAND ----------

df.columns.tolist()

# COMMAND ----------

df.info()


# COMMAND ----------

df.head()

# COMMAND ----------

df.sample(5,random_state=42)

# COMMAND ----------

df.isnull().sum().sort_values(ascending=False)

# COMMAND ----------

df.duplicated().sum()

# COMMAND ----------

df.describe()
df.describe(include="object")

# COMMAND ----------

for col in df.columns:
    print(f"{col}: {df[col].nunique()}")


# COMMAND ----------

df.dtypes

# COMMAND ----------

df[df.isnull().any(axis=1)]


##This shows the rows having one minimum NULL value. These rows constitue 6 (0.068%) of our 8778 rows
##Hence these rows can be dropped without significant loss of data. 

# COMMAND ----------

# DBTITLE 1,Cleaned Dataset
df_clean=df.dropna().copy()

df_clean.shape


# COMMAND ----------

df_clean.isnull().sum()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS spotify_bronze;
# MAGIC
# MAGIC CREATE DATABASE IF NOT EXISTS spotify_silver;
# MAGIC
# MAGIC CREATE DATABASE IF NOT EXISTS spotify_gold;

# COMMAND ----------

# MAGIC %sql
# MAGIC show databases