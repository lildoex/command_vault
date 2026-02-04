#!/bin/bash

# Prompt user for input
read -p "Enter Linux command: " CMD
read -p "Enter description: " DESCRIPTION

# Send data to the Flask server
curl -s -X POST -H "Content-Type: application/json" \
     -d "{\"cmd\": \"$CMD\", \"description\": \"$DESCRIPTION\"}" \
     http://127.0.0.1:5000/api/commands > /dev/null

echo "Success: Command saved to CommandVault!"