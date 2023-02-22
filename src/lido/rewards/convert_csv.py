import sys

import csv
import pandas as pd
import datetime



def convert_csv(input_csv):

    columns_names =["Type", "Buy Amount", "Buy Currency", "Sell Amount", "Sell Currency", "Fee", "Fee Currency", "Exchange", "Trade-Group", "Comment", "Date"]
    df = pd.read_csv(input_csv)
    print(df)
    
    data = []
    for ind in df.index:
        raw_text = df['date'][ind]
        text =raw_text.split(' ', 6)[0:6]
        input_text=" ".join(text[:len(text)])
        new_date = datetime.datetime.strptime(input_text,"%a %b %d %Y %H:%M:%S %Z%z")
        row = [df['type'][ind],df['change'][ind],'STETH',0.00,'',0.00,'','Ledger Live','LIDO staking rewards','LIDO staking rewards',new_date]
        data.append(row)
    dfout = pd.DataFrame(data,columns=columns_names)
    print(dfout)



