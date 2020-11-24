Binary Classification Metrics

This package contains various binary classification methods. The methods included are as follows:

1. Precision Score - precision_score(predicted,actual)
2. Recall Score - recall_score(predicted,actual)
3. Selectivity or True Negative Rate - true_negative_rate(predicted,actual)
4. Negative Predictive Value - negative_predictive_value(predicted,actual)
5. Miss Rate or False Negative Rate - miss_rate(predicted,actual)
6. Fall Out or False Positive Rate - fall_out_score(predicted,actual)
7. False Discovery Rate - false_discovery_rate(predicted,actual)
8. False Omission Rate - false_omission_rate(predicted,actual)
9. Weighted Average Precision Score - weighted_avg_precision_score(predicted,actual)
10. Weighted Average Recall Score - weighted_avg_recall_score(predicted,actual)
11. Confusion Matrix - confusion_matrix(predicted,actual) - Return False Pos,False Neg,True Pos,True Neg

* The two arguments are the predicted classes and actual classes of the classification.
* Higher Class Number equates to the positive label.