#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-goftest
Version  : 1.2.2
Release  : 25
URL      : https://cran.r-project.org/src/contrib/goftest_1.2-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/goftest_1.2-2.tar.gz
Summary  : Classical Goodness-of-Fit Tests for Univariate Distributions
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-goftest-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
for continuous univariate distributions, using
	     efficient algorithms.

%package lib
Summary: lib components for the R-goftest package.
Group: Libraries

%description lib
lib components for the R-goftest package.


%prep
%setup -q -c -n goftest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575396351

%install
export SOURCE_DATE_EPOCH=1575396351
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library goftest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library goftest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library goftest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc goftest || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/goftest/DESCRIPTION
/usr/lib64/R/library/goftest/INDEX
/usr/lib64/R/library/goftest/Meta/Rd.rds
/usr/lib64/R/library/goftest/Meta/features.rds
/usr/lib64/R/library/goftest/Meta/hsearch.rds
/usr/lib64/R/library/goftest/Meta/links.rds
/usr/lib64/R/library/goftest/Meta/nsInfo.rds
/usr/lib64/R/library/goftest/Meta/package.rds
/usr/lib64/R/library/goftest/NAMESPACE
/usr/lib64/R/library/goftest/R/goftest
/usr/lib64/R/library/goftest/R/goftest.rdb
/usr/lib64/R/library/goftest/R/goftest.rdx
/usr/lib64/R/library/goftest/help/AnIndex
/usr/lib64/R/library/goftest/help/aliases.rds
/usr/lib64/R/library/goftest/help/goftest.rdb
/usr/lib64/R/library/goftest/help/goftest.rdx
/usr/lib64/R/library/goftest/help/paths.rds
/usr/lib64/R/library/goftest/html/00Index.html
/usr/lib64/R/library/goftest/html/R.css
/usr/lib64/R/library/goftest/tests/all.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/goftest/libs/goftest.so
/usr/lib64/R/library/goftest/libs/goftest.so.avx2
