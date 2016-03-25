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

make $@

rm -rf $dir
