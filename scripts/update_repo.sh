# !/bin/bash

source run_or_fail.sh

# remove existing .commit_id - we only want this file to exist if there is a new commit ID anyhow
bash rm -f .commit_id

# verify the target repo exists, then reset it to the most recent commit to preserve sync
run_or_fail "Repo directory not found" pushd $1 1> /dev/null
run_or_fail "Could not reset git" git reset --hard HEAD

# call git log, then parse the output
COMMIT=$(run_or_fail "Could not call 'git log' on repository" git log -n1)
if [ $? != 0]; then
    echo "Could not call 'git log' on repository"
    exit 1
fi
COMMIT_ID=`echo $COMMIT | awk '{ print $2 }'`

# pull from repo, getting most recent changes and newest commit ID
run_or_fail "Could not pull from repository" git pull
COMMIT=$(run_or_fail "Could not call 'git log' on repository" git log -n1)
if [ $? != 0]; then
    echo "Could not call 'git log' on repository"
    exit 1
fi
NEW_COMMIT_ID=`echo $COMMIT | awk '{ print $2 }'`

# if the most recent commit ID has changed, write it to .commit_id
if [ $NEW_COMMIT_ID != $COMMIT_ID ]; then
    popd 1> /dev/null
    echo $NEW_COMMIT_ID > .commit_id
fi
