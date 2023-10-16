%global package_speccommit c16557bda3f18eb006b73b8e516cfbdaf549a219
%global usver 2.0.1
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
Summary: Vendor drivers
Name: vendor-drivers
Version: 2.0.1
Release: %{?xsrel}.2%{?dist}
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
Requires: qlogic-netxtreme2
Requires: qlogic-netxtreme2-4.19.0+1-modules
Requires: qlogic-qla2xxx

# XCP-ng additions
Requires: igc-module
Requires: mpi3mr-module
Requires: r8125-module

%description
Virtual package with dependencies on all vendor-provided kernel device drivers.

%files

%changelog
* Thu Oct 12 2023 Yann Dirson <yann.dirson@vates.tech> - 2.0.1-1.2
- Add mpi3mr-module

* Wed Feb 21 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 2.0.1-1.1
- Update to 2.0.1-1
- *** Upstream changelog ***
- * Mon Jan 30 2023 Zhuangxuan Fei <zhuangxuan.fei@cloud.com> - 2.0.1-1
- - CA-374882: Add new driver microsemi-aacraid as requires

* Mon Nov 07 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 2.0.0-1.3
- Add missing qlogic-netxtreme2

* Fri Nov 04 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 2.0.0-1.2
- Add r8125-module to default installation

* Wed Nov 02 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 2.0.0-1.1
- Add igc-module to default installation

* Wed Mar 23 2022 Alex Brett <alex.brett@citrix.com> - 2.0.0-1
- Initial set of vendor-drivers for rolling release
