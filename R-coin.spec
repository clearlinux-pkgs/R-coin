#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-coin
Version  : 1.4.3
Release  : 58
URL      : https://cran.r-project.org/src/contrib/coin_1.4-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/coin_1.4-3.tar.gz
Summary  : Conditional Inference Procedures in a Permutation Test Framework
Group    : Development/Tools
License  : GPL-2.0
Requires: R-coin-lib = %{version}-%{release}
Requires: R-libcoin
Requires: R-matrixStats
Requires: R-modeltools
Requires: R-multcomp
Requires: R-mvtnorm
BuildRequires : R-TH.data
BuildRequires : R-e1071
BuildRequires : R-libcoin
BuildRequires : R-matrixStats
BuildRequires : R-modeltools
BuildRequires : R-multcomp
BuildRequires : R-mvtnorm
BuildRequires : R-vcd
BuildRequires : R-xtable
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
problem including two-sample, K-sample (non-parametric ANOVA),
             correlation, censored, ordered and multivariate problems described

%package lib
Summary: lib components for the R-coin package.
Group: Libraries

%description lib
lib components for the R-coin package.


%prep
%setup -q -n coin
pushd ..
cp -a coin buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695838363

%install
export SOURCE_DATE_EPOCH=1695838363
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/coin/doc/Implementation.R
/usr/lib64/R/library/coin/doc/Implementation.Rnw
/usr/lib64/R/library/coin/doc/Implementation.pdf
/usr/lib64/R/library/coin/doc/LegoCondInf.R
/usr/lib64/R/library/coin/doc/LegoCondInf.Rnw
/usr/lib64/R/library/coin/doc/LegoCondInf.pdf
/usr/lib64/R/library/coin/doc/MAXtest.R
/usr/lib64/R/library/coin/doc/MAXtest.Rnw
/usr/lib64/R/library/coin/doc/MAXtest.pdf
/usr/lib64/R/library/coin/doc/coin.R
/usr/lib64/R/library/coin/doc/coin.Rnw
/usr/lib64/R/library/coin/doc/coin.pdf
/usr/lib64/R/library/coin/doc/index.html
/usr/lib64/R/library/coin/doxygen.cfg
/usr/lib64/R/library/coin/help/AnIndex
/usr/lib64/R/library/coin/help/aliases.rds
/usr/lib64/R/library/coin/help/coin.rdb
/usr/lib64/R/library/coin/help/coin.rdx
/usr/lib64/R/library/coin/help/paths.rds
/usr/lib64/R/library/coin/html/00Index.html
/usr/lib64/R/library/coin/html/R.css
/usr/lib64/R/library/coin/tests/AIDS.rda
/usr/lib64/R/library/coin/tests/Examples/coin-Ex.Rout.save
/usr/lib64/R/library/coin/tests/FAILURE.rda
/usr/lib64/R/library/coin/tests/LANCET.rda
/usr/lib64/R/library/coin/tests/army.rda
/usr/lib64/R/library/coin/tests/asthma.rda
/usr/lib64/R/library/coin/tests/bloodp.rda
/usr/lib64/R/library/coin/tests/bugfixes.R
/usr/lib64/R/library/coin/tests/bugfixes.Rout.save
/usr/lib64/R/library/coin/tests/comparisons.R
/usr/lib64/R/library/coin/tests/comparisons.Rout.save
/usr/lib64/R/library/coin/tests/employment.rda
/usr/lib64/R/library/coin/tests/lungcancer.rda
/usr/lib64/R/library/coin/tests/regtest_2sample.R
/usr/lib64/R/library/coin/tests/regtest_2sample.Rout.save
/usr/lib64/R/library/coin/tests/regtest_Ksample.R
/usr/lib64/R/library/coin/tests/regtest_Ksample.Rout.save
/usr/lib64/R/library/coin/tests/regtest_MTP.R
/usr/lib64/R/library/coin/tests/regtest_MTP.Rout.save
/usr/lib64/R/library/coin/tests/regtest_contingency.R
/usr/lib64/R/library/coin/tests/regtest_contingency.Rout.save
/usr/lib64/R/library/coin/tests/regtest_correlation.R
/usr/lib64/R/library/coin/tests/regtest_correlation.Rout.save
/usr/lib64/R/library/coin/tests/regtest_distribution.R
/usr/lib64/R/library/coin/tests/regtest_distribution.Rout.save
/usr/lib64/R/library/coin/tests/regtest_helpers.R
/usr/lib64/R/library/coin/tests/regtest_helpers.Rout.save
/usr/lib64/R/library/coin/tests/regtest_midpvalue.R
/usr/lib64/R/library/coin/tests/regtest_midpvalue.Rout.save
/usr/lib64/R/library/coin/tests/regtest_names.R
/usr/lib64/R/library/coin/tests/regtest_names.Rout.save
/usr/lib64/R/library/coin/tests/regtest_size.R
/usr/lib64/R/library/coin/tests/regtest_size.Rout.save
/usr/lib64/R/library/coin/tests/regtest_trafo.R
/usr/lib64/R/library/coin/tests/regtest_trafo.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/coin/libs/coin.so
/usr/lib64/R/library/coin/libs/coin.so.avx2
/usr/lib64/R/library/coin/libs/coin.so.avx512
