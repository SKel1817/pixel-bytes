#!/bin/bash

# Iterate over all screen sessions and terminate them properly
screen -ls | grep -E "Detached|Dead" | awk '{print $1}' | while read -r session_id; do
  screen -S "$session_id" -X quit
done

# Wipe out any remaining dead screens
screen -wipe

