#! /usr/bin/env python
import os
import argparse
import imp
import shutil
from django.conf import settings

if __name__ == '__main__':
    # using the CLI
    from libs import get_from_gi as gg
    from libs import tair_ms_parse as ms
    WDIR = ''
else:
    # Using django web
    from .libs import get_from_gi as gg
    from .libs import tair_ms_parse as ms
    WDIR = settings.MEDIA_ROOT


def checkForOutFolder(outfolder):
    if os.path.isdir(outfolder):
        print("The results will be in the already existent folder: %s" % outfolder)
    else:
        print("Creating the folder %s\n The results will be there." % outfolder)
        os.makedirs(outfolder)


def checkInputExist(data):
    for inFile in data:
        if not os.path.isfile(inFile):
            raise IOError("Are you sure that the file %s exists ?" % inFile)


def checkDependencies():
    # Check if necessary modules are installed
    imp.find_module('Bio')

    # Check if blast is installed
    if not shutil.which('makeblastdb'):
        raise OSError("Are you sure blast+ is installed ?")
    #distutils.spawn.find_executable("blastp")


def run_compare_cli(data, background, col_num, db,
                    outfolder, email, cpus=1, path_blast=''):

    # TODO This could possibly be improved
    if WDIR:
        os.chdir(WDIR)
    db = db[0]

    checkForOutFolder(outfolder)
    checkInputExist(data)
    gg.format_db(db, "prot")

    blast_outs = []

    for csvF in data + background:
        fas_name = os.path.join(outfolder,
                                os.path.basename(
                                    os.path.splitext(csvF)[0])) + ".fas"

        gis = gg.getGIs(csvF, col_num)
        gg.getFastaFromGIs(gis, fas_name, email)

        blastout_name = os.path.join(outfolder,
                                     os.path.basename(
                                        os.path.splitext(csvF)[0])) + ".tab"

        gg.do_blastP(fas_name, db, blastout_name, cpus, 6, path_blast)
        blast_outs.append(blastout_name)

    TAIRmap = ms.getMap(blast_outs)
    ms.print_original_Data(data, TAIRmap, col_num, outfolder, background=background)


if __name__ == '__main__':
    # FIXME Currently the CLI without the web interface will not work

    parser = argparse.ArgumentParser(prog="python ms_summary.py")
    parser.add_argument("-i", "--input", action='append',
                        help="CSV files of MS results. At least 2 should be given.",
                        required=True)

    parser.add_argument("-d", "--dbBlast", action='append',
                        help="""A database in fasta format
                        to blast against and then create the mapping""",
                        required=True)

    parser.add_argument("-b", "--background", action='append',
                        help="CSV files for the background.",
                        default=[])

    parser.add_argument("-c", "--cpus",
                        help="Number of cpus to use for blast",
                        default=1)

    parser.add_argument("-o", "--outfolder",
                        help="""Folder where the output will be regenerated.
                        Will be created if doesn't exist""",
                        default="MS_parse_out")

    parser.add_argument("-p", "--pathBlast",
                        help="""Folder where the blast+ executables are located,
                        if not specified, will look in the environment PATH""",
                        default='')
    parser.add_argument("-e", "--email",
                        help="Email mandatory for Entrez queries (GI lookup).",
                        required=True)

    args = parser.parse_args()

    checkDependencies()

    if len(args.input) < 2:
        raise IOError("At least 2 csvs files are required to compute a common set of TAIRS")

    run_compare_cli(args.input, args.background, 2,
                args.dbBlast, args.outfolder,
                args.email, args.cpus, args.pathBlast)
