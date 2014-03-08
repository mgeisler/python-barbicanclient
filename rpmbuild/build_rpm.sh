#!/bin/bash

pushd $PWD
mkdir -p rpmbuild/{BUILD,RPMS,S{OURCE,PEC,RPM}S}

BUILD_VERSION=$(ls dist | sed 's/^python-barbicanclient-\(.*\)\.tar\.gz/\1/g')
export BUILD_VERSION
echo "Building RPM version $BUILD_VERSION"

cp "dist/python-barbicanclient-$BUILD_VERSION.tar.gz" rpmbuild/SOURCES
sed -e s/BUILD_VERSION/$BUILD_VERSION/g -i rpmbuild/SPECS/python-barbicanclient.spec
rpmbuild --define "_topdir $WORKSPACE/rpmbuild" -ba --sign rpmbuild/SPECS/python-barbicanclient.spec
popd
