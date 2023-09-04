from operator import indexOf

import numpy as np

out = open('data/mission_auto_no_aspd.csv', 'w')

def decompose (data):
    lines = data.readlines()
    res = []
    for line in lines:
        _data = line.split(' ')
        _data[22] = f'srv0={_data[22][4:]}' 
        _data[23] = f'srv1={_data[23]}'
        _data[24] = f'srv2={_data[24]}'
        _data[25] = f'srv3={_data[25]}'
        _data[26] = f'lmt0={_data[26][4]}'
        _data[27] = f'lmt1={_data[27][:-1]}'
        temp = []
        for j in _data:
            j = j.split('=')
            temp.append(j)
        _data = np.array(temp)
        res.append(_data)
    return res

data = open('data/mission_auto.txt', 'r')
_decompose = decompose(data)

#insert feature columns
feature_list = _decompose[0].T[0]
features = ''
for f in feature_list:
    features = features + f
    if indexOf(feature_list,f) != len(feature_list) -1:
        features += ','

features+='\n'
dataframe = [features]
for decomposed_data in _decompose:
    df = decomposed_data.T[1]
    line = f'{np.int64(df[0])},{df[1]},{np.float64(df[2])},{np.float64(df[3])},{np.float64(df[4])},{np.float64(df[5])},{np.float64(df[6])},{np.float64(df[7])},{np.float64(df[8])},{np.float64(df[9])},{np.float64(df[10])},{np.float64(df[11])},{np.float64(df[12])},{np.float64(df[13])},{np.float64(df[14])},{np.float64(df[15])},{np.float64(df[16])},{np.float64(df[17])},{np.float64(df[18])},{np.float64(df[19])},{np.float64(df[20])},{np.float64(df[21])},{np.int32(df[22])},{np.int32(df[23])},{np.int32(df[24])},{np.int32(df[25])},{np.float64(df[26])},{np.float64(df[27])}\n'
    dataframe.append(line)

out.writelines(dataframe)
out.close()
data.close()