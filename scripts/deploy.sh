#!/bin/bash
set -e

# Vars
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR=$SCRIPT_DIR/..

python $SCRIPT_DIR/build_readme_and_index_html.py "$@"