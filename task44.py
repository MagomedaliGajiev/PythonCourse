import pandas as pd 
import numpy as np 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
 

data['isRobot'] = data['whoAmI'].apply(lambda s: 1 if s == 'robot' else 0)
#data['isHuman'] = data['whoAmI'].apply(lambda s: 1 if s == 'human' else 0) Одного столбца достаточно для one hot кодирования
data = data.drop('whoAmI', axis=1)
print(data)