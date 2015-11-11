import os
import csv
import itertools

#-------------------------------------------------------------------------------
def getMap( blastouts, isoform=True ):
    """
    From a list blast result (Sequences of the GIs of the MS against
    TAIR db) files in tab format, get a dictionnary for mapping MS' GIs to TAIRS.
    Set Isoform to "True" if the blast results are giving TAIRs such as "AT5G10160.1"
    (if "AT5G10160" then isoform=False )
    """
    
    TAIRmap = {}
    for bres in blastouts:
        with open(bres, "r") as f:
            
            for line in f:
                line = line.strip()
                gi = line.split('|')[1]
                tair = line.split()[1]
                
                if isoform:
                    tair = tair.split('.')[0]
                    
                if gi in TAIRmap:
                    pass
                else:
                    TAIRmap[gi] = tair

    print "Total of TAIR/GI mapping: %s" % (len(TAIRmap))
    return TAIRmap

#-------------------------------------------------------------------------------
def translateGIs(dataFile, TAIRmap):
    """
    From a csv file of MS results, return a set of TAIR IDs after
    mapping the GIs to the corresponding TAIRS
    GIs should be in column 3 of the MS results
    """
    
    TAIRset = set()
    missing_TAIR = 0
    
    with open(dataFile, "r") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        next(reader)
        for row in reader:
            gi = row[2].replace('gi|', '')

            if gi in TAIRmap:
                TAIRset.add( TAIRmap[gi] )
            else:
                missing_TAIR += 1

    print "\nFile: %s" % (dataFile)
    print "GIs missing TAIRs:%d" % (missing_TAIR,)
    print "Total TAIRs: %s" % (len(TAIRset))
    return TAIRset

#-------------------------------------------------------------------------------
def getAllGIs(dataList, TAIRmap):
    """
    From a list of MS results (.csv), return a dictionnary with the
    name of the file as key and the set of TAIRs present as value.
    """
    
    TAIRsDict = {}
    for dataFile in dataList:
        TAIRs = translateGIs(dataFile, TAIRmap)
        TAIRsDict[dataFile] = TAIRs
        
    return TAIRsDict

#-------------------------------------------------------------------------------
def compareTAIRs(dataList, TAIRmap, outfolder, background=False):
    """
    From a dict of MS_files:TAIRS_set, write a res_output.csv file with
    a comparison of the TAIRS content.  Return a set of TAIRs which
    are common to all MS results and with background removed (if
    background present)
    """

    outputF = os.path.join(outfolder, "res_output.csv")
    data_d = getAllGIs(dataList, TAIRmap)
    comparisons = itertools.combinations(data_d.keys(), 2)
    
    with open(outputF, "w") as f:
        for i, j in comparisons:
            print "\nComparing %s and %s..." % (i,j)
            commons = data_d[i] & data_d[j] 
            f.write( 'Common to:%s-%s\n' % (i,j) + '\n'.join(sorted(commons)) + '\n')
        common_to_all = set.intersection(*data_d.values())
        f.write( 'Common to all:\n' + '\n'.join(sorted(common_to_all)) + "\n")

        if background:
            back_d = getAllGIs(background, TAIRmap)
            common_back_TAIRs = set.intersection(*back_d.values())
            common_to_all_back_removed = common_to_all - common_back_TAIRs
            f.write( 'Common to all without background:\n'
                     + '\n'.join(sorted(common_to_all)) + "\n" )
            
            return [ common_to_all, common_to_all_back_removed ]
    return [ common_to_all ] 

#-------------------------------------------------------------------------------
def print_original_Data(dataList, TAIRmap, background=False):
    """
    A modified version of printOriginalData which print columns for
    each input files and put 1 if the TAIR (gi) is present in the
    corresponding file or 0 if not
    """
    
    if background:
        data_d = getAllGIs(dataList + background, TAIRmap)
    else:
        data_d = getAllGIs(dataList, TAIRmap)
        
    infiles = sorted(data_d.keys())
    
    for dataFile in dataList:
        csvOut = dataFile + "modif.csv"
        with open(dataFile, "r") as f:
            reader = csv.reader(f, delimiter=",", quotechar='"')
            
            with open(csvOut, "wb") as fout:
                writer = csv.writer(fout, delimiter=",", quotechar='"')
                header = next(reader) + ["TAIR"] + infiles
                writer.writerow(header)

                for row in reader:
                    gi = row[2].replace('gi|','')
                    if gi in TAIRmap:
                        TAIR = (TAIRmap[gi])
                        row.append(TAIR)

                        for infile in infiles:
                            row.append("1") if TAIR in data_d[infile] else row.append("0")

                    else:
                        row.append("NO MAPPING TO TAIR")
                        
                    writer.writerow(row)

#-------------------------------------------------------------------------------
def printOriginalData(common_to_all, dataFile, TAIRmap, csvOut):
    """
    Print the original data of a MS file, filtering out the TAIRs not
    in common_to_all.
    """

    with open(dataFile, "r") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        next(reader)

        with open(csvOut, "wb") as fout:
        
            writer = csv.writer(fout, delimiter=",", quotechar='"')
            for row in reader:
                gi = row[2].replace('gi|','')
                if gi in TAIRmap:
                    if TAIRmap[gi] in common_to_all:
                        row.append(TAIRmap[gi])
                        writer.writerow(row)
