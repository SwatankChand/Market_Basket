



####################### MARKET  BASKET ANALYSIS###########################


# importing neccessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


# main
df = pd.read_csv('E:\\Marker basket\\dataset\\basket_analysis.csv')

df = df.drop(columns=['Unnamed: 0'])

one_hot_encoded = df.applymap(lambda x: 1 if x > 0 else 0)

frequent_itemsets = apriori(one_hot_encoded, min_support=0.2, use_colnames=True)

association_rules_df = association_rules(frequent_itemsets, metric='lift', min_threshold=1)


#  output
print("Frequent Itemsets:\n", frequent_itemsets)

print("\nAssociation Rules:\n", association_rules_df)

