
#!/bin/sh

# project_nuke.sh: opens nuke  with the project environment

# source project environment
DIR=`dirname $0`
source ${DIR}/project_env.sh

export CURRENT_PROG='SubstancePainter'

# Change directories so current directory is not in the tools folder
#cd ${USER_DIR}

echo "Starting Substance Painter..."
substancepainter
