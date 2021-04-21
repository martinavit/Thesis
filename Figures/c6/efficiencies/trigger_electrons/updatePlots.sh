#!/bin/zsh
sourceDir=/user/tomc/public_html/leptonSF/trigger_HNL/

function copy {
  cd $2
  for f in **/*.png; do
    sourceFile=$1/$f
    if [ -f $sourceFile ]; then
      echo "Updating $f"
      cp -u $1/$f $f
    fi
  done
  cd -
}

copy $sourceDir .
