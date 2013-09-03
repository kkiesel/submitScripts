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

Submit the jobs with ```condor_submit condorSettingsSignal```
Check the status with ```condor_q -submitter $USER```

