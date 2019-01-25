import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

def getFields(df):
    return list(df.axes[1])

def loadData():
    df = []
    for i in range(4):
        filename = 'prof' + str(i + 1) + '.csv'
        this_df = pd.read_csv(filename)
        fields = getFields(this_df)
        
        new_df = {}
        for col in fields:
            new_df[col] = this_df[col].fillna(this_df[col].mean())
        df.append(pd.DataFrame(new_df))
    
    return df

def compare(df):
    fields = getFields(df[0])
    with open('output.txt', 'w') as fout:
        for k in fields:
            section = 'Comparison per %s:' % k 
            print(len(section) * '_'+ '\n' + section, file=fout)
            for i in range(len(df)):
                for j in range(i + 1, len(df)):
                    t_score, t_pval = ttest_ind(df[i][k], df[j][k])
                    mean_i, std_i = np.mean(df[i][k]), np.std(df[i][k])
                    mean_j, std_j = np.mean(df[j][k]), np.std(df[j][k])
                    print('Prof %d vs Prof %d >>' % (i + 1, j + 1), file=fout)
                    print('%d\'s mean and std: %.3f, %.3f' % (i + 1, mean_i, std_i), file=fout)
                    print('%d\'s mean and std: %.3f, %.3f' % (j + 1, mean_j, std_j), file=fout)
                    print('t-test: t_score = %.3f, p_value = %.3f' % (t_score, t_pval), file=fout)


if __name__ == '__main__':
    df = loadData()
    compare(df)


