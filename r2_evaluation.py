# now evaluate the model with R^2
Xtest = np.array(test_data[[f'answer_num_{n}' for n in range(1, 16)]])
ytest = np.array(test_data['result'])
print('R^2 score of the trained model ' + name_filter + ' : ', model.score(Xtest, ytest))
r2 =np.array(r2,[model.score(Xtest, ytest),name_filter])
