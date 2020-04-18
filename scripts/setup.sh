#!/bin/bash
set -e

# Vars
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR=$SCRIPT_DIR/..

# Install deps
echo "*** Install deps ***"
pip install -r $SCRIPT_DIR/requirements.txt

