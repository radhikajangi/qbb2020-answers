#!/bin/bash

for end in { 83 86 88 89 90 93 94 97 }
do
ktImportText -o day${end}.krona.html day${end}.kraken
done
