#!/bin/env python
import os
import re
import glob
import string

from optparse import OptionParser


cfgTemplateName = "Signal_cff_template_GEN_FASTSIM_HLT_PU.py"
crabTemplateName = "crab.cfg"

def createFromTemplate( d, templateFilename, outFilename  ):
   o = open(outFilename,"w+")
   data = open(templateFilename).read()
   tem=string.Template(data)
   data=tem.safe_substitute(d)
   o.write(data)
   o.close()

def prepareFastSim( lhaDir ):

    # absolute path
    absLhaDir = os.path.abspath( lhaDir )

    tmpFolder = "crab"
    #os.mkdir( tmpFolder )
    os.chdir( tmpFolder )

    for file in glob.glob( absLhaDir+"/*.slha" ):
        baseFilename = os.path.basename( file )

        # Determine Scan
        nlsp = ""
        if "Spectra_gsq_B" in lhaDir: nlsp = "Bino_"
        if "Spectra_gsq_W" in lhaDir: nlsp = "Wino_"

        # Determine Masses
        match = re.match( ".*/M3_(\d+)_msq_(\d+)_M._375.slha", file )
        if not match:
            print "coud not match", file
            continue
        mgluino, msquark = match.groups()

        cfgReplacementDict = { "SLHA": "SLHAFILE = \\'../{0}\\'".format( baseFilename ) }
        createFromTemplate( cfgReplacementDict, "../"+cfgTemplateName, cfgTemplateName )

        crabReplacementDict = { "NAME": "GGM_{0}Sq{1}_Gl{2}_8TeV_FastSim".format( nlsp, msquark, mgluino ),
                                "INPUTFILE": "{0}/{1}".format( absLhaDir, baseFilename )
                              }
        createFromTemplate( crabReplacementDict, "../"+crabTemplateName, crabTemplateName )

        forceRedo = ["GGM_Wino_Sq2000_Gl920_8TeV_FastSim","GGM_Wino_Sq800_Gl620_8TeV_FastSim","GGM_Wino_Sq700_Gl520_8TeV_FastSim","GGM_Wino_Sq1700_Gl820_8TeV_FastSim","GGM_Wino_Sq600_Gl1220_8TeV_FastSim","GGM_Wino_Sq2000_Gl2020_8TeV_FastSim","GGM_Wino_Sq1200_Gl420_8TeV_FastSim","GGM_Wino_Sq1700_Gl1320_8TeV_FastSim" ]
        if not os.path.exists(crabReplacementDict["NAME"]):
            if crabReplacementDict["NAME"] in forceRedo:
                os.system( "crab -create -submit" )

if (__name__ == "__main__"):
    # use option parser to allow verbose mode
    parser = OptionParser()
    parser.add_option( "--lhaDir", default="Spectra_gsq_W",
                                  help="path to the directory containing folders with the lhe files")
    (opts, args) = parser.parse_args()

    prepareFastSim(opts.lhaDir)
