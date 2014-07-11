# README
## susyNtuplizer

* set up the CMSSW and the [nTuplizer](https://github.com/CMSSUSYPhotons/SUSYPhotonAnalysis/tree/master/SusyNtuplizer)
* comment out the datasets you want to use in ```rawMulticrab.cfg```
* create the multicrab configuration file with
```
python2 createMulticrabConfiguration.py
```
* check the output!
* run
```
multicrab -cfg multicrab_gen.cfg -create -submit
```

## condor

* set upt the [treeWriter](https://github.com/kkiesel/singlePhoton/tree/master/TreeWriter)
* check the settings in executable.cc
* compile treeWriter

Submit the jobs with

condor_submit condorSignal.jdl -a 'Arguments = /eos/uscms/store/user/lpcpjm/PrivateMC/FastSim/525p1/Spectra_gsq_W/SusyNtuple/cms533v1_v1/ 03'
condor_submit condorSignal.jdl -a 'Arguments = /eos/uscms/store/user/lpcpjm/PrivateMC/FastSim/525p1/Spectra_gsq_W/SusyNtuple/cms533v1_v1/ 03'
condor_submit condorSignal.jdl -a 'Arguments = /uscms_data/d1/y/wino/ 03'

Check the status with ```condor_q -submitter $USER```
For more information, see http://www.uscms.org/uscms_at_work/computing/setup/batch_systems.shtml
