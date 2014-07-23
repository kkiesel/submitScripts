#!/bin/bash

version=V03.$2
inputPath=$1

echo Get final plots for all samples with version $version

echo set prod
. /uscmst1/prod/sw/cms/shrc prod

echo export
export SCRAM_ARCH=slc5_amd64_gcc462

echo cd to folder
cd /uscms_data/d1/kiesel/CMSSW_5_3_8_patch3/src
echo eval
eval `scramv1 runtime -sh`
echo now cd to working dir
cd ${_CONDOR_SCRATCH_DIR}
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:`pwd`

echo in this directory there is
ls
echo path is now:
echo $PATH
echo inputpath:
echo $inputPath
abbr=${inputPath:65:1}_gsq

if [[ "$inputPath" == "/uscms_data/d1/y/wino/" ]]; then
	abbr='W_gsq2'
fi
echo $abbr

for file in $(ls $inputPath)
do
	./treeWriter out${abbr}_$version$file $inputPath$file
done

echo now add the samples
hadd -f -k ${abbr}_$version.root out${abbr}_$verion*root

rm out${abbr}_${version}*root

