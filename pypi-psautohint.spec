#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-psautohint
Version  : 2.4.0
Release  : 16
URL      : https://files.pythonhosted.org/packages/91/74/014da6e9280844cec6a73a04e069d95740e5520fd9477afbf31208d0e2f4/psautohint-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/91/74/014da6e9280844cec6a73a04e069d95740e5520fd9477afbf31208d0e2f4/psautohint-2.4.0.tar.gz
Summary  : Python wrapper for Adobe's PostScript autohinter
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-psautohint-bin = %{version}-%{release}
Requires: pypi-psautohint-license = %{version}-%{release}
Requires: pypi-psautohint-python = %{version}-%{release}
Requires: pypi-psautohint-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(lxml)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![Test and Build](https://github.com/adobe-type-tools/psautohint/workflows/Test%20and%20Build/badge.svg)
[![Codecov](https://codecov.io/gh/adobe-type-tools/psautohint/branch/master/graph/badge.svg)](https://codecov.io/gh/adobe-type-tools/psautohint)
[![PyPI](https://img.shields.io/pypi/v/psautohint.svg)](https://pypi.org/project/psautohint)
[![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/adobe-type-tools/psautohint.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/adobe-type-tools/psautohint/context:cpp)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/adobe-type-tools/psautohint.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/adobe-type-tools/psautohint/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/adobe-type-tools/psautohint.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/adobe-type-tools/psautohint/alerts/)

%package bin
Summary: bin components for the pypi-psautohint package.
Group: Binaries
Requires: pypi-psautohint-license = %{version}-%{release}

%description bin
bin components for the pypi-psautohint package.


%package license
Summary: license components for the pypi-psautohint package.
Group: Default

%description license
license components for the pypi-psautohint package.


%package python
Summary: python components for the pypi-psautohint package.
Group: Default
Requires: pypi-psautohint-python3 = %{version}-%{release}

%description python
python components for the pypi-psautohint package.


%package python3
Summary: python3 components for the pypi-psautohint package.
Group: Default
Requires: python3-core
Provides: pypi(psautohint)
Requires: pypi(fonttools)

%description python3
python3 components for the pypi-psautohint package.


%prep
%setup -q -n psautohint-2.4.0
cd %{_builddir}/psautohint-2.4.0
pushd ..
cp -a psautohint-2.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685552081
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-psautohint
cp %{_builddir}/psautohint-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-psautohint/8359238144a0969705d737fb5f9b1e6b9cd5f16e || :
cp %{_builddir}/psautohint-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-psautohint/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/psautohint
/usr/bin/psstemhist

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-psautohint/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-psautohint/8359238144a0969705d737fb5f9b1e6b9cd5f16e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
