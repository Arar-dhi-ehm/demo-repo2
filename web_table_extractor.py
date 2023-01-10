"""
web_table_extractor.py
    Capabilities:

    Limitations:

    Improvements:

    Prerequisites:
        Install pandas library
        Install lxml library

"""
import pandas as pd

# Read 1 CSV file from a website itself. Copy the link address of csv file in the web.
pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')