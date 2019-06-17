# -*- coding: utf-8 -*
#%
#Cross Tab
#%

import pandas as pd
import seaborn as sns

# Define the headers since the data does not have any
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",           "num_doors", "body_style", "drive_wheels", "engine_location",           "wheel_base", "length", "width", "height", "curb_weight",           "engine_type", "num_cylinders", "engine_size", "fuel_system",   "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",  "city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df_raw = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/autos/imports-85.data",    header=None, names=headers, na_values="?" )
df_raw.head()
# Define a list of models that we want to review
models = ["toyota","nissan","mazda", "honda", "mitsubishi", "subaru", "volkswagen", "volvo"]

# Create a copy of the data with only the top 8 manufacturers
df = df_raw[df_raw.make.isin(models)].copy()
df.head()

pd.crosstab(df.make, df.body_style)

pd.crosstab(df.make, df.body_style)
df.pivot_table(index='make', columns='body_style', aggfunc={'body_style':len}, fill_value=0)
pd.crosstab(df.make, df.num_doors, margins=True, margins_name="Total")

pd.crosstab(df.make, [df.body_style, df.drive_wheels])

pd.crosstab([df.make, df.num_doors], [df.body_style, df.drive_wheels],
            rownames=['Auto Manufacturer', "Doors"],
            colnames=['Body Style', "Drive Type"],
            dropna=False)

sns.heatmap(pd.crosstab([df.make, df.num_doors], [df.body_style, df.drive_wheels]),
            cmap="YlGnBu", annot=True, cbar=False)