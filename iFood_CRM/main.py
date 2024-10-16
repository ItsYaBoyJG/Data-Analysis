import pandas as pd


original_file = "Data_Sets/iFood_BA_Test/ifood_df.csv"

new_file = "Data_Sets/iFood_BA_Test/new_ifood_df.csv"

data = pd.read_csv(original_file)

df = pd.DataFrame(data)

df['marital_Divorced'] = df['marital_Divorced'].astype('str')
df['marital_Single'] = df['marital_Single'].astype('str')
df['marital_Together'] = df['marital_Together'].astype('str')
df['marital_Married'] = df['marital_Married'].astype('str')
df['marital_Widow'] = df['marital_Widow'].astype('str')

df['education_Basic'] = df['education_Basic'].astype('str')
df['education_Graduation'] = df['education_Graduation'].astype('str')
df['education_Master'] = df['education_Master'].astype('str')
df['education_PhD'] = df['education_PhD'].astype('str')
df['education_2n Cycle'] = df['education_2n Cycle'].astype('str')

for index, row in df.iterrows():
    for j in row['marital_Divorced']:
        if j == 1 or j == '1':
            df.at[index, 'marital_Divorced'] = 'Divorced'
        else:
            df.at[index, 'marital_Divorced'] = ''
    for k in row['marital_Single']:
        if k == 1 or k == '1':
            df.at[index, 'marital_Single'] = 'Single'
        else:
            df.at[index, 'marital_Single'] = ''
    for l in row['marital_Together']:
        if l == 1 or l == '1':
            df.at[index, 'marital_Together'] = 'Together'
        else:
            df.at[index, 'marital_Together'] = ''
    for m in row['marital_Married']:
        if m == 1 or m == '1':
            df.at[index, 'marital_Married'] = 'Married'
        else:
            df.at[index, 'marital_Married'] = ''
    for n in row['marital_Widow']:
        if n == 1 or n == '1':
            df.at[index, 'marital_Widow'] = 'Widow'
        else:
            df.at[index, 'marital_Widow'] = ''
    for o in row['education_Basic']:
        if o == 1 or o == '1':
            df.at[index, 'education_Basic'] = 'Basic'
        else:
            df.at[index, 'education_Basic'] = ''
    for p in row['education_Graduation']:
        if p == 1 or p == '1':
            df.at[index, 'education_Graduation'] = 'Graduation'
        else:
            df.at[index, 'education_Graduation'] = ''
    for k in row['education_Master']:
        if k == 1 or k == '1':
            df.at[index, 'education_Master'] = 'Master'
        else:
            df.at[index, 'education_Master'] = ''
    for k in row['education_PhD']:
        if k == 1 or k == '1':
            df.at[index, 'education_PhD'] = 'PhD'
        else:
            df.at[index, 'education_PhD'] = ''
    for k in row['education_2n Cycle']:
        if k == 1 or k == '1':
            df.at[index, 'education_2n Cycle'] = '2n Cycle'
        else:
            df.at[index, 'education_2n Cycle'] = ''
    


df['education_Status'] = df['education_2n Cycle'] + df['education_Basic'] + df['education_Graduation'] + df['education_Master'] + df['education_PhD']

df['marital_Status'] = df['marital_Divorced'] + df['marital_Married'] + df['marital_Together'] + df['marital_Single'] + df['marital_Widow']

del df['education_2n Cycle'], df['education_Basic'], df['education_Graduation'], df['education_Master'], df['education_PhD'], df['marital_Divorced'], df['marital_Married'],df['marital_Single'], df['marital_Together'], df['marital_Widow']


df.to_csv(new_file)