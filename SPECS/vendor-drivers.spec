Summary: Vendor drivers
Name: vendor-drivers
Version: 1.0.2
Release: 1.2%{?dist}
License: GPLv2

Source0: SOURCES/vendor-drivers/requires




# auto-generated Requires list
%{lua: f = io.open(rpm.expand("%{_sourcedir}").."/requires") if f ~= nil then print(f:read "*a") f:close() end }

# XCP-ng's added drivers
Requires: r8125-module
Requires: igc-module

%description
Virtual package with dependencies on all vendor-provided kernel device drivers.

%files

%changelog

* Tue Feb 15 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.2-1.2
- Requires r8125-module and igc-module

* Tue Jan 11 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.2-1.1
- Add intel-ice from CH 8.2.1
- vendor-drivers was not updated by Citrix so we do it ourselves
