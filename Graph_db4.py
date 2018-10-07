import pandas as pd
import numpy as np
import math
from datetime import datetime

# todo Km ran and cycled from strava
# todo number of gym sessions

df = pd.read_csv("data/data.csv")

total_time = (365+9)*24
accounted_for = 7188
unaccounted_for = total_time - accounted_for

sankey_df = pd.DataFrame([["Total", "Unaccounted For", unaccounted_for]], columns=['from', 'to', 'time'])

for index, row in df.iterrows():
    category_1 = df.loc[index, "category_1"]
    category_2 = df.loc[index, "category_2"]
    category_3 = df.loc[index, "category_3"]
    time = df.loc[index, "total_time"]

    existing_from = sankey_df.index[sankey_df["from"] == "Total"].tolist()
    existing_to = sankey_df.index[sankey_df["to"] == category_1].tolist()
    common_elements = list(set(existing_from).intersection(existing_to))
    if len(common_elements) == 0:
        sankey_df.loc[len(sankey_df)] = ["Total", category_1, time]
    else:
        sankey_df.loc[common_elements[0], 'time'] = sankey_df.loc[common_elements[0], 'time'] + time

    existing_from = sankey_df.index[sankey_df["from"] == category_1].tolist()
    existing_to = sankey_df.index[sankey_df["to"] == category_2].tolist()
    common_elements = list(set(existing_from).intersection(existing_to))
    if len(common_elements) == 0:
        sankey_df.loc[len(sankey_df)] = [category_1, category_2, time]
    else:
        sankey_df.loc[common_elements[0], 'time'] = sankey_df.loc[common_elements[0], 'time'] + time

    if category_3 != "EMPTY":
        existing_from = sankey_df.index[sankey_df["from"] == category_2].tolist()
        existing_to = sankey_df.index[sankey_df["to"] == category_3].tolist()
        common_elements = list(set(existing_from).intersection(existing_to))
        if len(common_elements) == 0:
            sankey_df.loc[len(sankey_df)] = [category_2, category_3, time]
        else:
            sankey_df.loc[common_elements[0], 'time'] = sankey_df.loc[common_elements[0], 'time'] + time


#  Convert floats to int and output in format for Sankeymatic.com
sankey_df.time = sankey_df.time.astype(int)
text_file = open("data\Output.txt", "w")
for index, row in sankey_df.iterrows():
    # print(str(row["from"]) + " [" + str(row["time"]) + "] " + str(row["to"]))
    text_file.write(str(row["from"]) + " [" + str(round(row["time"]/24, 1)) + "] " + str(row["to"]) + "\n")
text_file.close()

sankey_df.to_csv("data/sankey.csv")

#  todo things are being added more than once - combine all three?