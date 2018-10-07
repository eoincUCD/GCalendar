import pandas as pd
import numpy as np
from datetime import datetime


def parse(filename, df):  # Function to parse
    open_file = open(filename, encoding="utf8")
    j = df.shape[0] - 1
    for line in open_file:
        if "BEGIN:VEVENT" in line:
            j += 1
            df.loc[j, "filename"] = filename
        if "DTSTART" in line:
            start = line.rstrip().split(":")
            df.loc[j, "start"] = start[-1]
        if "DTEND" in line:
            end = line.rstrip().split(":")
            df.loc[j, "end"] = end[-1]
        if "SUMMARY:" in line:
            summary = line.rstrip().split(":")
            df.loc[j, "summary"] = summary[-1]
        if "RRULE:" in line:
            rule = line.rstrip().split(":")
            df.loc[j, "rule"] = rule[-1]
        if "END:VEVENT" in line:
            if "T" in df.loc[j, "start"]:
                df.loc[j, "start_datetime"] = datetime.strptime(
                    df.loc[j, "start"].split("T")[0] + df.loc[j, "start"].split("T")[1][:4], '%Y%m%d%H%M')
                df.loc[j, "end_datetime"] = datetime.strptime(
                    df.loc[j, "end"].split("T")[0] + df.loc[j, "end"].split("T")[1][:4], '%Y%m%d%H%M')
                duration = df.loc[j, "end_datetime"] - df.loc[j, "start_datetime"]
                df.loc[j, "duration"] = duration / pd.Timedelta(hours=1)  # Divide by timedelta units of hours
            else:
                df.loc[j, "start_datetime"] = datetime.strptime(df.loc[j, "start"], '%Y%m%d')
                df.loc[j, "end_datetime"] = datetime.strptime(df.loc[j, "end"], '%Y%m%d')
                duration = df.loc[j, "end_datetime"] - df.loc[j, "start_datetime"]
                df.loc[j, "duration"] = duration / pd.Timedelta(hours=1)  # Divide by timedelta units of hours
    return df


df = pd.DataFrame()
# df = parse("data/CarrollFam.ics", df)

for file in ("Gmail.ics"):
    df = parse("data/" + file, df)
    print(file, df.shape[0])

df.to_csv("data/out_raw.csv")
df = df.loc[df["start_datetime"] >= datetime.strptime("20170801", '%Y%m%d')]
df = df.loc[df["end_datetime"] <= datetime.strptime("20180810", '%Y%m%d')]
df.to_csv("data/out_filtered.csv")