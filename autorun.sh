#!/bin/bash

dirname "$0"
python3 scripts/extract_streams.py > dailymotion.m3u
echo m3u grabbed

#dirname "$0"
#python3 scripts/pull_guides.py
#echo xmltv obtained
