#!/bin/env bash

pip install -r python/requirements.txt

git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status