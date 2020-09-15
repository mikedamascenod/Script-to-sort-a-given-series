# A Program to sort a given series
# uM programa que classifica uma determinada série.

import pandas as pd
s = pd.Series(['120','240','python','500.12','800'])
print("Original Data Series:")
print(s)
new_s = pd.Series(s).sort_values()
print(new_s)