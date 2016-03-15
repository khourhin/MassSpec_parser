import os
import csv


def getMap(blastouts, isoform=True):
    """
    From a list blast result (Sequences of the GIs of the MS against TAIR db)
    files in tab format, get a dictionnary for mapping MS' GIs to TAIRS.
    Set Isoform to "True" if the blast results are giving TAIRs
    such as "AT5G10160.1" (if "AT5G10160" then isoform=False )
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

    print("Total of TAIR/GI mapping: %s" % (len(TAIRmap)))
    return TAIRmap


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
                TAIRset.add(TAIRmap[gi])
            else:
                missing_TAIR += 1

    print("\nFile: %s" % (dataFile))
    print("GIs missing TAIRs:%d" % (missing_TAIR,))
    print("Total TAIRs: %s" % (len(TAIRset)))
    return TAIRset


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


def print_original_Data(dataList, TAIRmap, col_num, outfolder,
                        background=False):
    """
    Print columns for
    each input files and put 1 if the TAIR (gi) is present in the
    corresponding file or 0 if not
    """

    if background:
        data_d = getAllGIs(dataList + background, TAIRmap)
    else:
        data_d = getAllGIs(dataList, TAIRmap)

    infiles = sorted(data_d.keys())

    for dataFile in dataList:
        csvOut = os.path.basename(os.path.splitext(dataFile)[0])
        csvOut = os.path.join(outfolder, csvOut + "_out.csv")

        with open(dataFile, "r") as f:
            reader = csv.reader(f, delimiter=",", quotechar='"')

            with open(csvOut, "w", newline='') as fout:
                writer = csv.writer(fout, delimiter=",", quotechar='"')
                header = next(reader)  # + ["TAIR"] + infiles
                writer.writerow(header)

                for row in reader:
                    gi = row[col_num].replace('gi|', '')
                    if gi in TAIRmap:
                        TAIR = (TAIRmap[gi])
                        row.append(TAIR)

                        for infile in infiles:
                            if TAIR in data_d[infile]:
                                row.append("1")
                            else:
                                row.append("0")

                    else:
                        row.append("NO MAPPING TO TAIR")

                    writer.writerow(row)
