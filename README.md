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
