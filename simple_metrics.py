import dataloader
import operator
import pandas as pd


def count_files_in_repo(repo: dict):
    # Count the number of yaml-files in a repo
    return len(repo)


def depth(d, level=1):
    # Count the depth of a yaml-file (i.e.: the depth of a dictionary)
    if not isinstance(d, dict) or not d:
        return level
    return max(depth(d[k], level + 1) for k in d)


def count_keys(file: dict):
    # Count the variables in a yaml-file (keys in a dict)
    if type(file) == dict:
        return len(file.keys())
    elif type(file) == str:
        return 1
    else:
        return sum([len(d.keys()) for d in file if isinstance(d, dict)])


def count_different_keys(file: dict):
    if type(file) == dict:
        return len(set(file.keys()))
    else:
        return len(set([key for d in file for key in d.keys()]))


def count_nested_keys(file, counts):
    # Counts all the keys in the file, also in the nested dicts
    if type(file) == list:
        for item in file:
            count_nested_keys(item, counts)
    elif type(file) == dict:
        for key in file.keys():
            if key in counts.keys():
                counts[key] += 1
            else:
                counts[key] = 1
            if type(file[key]) in (list, dict):
                count_nested_keys(file[key], counts)


def count_values(value, counts):
    # Counts the occurrences of every value in a file
    if type(value) == list:
        for item in value:
            count_values(item, counts)
    elif type(value) == dict:
        for val in value.values():
            count_values(val, counts)
    else:
        if value in counts.keys():
            counts[value] += 1
        else:
            counts[value] = 1


"""
In the next step, the dataframe is created. For every file, all the filedata is
retrieved using the functions above, afterwards it is placed in the dataframe.
"""


def get_filedata(file):
    vars_in_file = count_keys(file)

    keycount = {}

    vars_in_file_alldepths = sum(keycount.values())
    if bool(keycount):
        most_occurring_var = max(keycount.items(), key=operator.itemgetter(1))
    else:
        most_occurring_var = 0

    unique_vars_in_file_alldepths = len(keycount)

    valuecount = {}

    unique_values_in_file_alldepths = len(valuecount)
    if bool(valuecount):
        most_occurring_value = max(valuecount.items(),
                                   key=operator.itemgetter(1))
    else:
        most_occurring_value = 0

    file_depth = depth(file)
    file_type = type(file)

    return [file_type, file_depth, vars_in_file, vars_in_file_alldepths,
            unique_vars_in_file_alldepths, most_occurring_var,
            unique_values_in_file_alldepths, most_occurring_value]


def create_dataframe(data, loc_data):
    lst = []
    for author in list(data.keys()):
        for repo in data[author].keys():
            for file in data[author][repo].keys():
                if data[author][repo][file]:
                    info = [author, repo, file]
                    info.extend(get_filedata(data[author][repo][file]))
                    info.append(loc_data[author][repo][file])
                    lst.append(info)

    df = pd.DataFrame(lst, columns=['author', 'repo', 'path', 'file_type',
                                    'file_depth', 'vars_in_file',
                                    'vars_in_file_alldepths',
                                    'unique_vars_in_file_alldepths',
                                    'most_occurring_var',
                                    'unique_values_in_file_alldepths',
                                    'most_occurring_value', 'lines_of_code'])
    return df


if __name__ == '__main__':
    d = dataloader.DataLoader()
    ansible = d.load_json('ansible_data.json')
    chef = d.load_json('chef_data.json')
    puppet = d.load_json('puppet_data.json')
    iac = d.load_json('iac_data.json')
    infrascode = d.load_json('infrascode_data.json')

    ansible_loc = d.load_json('ansible_loc.json')
    chef_loc = d.load_json('chef_loc.json')
    puppet_loc = d.load_json('puppet_loc.json')
    iac_loc = d.load_json('iac_loc.json')
    infrascode_loc = d.load_json('infrascode_loc.json')

    ansible_properties = create_dataframe(ansible, ansible_loc)
    ansible_properties['language'] = 'ansible'
    chef_properties = create_dataframe(chef, chef_loc)
    chef_properties['language'] = 'chef'
    puppet_properties = create_dataframe(puppet, puppet_loc)
    puppet_properties['language'] = 'puppet'

    frames = [ansible_properties, chef_properties, puppet_properties]
    all_properties = pd.concat(frames)

    d.write_csv(all_properties, 'all_data_simple_metrics.csv')
    d.write_csv(ansible_properties, 'ansible_simple_metrics.csv')
    d.write_csv(chef_properties, 'chef_simple_metrics.csv')
    d.write_csv(puppet_properties, 'puppet_simple_metrics.csv')
