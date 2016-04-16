#!/bin/sh
set -e
wrapper=$(command -v gcc-rtags-wrapper.sh)
dir=$(mktemp -d)
pushd $dir

for binary in gcc cc g++ c++; do
    ln -s $wrapper $binary
done

popd

PATH=$dir:$PATH

case $1 in
    waf) shift
        python2 waf configure
        python2 waf;;
    *)  make $@;;
esac

rm -rf $dir
