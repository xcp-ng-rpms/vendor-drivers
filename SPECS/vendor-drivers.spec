%global package_speccommit c16557bda3f18eb006b73b8e516cfbdaf549a219
%global usver 2.0.1
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
Summary: Vendor drivers
Name: vendor-drivers
Version: 2.0.1
Release: %{?xsrel}%{?dist}
License: Public Domain

# This package has no source, no thing to prep, build or install, and no files.
BuildArch: noarch

Requires: avago-megaraid-sas
Requires: avago-mpt3sas
Requires: broadcom-bnxt-en
Requires: chelsio-cxgb4
Requires: cisco-enic
Requires: cisco-fnic
Requires: emulex-lpfc
Requires: intel-e1000e
Requires: intel-fm10k
Requires: intel-i40e
Requires: intel-ice
Requires: intel-igb
Requires: intel-ixgbe
Requires: mellanox-mlnxen
Requires: microsemi-aacraid
Requires: microsemi-smartpqi
Requires: qlogic-fastlinq
Requires: qlogic-netxtreme2-4.19.0+1-modules
Requires: qlogic-qla2xxx

%description
Virtual package with dependencies on all vendor-provided kernel device drivers.

%files

%changelog
* Mon Jan 30 2023 Zhuangxuan Fei <zhuangxuan.fei@cloud.com> - 2.0.1-1
- CA-374882: Add new driver microsemi-aacraid as requires

* Wed Mar 23 2022 Alex Brett <alex.brett@citrix.com> - 2.0.0-1
- Initial set of vendor-drivers for rolling release
