from paths import repoDir
import yamlreader
import dataloader
import sqlite3
import pandas as pd
import os


def get_yamlfiles(path, language_df):
    authors = [name for name in os.listdir(path)]
    data = dict()
    for author in authors:
        path2 = "{}\\{}".format(path, author)
        repos = [repo for repo in os.listdir(path2) if repo in
                 language_df['name'].values]
        if len(repos) > 0:
            data[author] = dict()
            for repo in repos:
                print(repo)
                reader = yamlreader.YmlReader("{}\\{}".format(path2, repo))

                data[author][repo] = reader.get_all()
    return data


if __name__ == '__main__':
    ansible = sqlite3.connect('Data/index-dumps/Ansible_dump.sqlite')
    chef = sqlite3.connect('Data/index-dumps/Chef_dump.sqlite')
    iac = sqlite3.connect('Data/index-dumps/IaC_dump.sqlite')
    infrascode = sqlite3.connect('Data/index-dumps/InfrastructureAsCode_dump.sqlite')
    puppet = sqlite3.connect('Data/index-dumps/Puppet_dump.sqlite')
    db_dict = {"df_ansible": ansible, "df_chef": chef, "df_iac": iac,
               "df_infrascode": infrascode, "df_puppet": puppet}

    ansible = pd.read_sql_query("SELECT * FROM repositories", ansible)
    chef = pd.read_sql_query("SELECT * FROM repositories", chef)
    iac = pd.read_sql_query("SELECT * FROM repositories", iac)
    infrascode = pd.read_sql_query("SELECT * FROM repositories", infrascode)
    puppet = pd.read_sql_query("SELECT * FROM repositories", puppet)

    ansible_data = get_yamlfiles(repoDir, ansible)
    chef_data = get_yamlfiles(repoDir, chef)
    iac_data = get_yamlfiles(repoDir, iac)
    infrascode_data = get_yamlfiles(repoDir, infrascode)
    puppet_data = get_yamlfiles(repoDir, puppet)

    d = dataloader.DataLoader()
    d.write_json(ansible_data, "ansible_data.json")
    d.write_json(chef_data, "chef_data.json")
    d.write_json(iac_data, "iac_data.json")
    d.write_json(infrascode_data, "infrascode_data.json")
    d.write_json(puppet_data, "puppet_data.json")
