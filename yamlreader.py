import os
import yaml


class YmlReader():

    # Initialize object
    def __init__(self, path):
        self.contents = os.listdir(path)
        self.name = path.split('\\')[-1]
        self.path = path

    # Count number of files and folders in directory
    def count(self):
        return len(self.contents)

    # Check if a file in the directory is a directory
    def isdir(self, file):
        return os.path.isdir(self.name + "\\" + file)

    # Check if a file in the directory is a file
    def isfile(self, file):
        return not self.isdir(file)

    # Check if a file in the directory is a YAML-file
    def isyaml(self, file):
        if self.isfile(file):
            filename = file
            extension = filename.split(".")[-1]
            return extension == "yaml" or extension == "yml"
        else:
            return False

    # Given a list of paths to files, created with get_yaml_files, read them.
    def read_yaml(self, list_of_yaml_files):
        filedict = {}
        # filelist = []
        for file in list_of_yaml_files:
            path = file.split("\\")[10:]
            filename = "\\".join(path)
            with open(file, 'r', encoding='utf8') as f:
                try:
                    # print(yaml.load(file))

                    filedict[filename] = yaml.load(f, Loader=yaml.Loader)
                    # filelist.append(yaml.load(file))
                except yaml.YAMLError as exc:
                    print(exc)
        # return filelist
        return filedict

    def get_yaml_files(self):
        walk = os.walk(self.path)
        yaml_files = []
        for root, dirs, files in walk:
            for filename in files:
                if filename.endswith(".yml"):
                    yaml_files.append(os.path.join(root, filename))

        return yaml_files

    def get_all(self):
        """
        The main function of the project,
        calling this function should do everything you want.
        """
        filename_list = self.get_yaml_files()
        filelist = self.read_yaml(filename_list)
        return filelist

    def count_loc(self, file):
        with open(file) as f:
            for i, l in enumerate(f):
                pass
            try:
                i
            except NameError:
                i = None
            if i is None:
                return 0
            else:
                return i+1


if __name__ == '__main__':
    path = 'repositories'
    r = YmlReader(path)
    files = r.get_yaml_files()
    for file in files:
        print(file, r.count_loc(file))
