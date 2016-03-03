# MassSpec_parser
A python library to parse Mass Spectrometry results and annotate with TAIR accessions

## Requirements
- Python3
- Numpy
- Biopython

## Installation
If you don't have yet the requirements installed:
#### Install Python3:
https://www.python.org/downloads/

If you are using Windows, you might have to add the path to Python
into your path variable.

#### (FOR WINDOWS) Install Microsoft Visual C++ compiler for Python3:
https://www.microsoft.com/en-us/download/details.aspx?id=44266

#### Install Pip (for easyer python module installation):
https://pip.pypa.io/en/stable/installing/

#### Install numpy module:
`pip install numpy`

#### Install biopython module:
`pip install biopython`

#### Verify that everything is all set:
\# In the command line:

`python`

\# In the python interpreter

`import numpy`

`import Bio`

## Usage
python ms_summary.py [-h] -i INPUTS -d DBBLAST [-b BACKGROUND] [-c CPUS] [-o OUTFOLDER] [-p PATHBLAST]

Arguments:

  * -h, --help

  show this help message and exit

  * -i INPUT, --inputs INPUT

  CSV file of MS results. At least 2 should be given.

  * -d DBBLAST, --dbBlast DBBLAST

  A database in fasta format to blast against and then create the mapping.

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
