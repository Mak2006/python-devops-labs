import numpy as np

# How do you apply a function on a dataframe column using data from previous rows?
# https://stackoverflow.com/questions/62170148/how-do-you-apply-a-function-on-a-dataframe-column-using-data-from-previous-rows

import pandas as pd

#    nums   b    result
# 0  20.0  1    20.0
# 1  22.0  0    0
# 2  30.0  1    0
# 3  29.1  1    0
# 4  20.0  0    0


data = [
    [20.0, 1, 20.0],
    [22.0, 0, 0],
    [30.0, 1, 0],
    [29.1, 1, 0],
    [20.0, 0, 0]
]


def some_calc_func(bval, prev_result, curr_num):
        if bval == 0:
            return prev_result + curr_num
        else:
            return prev_result - curr_num


if __name__ == '__main__':
    df = pd.DataFrame(data, columns=['nums', 'b', 'result'])
    print(df)

    # df['result'] = df['b'].apply(lambda x: df.b.shift(1) if x == 1 else x )

    # for i in range(1, len(df)):
    #     df.loc[i, 'result'] = df.loc[i - 1, 'result'] + df.loc[i, 'nums']

    # for i in range(1, len(df)):
    #     bval = df.loc[i, 'b']
    #     if bval == 0:
    #         df.loc[i, 'result'] = df.loc[i - 1, 'result'] + df.loc[i, 'nums']
    #     else:
    #         df.loc[i, 'result'] = df.loc[i - 1, 'result'] - df.loc[i, 'nums']

    for i in range(1, len(df)):
        df.loc[i, 'result'] = some_calc_func(df.loc[i, 'b'], df.loc[i - 1, 'result'], df.loc[i, 'nums'])

    print(df)
