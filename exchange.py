import numpy as np
import pandas as pd


dat_dir = '/Users/huyiqing/Desktop/capstone/'

raw_dat = pd.read_excel(dat_dir + 'exchangeRate/FUT_Foexquodt.xls')
dat = raw_dat.drop([0, 1])      #  drop first two column
dat = dat.set_index(dat['Issued'])
dat.drop('Issued', axis=1, inplace=True)
dat['Jap']['2014-11-18'] /= 100    # raw data bug


# dat['Jap'].plot()

#    Usd     Eur     Jap     Hkd     Gbp



print(dat)

