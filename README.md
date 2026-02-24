# [Clone Users Public Github Repositories]

A script to clone specific users public Github repositories in bulk with customisation options

## Background
- If you need to download a users public Github repositories then doing it manually takes time
- This script allows users to provide a users Github username and it will clone their repositories into a sub-folder of their username
- By default the script downloads the users 5 repositories that have been created most recently
    - This can be customised using the '--maxrepos' flag (see Usage section below)

- This script is useful for companies who need to review a job candidates portfolio to easily review their work

## Requirements

- Python (Install Python)[https://www.python.org/downloads/]
- Git (Installing Git)[https://git-scm.com/book/en/v2/Getting-Started-Installing-Git]

- The program also uses the following python packages
    - pandas
    - Requests

     - A requirements file has been provided which which will automatically install the required packages
        - To install them type 'pip install -r requirements.txt' in a terminal inside of this repository

## Usage

### Platforms 

- This script has been tested, and currently works on:
    - Linux
    - Mac
    - Windows

### Running

- Run 'python3 getrepos.py -username <username>'
    - Example: 'python3 getrepos.py -username jstriker87'

### Command line arguments

- '--username' - Provides username of the Github user that you wish to clone their repositories
- '--maxrepos' - Allows users to specify the number of repositories of the user to clone (default 5)
- '--file' - Allows users to provide an Excel file with each row containing a users name and username
    - A provided excel file should have the headers 'Name' and 'Username'
    - For each row the users Github repositories will be saved into subfolders using the format 'Name-Username'
        - For example if the spreadsheet had 'John Smith' 'github', the repositories would be stored in in a subfolder called 'John Smith - Github' 

## License
Licensed under the [GNU GENERAL PUBLIC LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html)
You can find a copy of it in [LICENSE](LICENSE).

## Dependencies / Acknowledgements

This project uses [**requests**](https://github.com/psf/requests) by [@psf](https://github.com/psf), A HTTP library

> requests is licensed under the Apache License 2.0 
> https://github.com/psf/requests/blob/main/LICENSE

This project uses [**pandas**](https://github.com/pandas-dev/pandas) from [@pandas-dev](https://github.com/pandas-dev),  A strict and fast JSON parser/decoder/encoder written in pure Lua.

> pandas is licensed under the BSD 3-Clause License 
> Redistribution and use in source and binary forms, with or without
    > https://github.com/pandas-dev/pandas?tab=BSD-3-Clause-1-ov-file#readme
