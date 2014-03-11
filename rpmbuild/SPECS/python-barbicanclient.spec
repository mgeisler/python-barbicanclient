%define version BUILD_VERSION
%define release 1

Summary: Python Client for Barbican Key Management API
Name: python-barbicanclient
Version: %{version}
Release: %{release}
Source0: python-barbicanclient-%{version}.tar.gz
Vendor: Rackspace, Inc.
Packager: Douglas Mendizabal <douglas.mendizabal@rackspace.com>
Url: http://github.com/cloudkeep/python-barbicanclient
License: Apache License (2.0)
Group: Development/Libraries
BuildRoot: %{_tmppath}/barbican-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python2-devel
Requires: python-argparse, python-eventlet, python-iso8601
Requires: python-keystoneclient, python-oslo-config, python-pbr
Requires: python-requests

%description
Python language library for using the Barbican Key Management API.

%prep
%setup -n python-barbicanclient-%{version} -q

%build
python setup.py build

%install
python setup.py install -O1 --root $RPM_BUILD_ROOT

%files
%{python_sitelib}/*
/usr/bin/barbican

%clean
rm -rf $RPM_BUILD_ROOT
