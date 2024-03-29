#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-xmldiff
Version  : 2.6.3
Release  : 23
URL      : https://files.pythonhosted.org/packages/7c/5d/75f88f059d3929554ebf9aaa16b9a7990f8146e8dacd44aad9889b826876/xmldiff-2.6.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/7c/5d/75f88f059d3929554ebf9aaa16b9a7990f8146e8dacd44aad9889b826876/xmldiff-2.6.3.tar.gz
Summary  : Creates diffs of XML files
Group    : Development/Tools
License  : MIT
Requires: pypi-xmldiff-bin = %{version}-%{release}
Requires: pypi-xmldiff-license = %{version}-%{release}
Requires: pypi-xmldiff-python = %{version}-%{release}
Requires: pypi-xmldiff-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
See LICENSE.txt for Licensing information.
See docs/source/contributing.rst for development information

%package bin
Summary: bin components for the pypi-xmldiff package.
Group: Binaries
Requires: pypi-xmldiff-license = %{version}-%{release}

%description bin
bin components for the pypi-xmldiff package.


%package license
Summary: license components for the pypi-xmldiff package.
Group: Default

%description license
license components for the pypi-xmldiff package.


%package python
Summary: python components for the pypi-xmldiff package.
Group: Default
Requires: pypi-xmldiff-python3 = %{version}-%{release}

%description python
python components for the pypi-xmldiff package.


%package python3
Summary: python3 components for the pypi-xmldiff package.
Group: Default
Requires: python3-core
Provides: pypi(xmldiff)
Requires: pypi(lxml)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-xmldiff package.


%prep
%setup -q -n xmldiff-2.6.3
cd %{_builddir}/xmldiff-2.6.3
pushd ..
cp -a xmldiff-2.6.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684870477
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-xmldiff
cp %{_builddir}/xmldiff-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-xmldiff/f3f2bfc0537c3f3d366e24c8ec9fff2480b37796 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xmldiff
/usr/bin/xmlpatch

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-xmldiff/f3f2bfc0537c3f3d366e24c8ec9fff2480b37796

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
