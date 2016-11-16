# MassSpec_parser
A python library to parse Mass Spectrometry results and annotate
with TAIR accessions

## Overview
### Input
- "MS infiles": At least one csv file with Mass Spectrometry results (with the GI accession number in the 3rd column). **MANDATORY**
- "Blast db": One fasta file to blast against for "blast db". **MANDATORY**
- "MS background": Csv files of background signal. OPTIONAL

### Workflow
1.  The program will extract the GI accession numbers (currently,
    the GIs **HAVE TO BE** the 3rd column of your csv files)

2. Sequences corresponding to the GIs will be extracted from Entrez and blasted
  against the reference given as "blast db".

3. The best hits (highest scores) will be then reported together with the
original Mass Spectrometry data in the `_out.csv` file. Blast results can be
found in the `.tab` file.

4. If you specify more than one file as "ms infiles", then the `_out.csv` file
will display columns showing the presence (1) or absence (0) of a particular
protein in the datasets given as infiles.

## Usage with Docker
- Install Docker

https://docs.docker.com/

- In Docker:

`docker run -p 8000:8000 -v OUTFOLDER_ON_YOUR_COMPUTER:/usr/src/user_data -d khourhin/bioinfo`

### On Windows
To get the IP of your localhost by typing in the command line:

`docker-machine ip`

Open your internet browser, and type as URL:

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

### Web interface Usage
`python3 manage.py runserver`

Then go to your web browser and go the URL:

http://localhost:8000/

### Command line Usage
python3 ms_summary.py [-h] -i INPUTS -d DBBLAST [-b BACKGROUND] [-c CPUS] [-o OUTFOLDER] [-p PATHBLAST]

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
