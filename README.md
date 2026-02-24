# [Clone Users Public Github Repositories]

A script to clone specific users public Github repositories in bulk with customisation options

## Background
- If you need to download a users public Github repositories then doing it manually takes time
- This script allows you to provide a users Github username and it will clone their repositories into a sub-folder of their username
- By default the script downloads the users 5 repositories that have been created most recently
    - This can be customised using the '--maxrepos' flag (see Usage section below)

- This script is useful for companies who need to review a job candidates portfolio to easily review their work

## Requirements

- Python
- Git (Installing Git)[https://git-scm.com/book/en/v2/Getting-Started-Installing-Git]

## Usage

### Platforms 

- This script has been tested, and currently works on:
- Linux

- Testing on other platforms will be carried out and this section will be updated

### Running

- Run 'python3 getrepos.py -username <username>'
    - Example: 'python3 getrepos.py -username jstriker87'

### Command line arguments

- '-username' - Mandatory: Provides username of the Github user that you wish to clone their repositories
- '--maxrepos' - Allows you to specify the number of repositories of the user to clone (default 5)

### Future plans

- Future updates will allow users to provide a file with a users Github username and optionally their first name and last name
    - The script will then process each users and if a first and last name has been provided the repositories will be created under a folder with the users name and Github username (e.g JohnSmith-jsmith99)

## License
Licensed under the [GNU GENERAL PUBLIC LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html)
You can find a copy of it in [LICENSE](LICENSE).
