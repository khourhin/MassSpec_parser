from Bio import Entrez
from Bio import SeqIO
import os
import csv
import subprocess

PATH_BLAST = '/home/tiennou/Documents/Taff/softwares/RNA-seq/blast+/bin/'
Entrez.email = 'ekornobis@gmail.com'

#-------------------------------------------------------------------------------
def getGIs(gis_csv, col_num):
    """
    Get the GIs from a csv file, specifying the number of the column
    where to find them (col index starting at 0)
    """
    gis = []

    with open(gis_csv, 'r') as f:
        next(f)
        for row in csv.reader(f):
            gis.append(row[col_num])

    print "Found %s GIs in csv %s" % (len(gis), gis_csv)
    return gis

#-------------------------------------------------------------------------------
def getFastaFromGIs(gis_list, fout_name):
    """
    From a list of GIs (as string) get a multifasta with name fout_name + ".fas"
    """

    if os.path.isfile(fout_name):
        print "Fasta file %s already existing, using it for next steps ..." % fout_name
        return False

    # Get data from NCBI
    handle = Entrez.efetch(db='protein', id=gis_list,
                           rettype='fasta', retmode='text')

    with open(fout_name, "w") as fout:
        count = 0
        for record in SeqIO.parse(handle, 'fasta'):
            count += 1
            fout.write('>' + record.id + record.description + "\n")
            fout.write(str(record.seq) + "\n")

    handle.close()
    print "Written %s sequences to %s" % (count, fout_name)

#-------------------------------------------------------------------------------
def format_db(fasta, dbtype='prot', path_blast=''):
    """
    Format a fasta file for having them as db for blast+
    dbtype can be 'nucl' or 'prot'
    """
    if all( [ os.path.isfile(x)
              for x in [fasta + ".phr", fasta + ".pin", fasta + ".psq"] ] ):
        print "Already formated database for %s" % fasta
        return False

    print "Formatting db for %s" % fasta
    cmd = [path_blast + 'makeblastdb', '-dbtype', dbtype, '-in', fasta ]
    proc = subprocess.Popen( cmd, stdout=subprocess.PIPE)
    out, err = proc.communicate()

    return out, err

#-------------------------------------------------------------------------------
def do_blastP(query, db, outfile, cpus, fmt=6, path_blast=''):
    """
    Launched a blastp analysis for the [query] against the [db]
    """
    if os.path.isfile(outfile):
        print "Seems like the blast results are already present: %s" % outfile
        print "This file will be therefore used for further computations."
        return False

    print "Starting BlastP"
    cmd = [path_blast + 'blastp', '-query', query, '-db', db, '-out', outfile,
           '-outfmt', str(fmt), '-evalue', '1e-6', '-num_threads', str(cpus) ]

    print " ".join(cmd)
    proc = subprocess.Popen( cmd, stdout=subprocess.PIPE)
    out, err = proc.communicate()
