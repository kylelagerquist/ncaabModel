import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm





pd.set_option('display.max_columns', 500)

data = pd.read_csv(r"/Users/kylelagerquist/PycharmProjects/NCAAB/ncaaBallGamesUpdated", sep=",")
data_without_na = data.dropna()


features = ["ppg","opp_blk_pg","fg_att_pg","ft_pg","fls_pg","thr_pg","ft_per",
            "fg_per","thr_per","opp_ppg","opp_fg_att_pg","opp_ft_pg","opp_fls_pg","opp_stls_pg",
            "opp_fg_per","opp_thr_per","opp_two_per"]
features = list(set(features))


# # Store the variable we'll be predicting on.
# target = "points"
# # Generate the training set.  Set random_state to be able to replicate results.
# train = data_without_na.sample(frac=0.8, random_state=1)
# # Select anything not in the training set and put it in the testing set.
# test = data_without_na.loc[~data_without_na.index.isin(train.index)]
# # Initialize the model class.
# lin_model = LinearRegression()
# # Fit the model to the training data.
# lin_model.fit(train[features], train[target])
#
# # Generate our predictions for the test set.
# lin_predictions = lin_model.predict(test[features])
# print("Predictions:", lin_predictions)
# # Compute error between our test predictions and the actual values.
# lin_mse = mean_squared_error(lin_predictions, test[target])
# print("Computed error:", lin_mse)
#
# print(len(lin_predictions))
# print(len(test))

X = data_without_na[["ppg","opp_blk_pg","fg_att_pg","ft_pg","fls_pg","thr_pg","ft_per",
            "fg_per","thr_per","opp_ppg","opp_fg_att_pg","opp_ft_pg","opp_fls_pg","opp_stls_pg",
            "opp_fg_per","opp_thr_per","opp_two_per"]]
Y = data_without_na['points']

X = sm.add_constant(X) # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)


