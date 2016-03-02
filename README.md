# MassSpec_parser
A python library to parse Mass Spectrometry results and annotate with TAIR accessions

## Requirements
- Python2.7
- Numpy
- Biopython

## Installation
If you don't have yet the requirements installed:
#### Install Python 2.7:
https://www.python.org/downloads/

If you are using Windows, you might have to add the path to Python
into your path variable.

#### (FOR WINDOWS) Install Microsoft Visual C++ compiler for Python 2.7:
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
python ms_summary.py [-h] -i [INPUTS [INPUTS ...]] [-b [BACKGROUND [BACKGROUND ...]]] -d DBBLAST [-c CPUS] [-o OUTFOLDER]                                                                          
Arguments:

-h, --help: show this help message and exit

-i [INPUTS [INPUTS ...]], --inputs [INPUTS [INPUTS ...]]: CSV files of MS results. At least 2 should be given.

-b [BACKGROUND [BACKGROUND ...]], --background [BACKGROUND [BACKGROUND ...]]: CSV files for the background.

-d DBBLAST, --dbBlast DBBLAST: A database in fasta format to blast against and then create the mapping

-c CPUS, --cpus CPUS  Number of cpus to use for blast

-o OUTFOLDER, --outfolder OUTFOLDER: Folder where the output will be regenerated. Will be created if doesn't exist.

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
