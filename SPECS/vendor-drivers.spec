Summary: Vendor drivers
Name: vendor-drivers
Version: 1.0.2
Release: 1%{?dist}
License: GPLv2

Source0: SOURCES/vendor-drivers/requires




# auto-generated Requires list
%{lua: f = io.open(rpm.expand("%{_sourcedir}").."/requires") if f ~= nil then print(f:read "*a") f:close() end }

%description
Virtual package with dependencies on all vendor-provided kernel device drivers.

%files
