df = pd.read_csv('Rainfall.csv')
df.head()
df.shape
df.describe().T
df.isnull().sum()
df.codf.rename(str.strip,
		axis='columns', 
		inplace=True)

df.columns
for col in df.columns:

# Checking if the column contains
# any null values
if df[col].isnull().sum() > 0:
	val = df[col].mean()
	df[col] = df[col].fillna(val)
	
df.isnull().sum().sum()

