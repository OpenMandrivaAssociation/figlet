%define _fontdir %{_datadir}/%{name}

Name: figlet
Epoch: 1
Version: 2.2.5
Release: 1
Summary: A program for making large letters out of ordinary text
URL: http://www.figlet.org/
Group: Toys
License: BSD
Source: ftp://ftp.figlet.org:21/pub/figlet/program/unix/%{name}-%{version}.tar.gz
BuildRequires: zip
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
FIGlet is a program that creates large characters out of ordinary
screen characters
 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \_
|_|_|_|\_\___|  \__|_| |_|_|___(_)

(This is meant to be viewed in a monospaced font.)  FIGlet can create
characters in many different styles and can kern and "smush" these
characters together in various ways.

%prep
%setup -q

%build
%make \
  CFLAGS="%{optflags}" \
  BINDIR=%{_bindir} \
  MANDIR=%{_mandir} \
  DEFAULTFONTDIR=%{_fontdir}

%install
rm -rf %{buildroot}

# Compress fonts
(cd fonts;
chmod 644 *;
for i in *; do
  zip -m $i.zip $i
  mv $i.zip $i
done)

make install \
  BINDIR=%{_bindir} \
  MANDIR=%{_mandir} \
  DEFAULTFONTDIR=%{_fontdir} \
  DESTDIR=%{buildroot}
./run-tests.sh %{buildroot}%{_fontdir}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc FAQ CHANGES LICENSE README figfont.txt
%attr(755,-,-) %{_bindir}/figlet
%attr(755,-,-) %{_bindir}/chkfont
%attr(755,-,-) %{_bindir}/figlist
%attr(755,-,-) %{_bindir}/showfigfonts
%{_mandir}/man6/figlet.6*
%{_mandir}/man6/chkfont.6*
%{_mandir}/man6/figlist.6*
%{_mandir}/man6/showfigfonts.6*
%dir %{_fontdir}
%{_fontdir}/*.fl[fc]


%changelog
* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 1:2.2.4-2mdv2011.0
+ Revision: 640432
- rebuild to obsolete old packages

* Fri Jan 28 2011 Claudio Matsuoka <claudio@mandriva.com> 1:2.2.4-1
+ Revision: 633686
- new upstream release
  * add support for tlf2 fonts
  * fix smushing corruption bug

* Mon Jan 24 2011 Claudio Matsuoka <claudio@mandriva.com> 1:2.2.3-2
+ Revision: 632479
- add upstream patch to fix rendering corruption on multiline smushing

* Thu Jan 13 2011 Claudio Matsuoka <claudio@mandriva.com> 1:2.2.3-1
+ Revision: 631016
- new upstream version 2.2.3
  * license changed to BSD
  * zipio license changed to MIT
  * fixes for JIS0201
  * fix for memory allocation errors and access violations
- Fix memory violation when smushing at line start
- Relicense zipio files under the MIT license
- fix handling of JIS X 0201 characters (by Micah Cowan)
- refactor FIGlet package
  * layout change: include fonts as subpackages, obsolete figlet-more-fonts
  * better package descriptions
  * use upstream version numbering system
- fix memory allocation error handling
- fix 5x8 fixed font size
- add utility manpages written by Jonathon Abbott for Debian
- use compressed fonts to save storage space
- imported package figlet

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 222-9mdv2011.0
+ Revision: 618282
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 222-8mdv2010.0
+ Revision: 428729
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 222-7mdv2009.0
+ Revision: 245133
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 222-5mdv2008.1
+ Revision: 170829
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 222-4mdv2008.0
+ Revision: 68487
- rebuild


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 11:20:43 (53392)
- rebuild

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 11:14:40 (53391)
Import figlet

* Tue Jul 26 2005 Olivier Thauvin <nanardon@mandriva.org> 222-2mdk
- update url

* Tue Jul 26 2005 Olivier Thauvin <nanardon@mandriva.org> 222-1mdk
- 222

* Mon Jun 14 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 221-2mdk
- birthday rebuild
- split font into figlet-more-fonts


