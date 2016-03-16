# MassSpec_parser
A python library to parse Mass Spectrometry results and annotate with TAIR accessions

## Installation with Docker
- Install Docker

https://docs.docker.com/

In Docker:

`docker run /khourhin/bioinfo -p 8000:8000 -v OUTFOLDER_ON_YOUR_COMPUTER:/usr/src/user_data -d /khourhin/bioinfo`

### On Windows
To get the IP to check with your browser:

`docker-machine ip`

Open your internet browser with URL:

PREVIOUS_STEP_IP:8000

### On Linux (and Mac I guess)
Open your internet browser with URL:

localhost:8000

## Classical Installation

### Requirements
- Python3
- Numpy
- Biopython
- blast+

For the web platform version:
- django 1.9.4
- django-forms-bootstrap

## Command line Usage
python ms_summary.py [-h] -i INPUTS -d DBBLAST [-b BACKGROUND] [-c CPUS] [-o OUTFOLDER] [-p PATHBLAST]

Arguments:

  * -h, --help

  show this help message and exit

  * -i INPUT, --inputs INPUT

  CSV file of MS results (more than one can be given). One csv at least is required.

  * -d DBBLAST, --dbBlast DBBLAST

  A database in fasta format to blast against and then create the mapping. One fasta is required.

  * -b BACKGROUND, --background BACKGROUND

  CSV file for the background (more than one can be given).

  * -c CPUS, --cpus CPUS

  Number of cpus to use for blast.
  * -o OUTFOLDER, --outfolder OUTFOLDER

  Folder where the output will be regenerated. Will be created if doesn't exist.

  * -p PATHBLAST, --pathBlast PATHBLAST

  Folder where the blast+ executables are located, if not specified, will look in the environment PATH.

## Web interface Usage
`python3 manage.py runserver`

Then go to your web browser and go the URL:

http://localhost:8000/

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History
TODO

## Credits
TODO

## License
TODO
