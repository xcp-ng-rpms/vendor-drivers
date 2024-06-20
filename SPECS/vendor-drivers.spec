%global package_speccommit 455bb56d5269638a6da4c036a2246a12900be34f
%global usver 2.0.3
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
Summary: Vendor drivers
Name: vendor-drivers
Version: 2.0.3
Release: %{?xsrel}.1%{?dist}
License: Public Domain

# This package has no source, no thing to prep, build or install, and no files.
BuildArch: noarch

Requires: avago-megaraid-sas
Requires: avago-mpt3sas
Requires: broadcom-bnxt-en
# XCP-ng: we packaged mpi3mr ourselves as mpi3mr-module
#Requires: broadcom-mpi3mr
Requires: chelsio-cxgb4
Requires: cisco-enic
Requires: cisco-fnic
Requires: emulex-lpfc
Requires: intel-e1000e
Requires: intel-fm10k
Requires: intel-i40e
Requires: intel-ice
Requires: intel-igb
Requires: intel-igc
Requires: intel-ixgbe
Requires: mellanox-mlnxen
Requires: microsemi-aacraid
Requires: microsemi-smartpqi
Requires: qlogic-fastlinq
Requires: qlogic-netxtreme2
Requires: qlogic-netxtreme2-4.19.0+1-modules
Requires: qlogic-qla2xxx

# XCP-ng additions
Requires: mpi3mr-module
Requires: r8125-module

%description
Virtual package with dependencies on all vendor-provided kernel device drivers.

%files

%changelog
* Thu Jun 20 2024 Samuel Verschelde <stormi-xcp@ylix.fr> - 2.0.3-1.1
- Rebase on 2.0.3-1
- Switch dependency from our igc-module to the new intel-igc
- *** Upstream changelog ***
- * Fri Apr 19 2024 Stephen Cheng <stephen.cheng@cloud.com> - 2.0.3-1
- - Add intel-igc to required drivers

* Mon Jan 22 2024 Samuel Verschelde <stormi-xcp@ylix.fr> - 2.0.2-1.1
- Rebase on 2.0.2-1
- Keep dependency to our mpi3mr-module RPM instead of upstream's new but older broadcom-mpi3mr RPM
- *** Upstream changelog ***
- * Wed Nov 22 2023 Mark Syms <mark.syms@citrix.com> - 2.0.2-1
- - Add broadcom-mpi3mr to required drivers

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
