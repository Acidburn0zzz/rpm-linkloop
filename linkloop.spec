Name:           linkloop
Summary:        Test network connectivity at link layer (layer-2)
Version:        1.0.1
Release:        1
License:        GPL-2.0+
Group:          Productivity/Networking/Other
Url:            https://sourceforge.net/projects/linkloop/
Source0:        http://ncu.dl.sourceforge.net/project/linkloop/linkloop/%{version}/linkloop-%{version}-hp.tar.gz
Source1:        linkloop.service

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

%description
This program is similar to ping, but tests connectivity at the link layer
(layer 2) instead of the network layer (layer 3). This works like the
HP-UX linkloop utility. It was tested between Linux and HP-UX. There is
also a "server-side" utility.

%prep
%autosetup -n %{name}-%{version}-hp

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -D %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
# Cleanup unused init.d script
rm -f %{buildroot}/etc/init.d/linkloopd

%clean
rm -rf %
 
%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_unitdir}/%{name}.service
%{_mandir}/man*/*

%changelog
* Mon Oct 17 2016 John Siegrist <john@complects.com> 1.0.1-1
- Update for Fedora and CentOS and import into the CloudRouter project
* Fri Dec  2 2011 coolo@suse.com
- add automake as buildrequire to avoid implicit dependency
* Mon Aug 11 2008 tiwai@suse.de
- initial version: 1.0.0 (FATE#303779)
- fix some bugs in buffer size handling
