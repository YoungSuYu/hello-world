import pandas as pd
import numpy as np
data_13 = pd.read_csv("/Users/yuyoungsu/Documents/LAB/12. SNA prediction/3. Data/4. Pair data/2.1. Pair_2013_binary.csv", header=0)
sum_data = pd.read_csv("/Users/yuyoungsu/Documents/LAB/12. SNA prediction/3. Data/5. sum_by ID_by 2015.csv", header=0, index_col=0)
master = pd.read_csv("/Users/yuyoungsu/Documents/LAB/12. SNA prediction/3. Data/3. Master data_by 2015.csv", header=0, index_col=0)
list(data_13)
list(master)
data_13['source'].values
data_13['target'].values
data_13['binary'].values

sum_data.values

#dic ={}
#dic['key1'] = 1
#dic['key2'] = 2
#dic2 = {"key": 1}
#a = np.array([0,1,2,3])


#2013 make variables
##2013 PA
# dic = {}
# for j in range(1, len(sum_data)+1):
#     dic['n'+str(j)] = sum_data.loc['n'+str(j)]['2013']
#
# result = list()
# for i in range(len(data_13)):
#     result.append(dic[data_13['source'].values[i]] * dic[data_13['target'].values[i]])
#
# result2 = pd.DataFrame(result, columns=['PA'])
# frame = [data_13, result2]
# result_data_13 = pd.concat(frame, axis=1)

result_data_13 = data_13

##2013 Global-Local
list(result_data_13)

result_data_13['global_local'] = result_data_13['source_gl']+result_data_13['target_gl']
result_data_13['global_local'] = result_data_13['global_local'].replace('gl', 'lg')

result_data_13['global_local'] = result_data_13['global_local'].replace('ll',1)
result_data_13['global_local'] = result_data_13['global_local'].replace('lg',0.5)
result_data_13['global_local'] = result_data_13['global_local'].replace('gg',0.25)


##2013 Success rate difference
dic = {}
for i in range(1, len(master)+1):
    dic['n'+str(i)] = master.loc['n'+str(i)]['Success_rate(2013)']

result = list()
for j in range(len(result_data_13)):
    result.append(abs(dic[result_data_13['source'].values[j]]- dic[result_data_13['target'].values[j]]))

result2 = pd.DataFrame(result, columns=['Success_rate_difference'])
frame = [result_data_13, result2]
result_data_13 = pd.concat(frame, axis=1)

##2013 Experience difference
dic = {}
for i in range(1, len(master)+1):
    dic['n'+str(i)] = master.loc['n'+str(i)]['Experience(2013)']

result = list()
for j in range(len(result_data_13)):
    result.append(abs(dic[result_data_13['source'].values[j]]- dic[result_data_13['target'].values[j]]))

result2 = pd.DataFrame(result, columns=['Experience_difference'])
frame = [result_data_13, result2]
result_data_13 = pd.concat(frame, axis=1)

##2013 Technical difference
dic = {}
for i in range(1, len(master)+1):
    dic['n'+str(i)] = master.loc['n'+str(i)]['Technical(2013)']

result = list()
for j in range(len(result_data_13)):
    result.append(abs(dic[result_data_13['source'].values[j]]- dic[result_data_13['target'].values[j]]))

result2 = pd.DataFrame(result, columns=['Technical_difference'])
frame = [result_data_13, result2]
result_data_13 = pd.concat(frame, axis=1)

##2013 Financial difference
dic = {}
for i in range(1, len(master)+1):
    dic['n'+str(i)] = master.loc['n'+str(i)]['Financial(2013)']

result = list()
for j in range(len(result_data_13)):
    result.append(abs(dic[result_data_13['source'].values[j]]- dic[result_data_13['target'].values[j]]))

result2 = pd.DataFrame(result, columns=['Financial_difference'])
frame = [result_data_13, result2]
result_data_13 = pd.concat(frame, axis=1)

list(result_data_13)

result_data_13.to_csv('/Users/yuyoungsu/Documents/LAB/12. SNA prediction/3. Data/6. Preprocessing for DL/2013/1.data_2013_pa.csv')


