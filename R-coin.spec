#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-coin
Version  : 1.2.2
Release  : 3
URL      : https://cran.r-project.org/src/contrib/coin_1.2-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/coin_1.2-2.tar.gz
Summary  : Conditional Inference Procedures in a Permutation Test Framework
Group    : Development/Tools
License  : GPL-2.0
Requires: R-coin-lib
Requires: R-e1071
Requires: R-modeltools
Requires: R-multcomp
Requires: R-mvtnorm
Requires: R-vcd
Requires: R-xtable
BuildRequires : R-TH.data
BuildRequires : R-e1071
BuildRequires : R-modeltools
BuildRequires : R-multcomp
BuildRequires : R-mvtnorm
BuildRequires : R-vcd
BuildRequires : R-xtable
BuildRequires : clr-R-helpers

%description
problem including two-sample, K-sample (non-parametric ANOVA), correlation,
  censored, ordered and multivariate problems.

%package lib
Summary: lib components for the R-coin package.
Group: Libraries

%description lib
lib components for the R-coin package.


%prep
%setup -q -c -n coin

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523295351

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523295351
export LANG=C
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library coin
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library coin
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library coin
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library coin|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/coin/CITATION
/usr/lib64/R/library/coin/DESCRIPTION
/usr/lib64/R/library/coin/INDEX
/usr/lib64/R/library/coin/Meta/Rd.rds
/usr/lib64/R/library/coin/Meta/data.rds
/usr/lib64/R/library/coin/Meta/features.rds
/usr/lib64/R/library/coin/Meta/hsearch.rds
/usr/lib64/R/library/coin/Meta/links.rds
/usr/lib64/R/library/coin/Meta/nsInfo.rds
/usr/lib64/R/library/coin/Meta/package.rds
/usr/lib64/R/library/coin/Meta/vignette.rds
/usr/lib64/R/library/coin/NAMESPACE
/usr/lib64/R/library/coin/NEWS.Rd
/usr/lib64/R/library/coin/R/coin
/usr/lib64/R/library/coin/R/coin.rdb
/usr/lib64/R/library/coin/R/coin.rdx
/usr/lib64/R/library/coin/data/Rdata.rdb
/usr/lib64/R/library/coin/data/Rdata.rds
/usr/lib64/R/library/coin/data/Rdata.rdx
/usr/lib64/R/library/coin/doc/LegoCondInf.R
/usr/lib64/R/library/coin/doc/LegoCondInf.Rnw
/usr/lib64/R/library/coin/doc/LegoCondInf.pdf
/usr/lib64/R/library/coin/doc/MAXtest.R
/usr/lib64/R/library/coin/doc/MAXtest.Rnw
/usr/lib64/R/library/coin/doc/MAXtest.pdf
/usr/lib64/R/library/coin/doc/coin.R
/usr/lib64/R/library/coin/doc/coin.Rnw
/usr/lib64/R/library/coin/doc/coin.pdf
/usr/lib64/R/library/coin/doc/coin_implementation.R
/usr/lib64/R/library/coin/doc/coin_implementation.Rnw
/usr/lib64/R/library/coin/doc/coin_implementation.pdf
/usr/lib64/R/library/coin/doc/index.html
/usr/lib64/R/library/coin/doxygen.cfg
/usr/lib64/R/library/coin/help/AnIndex
/usr/lib64/R/library/coin/help/aliases.rds
/usr/lib64/R/library/coin/help/coin.rdb
/usr/lib64/R/library/coin/help/coin.rdx
/usr/lib64/R/library/coin/help/paths.rds
/usr/lib64/R/library/coin/html/00Index.html
/usr/lib64/R/library/coin/html/R.css
/usr/lib64/R/library/coin/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/coin/libs/coin.so
/usr/lib64/R/library/coin/libs/coin.so.avx2
/usr/lib64/R/library/coin/libs/coin.so.avx512
