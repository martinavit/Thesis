#!/bin/zsh
sourceDir=/user/tomc/public_html/hnl/

function copy {
  cd $2
  for f in **/*.pdf; do
    sourceFile=$1/$f
    if [ -f $sourceFile ]; then
      if [[ $sourceFile -nt $f ]]; then
        echo "Updating $f"
        cp -u $1/$f $f
      fi
    fi
  done
  cd -
}

copy $sourceDir .
