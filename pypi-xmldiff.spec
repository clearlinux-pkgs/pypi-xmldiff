#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-xmldiff
Version  : 2.4
Release  : 14
URL      : https://files.pythonhosted.org/packages/76/36/a3e41bf7c01f1110d7b5589ca74d2927d3736a5b43ee63053faf3483b991/xmldiff-2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/76/36/a3e41bf7c01f1110d7b5589ca74d2927d3736a5b43ee63053faf3483b991/xmldiff-2.4.tar.gz
Summary  : Creates diffs of XML files
Group    : Development/Tools
License  : MIT
Requires: pypi-xmldiff-bin = %{version}-%{release}
Requires: pypi-xmldiff-license = %{version}-%{release}
Requires: pypi-xmldiff-python = %{version}-%{release}
Requires: pypi-xmldiff-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(lxml)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)

%description
========

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
Requires: pypi(six)

%description python3
python3 components for the pypi-xmldiff package.


%prep
%setup -q -n xmldiff-2.4
cd %{_builddir}/xmldiff-2.4
pushd ..
cp -a xmldiff-2.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361031
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
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
cp %{_builddir}/xmldiff-2.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-xmldiff/f3f2bfc0537c3f3d366e24c8ec9fff2480b37796
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
