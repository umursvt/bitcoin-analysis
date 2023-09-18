import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

csv_read=pd.read_csv('btc_price.csv')

plt.figure(figsize=(20,12))

for index, col in enumerate([ 'High','Low'],1):
    plt.subplot(2,1,index)
    plt.plot(csv_read['Date'],csv_read[col])
    plt.title(col)

plt.tight_layout()
plt.show()