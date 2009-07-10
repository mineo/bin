#!/bin/sh
# ----------------------------------
# updates git-/svn-/hg-/bzr-packages
# in /var/abs/local/yaourtbuild
# ----------------------------------
cd /var/abs/local/yaourtbuild/
for i in `ls | grep "svn\|git\|hg\|bzr"`;do
	cd $i
	$(pwd)
	rm *pkg.tar.gz
	makepkg
	cd ..
done
for i in `ls | grep "svn\|git\|hg\|bzr`;do
	cd $i
	yaourt -U *pkg.tar.gz
	cd ..
done
