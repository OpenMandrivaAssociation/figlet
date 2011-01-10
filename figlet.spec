%define vertag 222

Name: figlet
Version: 2.2.2
Release: %mkrel 1
Summary: A program for making large letters out of ordinary text
URL: http://www.figlet.org/
Group: Text tools
License: Academic Free License 2.1
Source0: %{name}%{vertag}.tar.gz
Source1: showfigfonts.6
Source2: chkfont.6
Source3: figlist.6
Source4: contributed.tar.gz
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

%package contributed
Summary: Contributed fonts for FIGlet
Requires: %{name}

%description contributed
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package contains many contributed fonts for figlet.


%prep
%setup -q -n %{name}%{vertag}
tar xzf %{_sourcedir}/contributed.tar.gz

%build
%make \
  CFLAGS="%{optflags}" \
  DESTDIR=%{_bindir} \
  MANDIR=%{_mandir}/man6 \
  DEFAULTFONTDIR=%{_datadir}/%{name}

%install
rm -rf %{buildroot}
install -D -m755 figlet %{buildroot}%{_bindir}/figlet
install -D -m644 figlet.6 %{buildroot}%{_mandir}/man6/figlet.6
for i in chkfont figlist showfigfonts; do
  install -D -m755 $i %{buildroot}%{_bindir}/$i
  install -D -m644 %{_sourcedir}/$i.6 %{buildroot}%{_mandir}/man6/$i.6
done
mkdir -p %{buildroot}%{_datadir}/%{name}/

rm contributed/banner.flf
for i in fonts contributed; do
  ls $i/*.fl[cf] | sed "s!$i!%{_datadir}/%{name}!" > $i.list
  cp $i/*.fl[cf] %{buildroot}%{_datadir}/%{name}/
done

%clean
rm -rf %{buildroot}

%files -f fonts.list
%defattr(0644,root,root,0755)
%doc FAQ CHANGES LICENSE README
%attr(755,-,-) %{_bindir}/figlet
%attr(755,-,-) %{_bindir}/chkfont
%attr(755,-,-) %{_bindir}/figlist
%attr(755,-,-) %{_bindir}/showfigfonts
%{_mandir}/man6/figlet.6*
%{_mandir}/man6/chkfont.6*
%{_mandir}/man6/figlist.6*
%{_mandir}/man6/showfigfonts.6*
%dir %{_datadir}/%{name}

%files contributed -f contributed.list
%defattr(0644,root,root,0755)
