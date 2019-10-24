import dataloader
from statistics import median, mean
import numpy as np

if __name__ == '__main__':
    d = dataloader.DataLoader()
    data = d.load_csv('simple_metrics.csv')

    ans_loc = data[data['language'] == 'ansible']['lines_of_code']
    chef_loc = data[data['language'] == 'chef']['lines_of_code']
    pup_loc = data[data['language'] == 'puppet']['lines_of_code']

    print("number of ansible files: {}".format(len(ans_loc)))
    print("number of chef files: {}".format(len(chef_loc)))
    print("number of puppet files: {}".format(len(pup_loc)))
    print('\n')

    print("Total number of ansible lines of code: {}".format(sum(ans_loc)))
    print("Total number of chef lines of code: {}".format(sum(chef_loc)))
    print("Total number of puppet lines of code: {}".format(sum(pup_loc)))
    print('\n')

    print("Average number of ansible lines of code: {}".format(mean(ans_loc)))
    print("Average number of chef lines of code: {}".format(mean(chef_loc)))
    print("Average number of puppet lines of code: {}".format(mean(pup_loc)))
    print('\n')

    print("Median number of ansible lines of code: {}".format(median(ans_loc)))
    print("Median number of chef lines of code: {}".format(median(chef_loc)))
    print("Median number of puppet lines of code: {}".format(median(pup_loc)))
    print('\n')

    print("Proportion of God Blueprints in ansible: {}".format(sum(
        data[data['language'] == 'ansible']['upper_outlier'])/len(ans_loc)))
    print("Proportion of God Blueprints in chef: {}".format(
        sum(data[data['language'] == 'chef']['upper_outlier'])/len(chef_loc)))
    print("Proportion of God Blueprints in puppet: {}".format(
        sum(data[data['language'] == 'puppet']['upper_outlier'])/len(pup_loc)))
    print('\n')

    print("first and third quartile of ansible LOC: {}".format(
        np.percentile(ans_loc, [25, 75])))
    print("first and third quartile of chef LOC: {}".format(
        np.percentile(chef_loc, [25, 75])))
    print("first and third quartile of puppet LOC: {}".format(
        np.percentile(pup_loc, [25, 75])))
    print('\n')

    print("Number of God Blueprints in ansible: {}".format(
        sum(data[data['language'] == 'ansible']['upper_outlier'])))
    print("Number of God Blueprints in chef: {}".format(
        sum(data[data['language'] == 'chef']['upper_outlier'])))
    print("Number of God Blueprints in puppet: {}".format(
        sum(data[data['language'] == 'puppet']['upper_outlier'])))
    print('\n')
