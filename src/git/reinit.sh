#!/bin/bash

# Configuration file
QUINES_CONFIG_FILE="quinerepo.json"

# Function to initialize and run a quine
run_quine() {
  local quine_name=$1
  local branch=$2
  local parameters=$3
  local new_branch="quine-$RANDOM"

  # Create and checkout a new branch
  git checkout -b "$new_branch"

  # Reinitialize the branch
  eval $(ssh-agent)
  ssh-add /home/tp/.ssh/id_rsa
  git add .
  git commit -m "Initial commit"
  git branch -m development # rename master to development
  git remote set-url origin git@github.com:Phovos/quine.git # update SSH URL
  git push origin HEAD:master

  # Checkout the new branch and run the quine
  git checkout "$new_branch"
  echo "Invoking Quine $quine_name with parameters: $parameters"
  python quine.py $parameters

  # Clean up the branch after execution
  git branch -D "$new_branch"
}

# Load configuration file and run quines in parallel
while IFS= read -r line; do
  if [[ $line =~ "\"name\":\"" ]]; then
    quine_name=$(echo $line | jq -r '.name')
    branch=$(echo $line | jq -r '.branch')
    parameters=$(echo $line | jq -r '.parameters | join(" ")')

    # Run each quine in the background
    run_quine "$quine_name" "$branch" "$parameters" &
  fi
done < <(jq -c '.[]' "$QUINES_CONFIG_FILE")

# Wait for all background processes to complete
wait
