plt.pie(df['rainfall'].value_counts().values,
		labels = df['rainfall'].value_counts().index,
		autopct='%1.1f%%')
plt.show()
df.groupby('rainfall').mean()
features = list(df.select_dtypes(include = np.number).columns)
features.remove('day')
print(features)
plt.subplots(figsize=(15,8))

for i, col in enumerate(features):
plt.subplot(3,4, i + 1)
sb.distplot(df[col])
plt.tight_layout()
plt.show()
plt.subplots(figsize=(15,8))

for i, col in enumerate(features):
plt.subplot(3,4, i + 1)
sb.boxplot(df[col])
plt.tight_layout()
plt.show()
dplt.figure(figsize=(10,10))
sb.heatmap(df.corr() > 0.8,
		annot=True,
		cbar=False)
plt.show()
f.replace({'yes':1, 'no':0}, inplace=True)
df.drop(['maxtemp', 'mintemp'], axis=1, inplace=True)

