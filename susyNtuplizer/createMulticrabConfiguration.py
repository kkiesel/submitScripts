#!/usr/bin/python2
import ConfigParser
import os

filename = "multicrab_gen.cfg"
inputFile = "rawMulticrab.cfg"
version = "V02"

total_number_of_events = -1
events_per_job = 50000

total_number_of_lumis = -1
lumis_per_job = 200

pset = os.environ['CMSSW_BASE']+"/src/SUSYPhotonAnalysis/SusyNtuplizer/runOverAOD_CommandLine.py"

conf = ConfigParser.SafeConfigParser()
conf.read( inputFile )

output = """## This file was generated by create_multicrab.py.
[MULTICRAB]
cfg = crab.cfg

[COMMON]
USER.email = %s@cern.ch
"""%os.environ['USER']

for section in conf.sections():
    output += "\n[%s_%s]\n"%( section, version )
    output += "CMSSW.datasetpath = %s\n"%conf.get( section, "datasetpath" )
    output += "CMSSW.pset = %s\n"%pset
    output += "CMSSW.pycfg_params = dataset=%s\n"%conf.get( section, "dataset" )
    if conf.has_option( section, "lumi_mask" ):
        output += "CMSSW.total_number_of_lumis = %s\n"%total_number_of_lumis
        output += "CMSSW.lumis_per_job = %s\n"%lumis_per_job
        output += "CMSSW.lumi_mask = %s\n"%conf.get( section, "lumi_mask" )
    else:
        output += "CMSSW.total_number_of_events = %s\n"%total_number_of_events
        output += "CMSSW.events_per_job = %s\n"%events_per_job

f = open( filename, "w")
f.write( output )
f.close()
print "Multicrab configuration file '%s' created."%filename
print output

