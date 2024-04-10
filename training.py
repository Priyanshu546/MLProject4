features = df.drop(['day', 'rainfall'], axis=1)
target = df.rainfall
X_train, X_val, \
	Y_train, Y_val = train_test_split(features,
									target,
									test_size=0.2,
									stratify=target,
									random_state=2)

# As the data was highly imbalanced we will
# balance it by adding repetitive rows of minority class.
ros = RandomOverSampler(sampling_strategy='minority',
						random_state=22)
X, Y = ros.fit_resample(X_train, Y_train)
# Normalizing the features for stable and fast training.
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_val = scaler.transform(X_val)
models = [LogisticRegression(), XGBClassifier(), SVC(kernel='rbf', probability=True)]

for i in range(3):
models[i].fit(X, Y)

print(f'{models[i]} : ')

train_preds = models[i].predict_proba(X) 
print('Training Accuracy : ', metrics.roc_auc_score(Y, train_preds[:,1]))

val_preds = models[i].predict_proba(X_val) 
print('Validation Accuracy : ', metrics.roc_auc_score(Y_val, val_preds[:,1]))
print()
metrics.plot_confusion_matrix(models[2], X_val, Y_val)
plt.show()
print(metrics.classification_report(Y_val,
									models[2].predict(X_val)))
