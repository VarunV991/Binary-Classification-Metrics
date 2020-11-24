# Converter
def converter(predicted,actual):
    values = sorted(set(actual))
    dict1 = {values[0]:0,values[1]:1}
    actual = [dict1[k] for k in actual]
    predicted = [dict1[k] for k in predicted]
    return predicted,actual

# Confusion Matrix
def confusion_matrix(predicted,actual):
    fp = 0
    fn = 0
    tp = 0
    tn = 0
    for i in range(len(predicted)):
        if(predicted[i]==actual[i]):
            if(predicted[i]==1):
                tp+=1
            else:
                tn+=1
        else:
            if(predicted[i]==1):
                fp+=1
            else:
                fn+=1
    return fp,fn,tp,tn 

# Recall/ True Positive Rate
def recall_score(predicted,actual):
    predicted,actual = converter(predicted,actual)
    fp,fn,tp,tn = confusion_matrix(predicted,actual)
    return tp/(tp+fn)

# Precision / Positive Predictive Value
def precision_score(predicted,actual):
    predicted,actual = converter(predicted,actual)
    fp,fn,tp,tn = confusion_matrix(predicted,actual)
    return tp/(tp+fp)

# True Negative Rate
def true_negative_rate(predicted,actual):
    predicted,actual = converter(predicted,actual)
    fp,fn,tp,tn = confusion_matrix(predicted,actual)
    return tn/(tn+fp)

# Negative Predictive Value
def negative_predictive_value(predicted,actual):
    predicted,actual = converter(predicted,actual)
    fp,fn,tp,tn = confusion_matrix(predicted,actual)
    return tn/(tn+fn)

# Miss rate / false negative rate
def miss_rate(predicted,actual):
    return 1 - recall_score(predicted,actual)

# fall-out / false positive rate
def fall_out_score(predicted,actual):
    return 1 - true_negative_rate(predicted,actual)

# false discovery rate
def false_discovery_rate(predicted,actual):
    return 1 - precision_score(predicted,actual)

# false omission rate
def false_omission_rate(predicted,actual):
    return 1 - negative_predictive_value(predicted,actual)

# Weighted Average Precision Score
def weighted_avg_precision_score(predicted,actual):
    predicted,actual = converter(predicted,actual)
    total_neg = 0
    total_pos = 0
    for i in range(len(predicted)):
        if(actual[i]==1):
            total_pos+=1
        else:
            total_neg+=1
    precision_pos = precision_score(predicted,actual)
    precision_neg = negative_predictive_value(predicted,actual)
    return (total_pos*precision_pos + total_neg*precision_neg)/len(actual)

# Weighted Average Recall Score
def weighted_avg_recall_score(predicted,actual):
    predicted,actual = converter(predicted,actual)
    total_neg = 0
    total_pos = 0
    for i in range(len(predicted)):
        if(actual[i]==1):
            total_pos+=1
        else:
            total_neg+=1
    recall_pos = recall_score(predicted,actual)
    recall_neg = fall_out_score(predicted,actual)
    return (total_pos*recall_pos + total_neg*recall_neg)/len(actual)

__version__ = "0.0.3"