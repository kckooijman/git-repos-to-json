### Converting YAML-Files to a data set.

    .
    ├── Data
        ├── csv                 # All csv-files are written here.
        ├── index-dumps         # Folder containing metadata of the scraped repositories.
        ├── json                # The YAML-files are converted to a data set in the form of several JSON-files.
        ├── repositories        # Folder containing all repositories.
    ├── create_datasets.py        # Main file to convert all YAML-files to a dictionary, with help of yamlreader.py and dataloader.py.
    ├── dataloader.py             # Class to load and write files.
    ├── extract_lines_of_code.py  # One of the first metrics, extracts lines of code from a YAML-file.
    ├── god_blueprint.py          # A file that is much larger than others, is considered a God Blueprint. Uses lines of code.
    ├── god_blueprint_descriptives.py # Descriptives about God Blueprint files
    ├── paths.py                  # Keeps track of all the paths to the data
    ├── requirements.txt
    ├── simple_metrics.py         # Contains the first extraction of some straightforward metrics from the data
    ├── yamlreader.py             # Class that reads all YAML-files from a folder.
    
    
    

