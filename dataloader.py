from paths import dataDir, jsonDir, csvDir
import json
import pandas as pd


class DataLoader():
    """The class's docstring."""

    def __init__(self):
        """Initialize class."""
        self.dir = dataDir
        self.jsonDir = jsonDir
        self.csvDir = csvDir

    def load_json(self, filename):
        # Load json file.
        with open(self.jsonDir + "\\" + filename, 'r') as f:
            data = json.load(f)
        return data

    def load_csv(self, filename):
        return pd.read_csv(self.csvDir + "\\" + filename)

    def write_csv(self, file, filename):
        # Write csv file
        file.to_csv(self.csvDir + "\\" + filename)

    def write_json(self, file, filename):
        # Write json file.
        with open(self.jsonDir + "\\" + filename, 'w') as f:
            json.dump(file, f, indent=4, default=str)
