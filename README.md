# README
## susyNtuplizer

* set CMSSW environment
* comment out the datasets you want to use
* create the multicrab configuration file with
```
python2 createMulticrabConfiguration.py
```
* check the output!
* run
```
multicrab -cfg multicrab_gen.cfg -create -submit
```
