#!/bin/zsh
sourceDir=/user/tomc/public_html/hnl/danielePlots/

function copy {
  cd $2
  for f in **/*.pdf; do
    sourceFile=$1/$f
    if [ -f $sourceFile ]; then
      if [[ $sourceFile -nt $f ]]; then
        echo "Updating $f"
        cp -u $1/$f $f
        cp -u $1/${f%.pdf}.root ${f%.pdf}.root
      fi
    fi
  done
  cd -
}

copy $sourceDir .
