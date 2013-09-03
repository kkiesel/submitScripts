#!/bin/bash

. /uscmst1/prod/sw/cms/shrc prod

export SCRAM_ARCH=slc5_amd64_gcc462

cd ~/CMSSW_5_3_8_patch3/src
echo "Set cmssw environment"
eval `scramv1 runtime -sh`
cd

inputPath=/eos/uscms/store/user/lpcpjm/PrivateMC/FastSim/525p1/Spectra_gsq_W/SusyNtuple/cms533v1_v1/

echo "input path"
echo $inputPath

#for file in $(ls $inputPath)
#do
#	~/singlePhoton/TreeWriter/executable out$file $inputPath$file
#done

echo "is file there?"
ls /afs/cern.ch/user/k/kiesel/public/qcdWeight.root

file=tree_1000_1020_375.root
~/singlePhoton/TreeWriter/executable out$file $inputPath$file

