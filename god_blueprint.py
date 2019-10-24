from statistics import median
import numpy as np
import dataloader


def is_upper_outlier(value, language, upper_bounds):
    return value > upper_bounds[language]


if __name__ == '__main__':
    d = dataloader.DataLoader()
    data = d.load_csv("all_data_simple_metrics.csv")
    languages = ['ansible', 'chef', 'puppet']
    upper_bounds = {}
    for language in languages:
        language_data = data[data['language'] == language]
        loc = language_data['lines_of_code']
        m = median(loc)
        q1, q3 = np.percentile(loc, [25, 75])
        iqr = q3 - q1
        upper_bounds[language] = q3 + (1.5*iqr)

    data['upper_outlier'] = [rule['lines_of_code'] >
                             upper_bounds[rule['language']]
                             for index, rule in data.iterrows()]

    d.write_csv(data, 'simple_metrics.csv')
