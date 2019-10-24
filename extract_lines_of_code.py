import paths
import yamlreader
import dataloader
import sqlite3
import pandas as pd
import os


def count_linesofcode(path, language_df):
    authors = [name for name in os.listdir(path)]
    data = dict()
    for author in authors:
        path2 = "{}\\{}".format(path, author)
        repos = [repo for repo in os.listdir(path2) if repo in
                 language_df['name'].values]

        if len(repos) > 0:
            data[author] = dict()

            for repo in repos:
                reader = yamlreader.YmlReader("{}\\{}".format(path2, repo))
                files = reader.get_yaml_files()
                data[author][repo] = dict()

                for file in files:
                    p = file.split('\\')[10:]
                    filename = '\\'.join(p)
                    data[author][repo][filename] = dict()
                    loc = reader.count_loc(file)
                    data[author][repo][filename] = loc

    return data


if __name__ == '__main__':
    os.chdir(paths.dumpsDir)
    ansible = sqlite3.connect('Ansible_dump.sqlite')
    chef = sqlite3.connect('Chef_dump.sqlite')
    iac = sqlite3.connect('IaC_dump.sqlite')
    infrascode = sqlite3.connect('InfrastructureAsCode_dump.sqlite')
    puppet = sqlite3.connect('Puppet_dump.sqlite')
    db_dict = {"df_ansible": ansible, "df_chef": chef, "df_iac": iac,
               "df_infrascode": infrascode, "df_puppet": puppet}

    ansible = pd.read_sql_query("SELECT * FROM repositories", ansible)
    chef = pd.read_sql_query("SELECT * FROM repositories", chef)
    iac = pd.read_sql_query("SELECT * FROM repositories", iac)
    infrascode = pd.read_sql_query("SELECT * FROM repositories", infrascode)
    puppet = pd.read_sql_query("SELECT * FROM repositories", puppet)

    ansible_loc = count_linesofcode(paths.repoDir, ansible)
    chef_loc = count_linesofcode(paths.repoDir, chef)
    iac_loc = count_linesofcode(paths.repoDir, iac)
    infrascode_loc = count_linesofcode(paths.repoDir, infrascode)
    puppet_loc = count_linesofcode(paths.repoDir, puppet)

    d = dataloader.DataLoader()
    d.write_json(ansible_loc, "ansible_loc.json")
    d.write_json(chef_loc, "chef_loc.json")
    d.write_json(iac_loc, "iac_loc.json")
    d.write_json(infrascode_loc, "infrascode_loc.json")
    d.write_json(puppet_loc, "puppet_loc.json")
