Summary: Vendor drivers
Name: vendor-drivers
Version: 1.0.2
Release: 1.7%{?dist}
License: GPLv2

Source0: SOURCES/vendor-drivers/requires




# auto-generated Requires list
%{lua: f = io.open(rpm.expand("%{_sourcedir}").."/requires") if f ~= nil then print(f:read "*a") f:close() end }

# XCP-ng additions
Requires: mpi3mr-module
Requires: r8125-module

# XCP-ng: not exactly a "vendor" driver since it's a backport from linux
Requires: intel-igc

%description
Virtual package with dependencies on all vendor-provided kernel device drivers.

%files

%changelog
* Tue Oct 01 2024 Thierry Escande <thierry.escande@vates.tech> - 1.0.2-1.7
- Rename igc-module dependency to intel-igc

* Thu Nov 21 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.2-1.6
- Require r8125-module and igc-module, for good this time

* Thu Oct 16 2023 Yann Dirson <yann.dirson@vates.tech> - 1.0.2-1.5
- Add mpi3mr-module

* Thu Feb 24 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.2-1.3
- Revert previous change

* Tue Feb 15 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.2-1.2
- Requires r8125-module and igc-module

* Tue Jan 11 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.2-1.1
- Add intel-ice from CH 8.2.1
- vendor-drivers was not updated by Citrix so we do it ourselves
