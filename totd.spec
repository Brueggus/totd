#
# spec file for package totd
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           totd
Version:        1.5.3
Release:        1
Summary:        Trick Or Treat Daemon
License:        BSD
Group:          Productivity/Networking/DNS/Servers
Url:            http://www.dillema.net/software/totd.html
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.service
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The totd ('Trick Or Treat Daemon') DNS proxy Totd is a small DNS proxy
nameserver that supports IPv6 only hosts/networks that communicate with the
IPv4 world using some translation mechanism. Examples of such translation
mechanisms currently in use are:

 * IPv6/IPv4 Network Address and Packet Translation (NAT-PT) implemented e.g.
   by Cisco.
 * Application level translators as the faithd implemented by the KAME project.
   See faithd(8) on BSD/Kame. 

These translators translate map IPv4 to IPv6 connections and back in some way.
In order for an application to connect through such a translator to the world
beyond it needs to use fake or fabricated addresses that are routed to this
translator. These fake addresses don't exist in the DNS, and most likely you
would not want them to appear there either. Totd fixes this problem for now
(until more elegant solutions emerge?) by translating DNS queries/responses for
the faked addresses. totd constructs these fake addresses based on a configured
IPv6 translator prefix and records it *does* find in DNS. Totd is merely a
stateless DNS-proxy, not a nameserver itself. Totd needs to be able to forward
requests to a real nameserver. In addition, totd has experimental support for
reverse lookup of 6to4 addresses and for translation scoped address queries.
See also, the README file and man page that ships with totd.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
install -D -m 0755 totd %{buildroot}%{_sbindir}/totd
install -D -m 0644 totd.conf.sample %{buildroot}%{_sysconfdir}/totd.conf
install -D -m 0644 totd.8 %{buildroot}%{_mandir}/man8/totd.8
install -D -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/totd.service

%files
%defattr(-,root,root)
%doc README COPYRIGHT
%{_sbindir}/totd
%config(noreplace) %{_sysconfdir}/totd.conf
%{_mandir}/man8/totd.8*
%dir /usr/lib/systemd
%dir /usr/lib/systemd/system
/usr/lib/systemd/system/totd.service

%changelog
* Tue Dec 29 2020 Alexander Bruegmann <mail@abruegmann.eu> 1.5.3
- update version
* Mon Apr  1 2013 mhrusecky@suse.com
- systemd integration
* Sun Mar 31 2013 mhrusecky@suse.com
- initial version of totd
