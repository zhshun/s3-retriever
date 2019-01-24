#!/bin/bash

SCRIPTDIR=`/usr/bin/dirname $0`
if [ "$SCRIPTDIR" != "." ]; then
  cd $SCRIPTDIR
fi
SCRIPTDIR=`/bin/pwd`
cd $SCRIPTDIR

if `which pip3 >/dev/null 2>&1`; then
  pip3 install boto3 >/dev/null 2>&1
else
  pip install boto3 >/dev/null 2>&1
fi

if `which python3 >/dev/null 2>&1`; then
  python3 retrieve.py
else
  python retrieve.py
fi
