#! /usr/bin/env python

from lib import get_from_gi as gg
from lib import tair_ms_parse as ms
import os
import argparse

if __name__ == '__main__':
    """
    From a csv with a list of gis, get a multifasta with the
    corresponding sequences.
    Params: 
    - col number where to find the GIs in the csv
    """

    ################################################################################
    parser = argparse.ArgumentParser(prog="python ms_summary.py")
    parser.add_argument("-i","--inputs",nargs="*", help="CSV files of MS results. At least 2 should be given.", required=True )
    parser.add_argument("-b", "--background", nargs="*", help="CSV files for the background.") 
    parser.add_argument("-d", "--dbBlast", help="""A database in fasta format 
    to blast against and then create the mapping""", required=True)
    parser.add_argument("-c", "--cpus", help="Number of cpus to use for blast")
    parser.add_argument("-o", "--outfolder", help="Folder where the output will be regenerated. Will be created if doesn't exist", default="MS_parse_out")
    args = parser.parse_args()
    ################################################################################
    
    if len(args.inputs) < 2:
        raise IOError("At least 2 csvs files are required to compute a common set of TAIRS")

#Column where to find the gis in the csv (index starting at 0)
    COL_NUM = 2
    DB = args.dbBlast
    BACKGROUND = args.background
    DATA = args.inputs
    OUTFOLDER = args.outfolder

    if os.path.isdir(OUTFOLDER):
        print "The results will be in the already existent folder: %s" % OUTFOLDER
    else:
        print "Creating the folder %s\n The results will be there." % OUTFOLDER
        os.makedirs(OUTFOLDER)
    
    for inFile in DATA:
        if not os.path.isfile(inFile):
            raise IOError("Are you sure that the file %s exists ?") % inFile 

    gg.format_db(DB, "prot")

    blast_outs = []
    outPathFor = lambda x: os.path.join( OUTFOLDER,
                                      os.path.basename (os.path.splitext(x)[0] ))
    
    for csvF in DATA + BACKGROUND:
         fas_name = outPathFor(csvF) + ".fas"
         gis = gg.getGIs(csvF, COL_NUM)
         gg.getFastaFromGIs(gis, fas_name)

         blastout_name = outPathFor(csvF) + ".tab"
         gg.do_blastP(fas_name, DB, blastout_name, 2)
         blast_outs.append(blastout_name)

    TAIRmap =  ms.getMap(blast_outs)
    common_to_all = ms.compareTAIRs( DATA, TAIRmap, OUTFOLDER, background=BACKGROUND )

    for csvF in DATA:
        csvOut = outPathFor(csvF) + "_with_background.csv"
        ms.printOriginalData( common_to_all[0], csvF, TAIRmap, csvOut )

        if BACKGROUND:
            csvOut = outPathFor(csvF) + "_background_removed.csv"
            ms.printOriginalData( common_to_all[1], csvF, TAIRmap, csvOut )
