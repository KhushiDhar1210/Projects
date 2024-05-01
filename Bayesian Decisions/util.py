


def mean(np_array):
    array_sum = sum(np_array)
    ans = array_sum/len(np_array)   
    return ans


def stdev(np_array, mu='none'):
    if mu == 'none':
        mu = mean(np_array)
        
    sq_val_mean_diff = [(x - mu) ** 2 for x in np_array]
    new_mean = sum(sq_val_mean_diff)/len(np_array)
    ans = new_mean**0.5
    return ans

def sampleMean(np_array):
    no_of_samples = len(np_array)
    no_of_feature = len(np_array[0])
    feat_sum = [0] * no_of_feature
    for sample in np_array:
        for x in range(no_of_feature):
            feat_sum[x] += sample[x]
    ans = [summ/no_of_samples for summ in feat_sum]
    return ans


def covariance(np_array):
    no_of_samples = len(np_array)
    no_of_feature = len(np_array[0])
    find_mean = [mean(feat) for feat in zip(*np_array)]
    ans = [[0 for x in range(no_of_feature)] for x in range(no_of_feature)]
    for m in range(no_of_feature):
        for n in range(no_of_feature):
            covariance = sum((np_array[l][m] - find_mean[m]) * (np_array[l][n] - find_mean[n]) for l in range(no_of_samples)) / (no_of_samples - 1)
            ans[m][n] = covariance
            
    return ans
