%define _fontdir %{_datadir}/%{name}

Name: figlet
Epoch: 1
Version: 2.2.4
Release: %mkrel 2
Summary: A program for making large letters out of ordinary text
URL: http://www.figlet.org/
Group: Toys
License: BSD
Source: ftp://ftp.figlet.org/pub/figlet/program/unix/%{name}-%{version}.tar.gz
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
