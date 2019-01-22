#!/bin/bash

SCRIPTDIR=`/usr/bin/dirname $0`
if [ "$SCRIPTDIR" != "." ]; then
  cd $SCRIPTDIR
fi
SCRIPTDIR=`/bin/pwd`
cd $SCRIPTDIR

pip install s3 >/dev/null 2>&1
pip install yaml >/dev/null 2>&1

python retrieve.py
