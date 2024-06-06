import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest


df_final = pd.read_csv('df_final_demo.txt')
df_web1 = pd.read_csv('df_final_web_data_pt_1.txt')
df_web2 = pd.read_csv('df_final_web_data_pt_2.txt')
df_exp = pd.read_csv('df_final_experiment_clients.txt')

# Dropping this column and dropping duplicates

df_final = df_final.drop(columns=['clnt_tenure_mnth'])
df_final = df_final.drop_duplicates()


# Filling the null values with the median

for column in ['num_accts', 'calls_6_mnth', 'logons_6_mnth']:
    median_value = df_final[column].median()
    df_final[column] = df_final[column].fillna(median_value)
    df_final[column] = df_final[column].astype(int)
    
# Filling the null values in age column with the mode

mode_clnt_age = df_final['clnt_age'].mode()[0]
df_final['clnt_age'] = df_final['clnt_age'].fillna(mode_clnt_age).astype(int)

# Fixing null values of bal column with mean and roading

mean_bal = df_final['bal'].mean()
df_final['bal'] = df_final['bal'].fillna(mean_bal).round(2)

# Filling null values with the mode in the gender column

mode_gendr = df_final['gendr'].mode()[0]
df_final['gendr'] = df_final['gendr'].fillna(mode_gendr)

# Changing null values to 1 and changing the data type of num accounts

df_final['num_accts'] = df_final['num_accts'].fillna(1).astype(int)

# Changing null values to 0 in these columns

df_final['calls_6_mnth'] = df_final['calls_6_mnth'].fillna(0).astype(int)
df_final['logons_6_mnth'] = df_final['logons_6_mnth'].fillna(0).astype(int)
df_final['clnt_tenure_yr'] = df_final['clnt_tenure_yr'].fillna(0).astype(int)

# Changing the columns names

df_final.rename(columns={
    'clnt_tenure_yr': 'loyalty',
    'clnt_age': 'client_age',
    'gendr': 'gender',
    'num_accts': 'num_accounts',
    'bal': 'balance',
    'calls_6_mnth': 'calls_6m',
    'logons_6_mnth': 'logons_6m'
}, inplace=True)

# Drop Clients are not in the Test or Control
df_exp = df_exp.dropna(subset='Variation')

# Contact testing program
df_webfull = pd.concat([df_web1, df_web2])

# Preparing / Cleaning  Dataframe
df_webfull['date_time'] = pd.to_datetime(df_webfull['date_time'], dayfirst=True)

# Set date 
date_start = '2017-03-15'
date_end = '2017-06-20'

# Filter DataFrame 
df_webfullfilter = df_webfull.query('date_time >= @date_start and date_time <= @date_end')

map_categoria = df_exp.set_index('client_id')['Variation'].to_dict()
df_webfullfilter['experiment'] = df_webfullfilter['client_id'].map(map_categoria)

df_webfullfilter = df_webfullfilter.dropna(subset='experiment')

# Calcular a taxa de conversão acumulada
def calculate_total_completion_rate(df, experiment_type):
    df_experiment = df[df['experiment'] == experiment_type]
    
    # Total de visitantes únicos
    total_visitors = df_experiment['visitor_id'].nunique()
    
    # Total de visitantes que completaram o processo
    completed_visitors = df_experiment[df_experiment['process_step'] == 'confirm']['visitor_id'].nunique()
    
    # Calcular a taxa de conversão acumulada
    completion_rate = completed_visitors / total_visitors if total_visitors > 0 else 0
    
    return completion_rate

# Calcular a taxa de conversão acumulada para controle e teste
control_total_completion_rate = calculate_total_completion_rate(df_webfullfilter, 'Control')
test_total_completion_rate = calculate_total_completion_rate(df_webfullfilter, 'Test')

control_total_completion_rate, test_total_completion_rate




# step time spent  rates 
# Sort the DataFrame by 'client_id', 'visitor_id', and 'date_time'

df_webfullfilter = df_webfullfilter.sort_values(by=['client_id', 'visitor_id', 'date_time'])

# Calculate the time difference between consecutive rows for each client
# Create Hour colummns and Extract hour from date_time
# df_webfullfilter.loc[:,'hour'] = df_webfullfilter['date_time'].dt.strftime('%H:%M:%S')

# df_webfullfilter['hour'] = pd.to_timedelta(df_webfullfilter['hour'])

df_webfullfilter['time_spent'] = (df_webfullfilter.groupby(['client_id', 'visit_id'])['date_time']
                                                  .diff()
                                                  .shift(-1)
                                                  .fillna(pd.Timedelta(seconds=0))
                                )

df_webfullfilter['seconds_spent'] = df_webfullfilter['time_spent'].dt.total_seconds()
df_webfullfilter = df_webfullfilter.drop(columns="time_spent")

def get_bouncers(dataframe):
    # Group by visit_id and aggregate the process_step
    grouped = dataframe.groupby('visit_id')['process_step'].agg(set).reset_index()

    # Filter to keep only those groups where the set contains only 'start'
    bounce_ids = grouped[grouped['process_step'].apply(lambda x: len(x) == 1 and 'start' in x)]['visit_id']

    return grouped






# Time spent per page
# pivot_table.columns.droplevel(0) remove o nível superior das colunas que contém "mean".
# pivot_table.columns.name = None remove o nome das colunas, eliminando "process_step".
# pivot_table.index.name = None remove o nome do índice, eliminando "experiment".
# Removendo os nomes dos níveis das colunas

df_webfullfilter.groupby('process_step')['seconds_spent'].mean()

pivot_table = pd.pivot_table(
                            df_webfullfilter,
                            values='seconds_spent',
                            index='experiment',
                            columns='process_step',
                            aggfunc=['mean']
                            )
pivot_table.columns = pivot_table.columns.droplevel(0)
pivot_table.columns.name = None
pivot_table.index.name = None




# ERROR RATES
# Função para mapear os passos do processo para números
step_mapping = {'start': 1, 'step_1': 2, 'step_2': 3, 'step_3': 4, 'confirm': 5}

# Mapear os passos para números
df_webfullfilter['steps'] = df_webfullfilter['process_step'].map(step_mapping)

# Identificar se houve retorno para uma etapa anterior
df_webfullfilter['error'] = df_webfullfilter.groupby(['client_id', 'visit_id'])['steps'].diff().shift(-1) < 0

df_webfullfilter = df_webfullfilter.drop_duplicates(subset=['client_id','visit_id', 'process_step', 'experiment', 'error'])


# # Number visits per client
# unique_counts_per_client = df_webfullfilter.groupby('client_id').agg({
#     'visitor_id': 'nunique',
#     'visit_id': 'nunique'
# }).reset_index()

# unique_counts_per_client.columns = ['client_id', 'unique_visitors', 'unique_visits']

def calculate_total_completion_rate(df, experiment_type):
    df_experiment = df[df['experiment'] == experiment_type]
    
    # Total de visitantes únicos
    total_visitors = df_experiment['visitor_id'].nunique()
    
    # Total de visitantes que completaram o processo
    completed_visitors = df_experiment[df_experiment['process_step'] == 'confirm']['visitor_id'].nunique()
    
    # Calcular a taxa de conversão acumulada
    completion_rate = completed_visitors / total_visitors if total_visitors > 0 else 0
    
    return completion_rate
control_total_completion_rate = calculate_total_completion_rate(df_webfullfilter, 'Control')
test_total_completion_rate = calculate_total_completion_rate(df_webfullfilter, 'Test')

## AGE RATES
# Merge the datasets and select only the relevant columns

merged_df = pd.merge(df_exp, df_final, on='client_id')[['client_id', 'client_age', 'Variation']]

# Separate the client ages based on their engagement with the new or old process

test_group = merged_df[merged_df['Variation'] == 'Test']['client_age']
control_group = merged_df[merged_df['Variation'] == 'Control']['client_age']

# Perform a t-test to compare the average ages

t_stat, p_value = ttest_ind(test_group, control_group)

# Define the significance level

alpha = 0.05


## Save all files

df_webfullfilter.to_csv('data_web.csv', index=False)
df_final.to_csv('data_demo.csv',index=False)
