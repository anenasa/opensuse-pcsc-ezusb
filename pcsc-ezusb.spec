#
# spec file for package pcsc-ezusb
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           pcsc-ezusb
Version:        1.5.3
Release:        0
Summary:        PCSC Driver for Castles Technology EZ100PU/EZMINI
License:        NonFree
URL:            https://www.castlestech.com/
Source0:        https://archive.org/download/ezusb-%version/ezusb-%version.zip
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
Requires:       pcsc-lite
%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
PCSC Driver for Castles Technology EZ100PU/EZMINI.

%prep
%setup -q -n EZUSB_Linux
unzip -qo EZUSB_Linux_x86_64_v%version.zip

%build

%install
install -m644 -D EZUSB_Linux_x86_64_v%version/driver_ezusb_v%{version}_for_64_bit/drivers/ezusb.so %{buildroot}/%{ifddir}/ezusb.bundle/Contents/Linux/ezusb.so
install -m644 -D EZUSB_Linux_x86_64_v%version/driver_ezusb_v%{version}_for_64_bit/drivers/Info.plist %{buildroot}/%{ifddir}/ezusb.bundle/Contents/Info.plist

%files
%{ifddir}/*

%changelog
