#!/bin/bash
set -e
REPO_NAME="autogen-retail-agent-demo"
GITHUB_URL="https://github.com/YOUR_USERNAME/$REPO_NAME.git"
git init
git remote add origin $GITHUB_URL
git add .
git commit -m "Initial commit: AutoGen retail agent project"
git branch -M main
git push -u origin main
