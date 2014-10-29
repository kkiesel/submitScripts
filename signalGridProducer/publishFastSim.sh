#!/bin/bash

for job in crab/GGM_*; do
    crab -c $job -publish
done
