%define vertag 222
%define _fontdir %{_datadir}/%{name}

Name: figlet
Epoch: 1
Version: 2.2.2
Release: %mkrel 1
Summary: A program for making large letters out of ordinary text
URL: http://www.figlet.org/
Group: Toys
License: Academic Free License 2.1
Source0: %{name}%{vertag}.tar.gz
Source1: showfigfonts.6
Source2: chkfont.6
Source3: figlist.6
Source4: contributed.tar.gz
Source5: international.tar.gz
Patch1: 0001-Address-compiler-warnings.patch
Patch2: 0002-Handle-memory-allocation-errors.patch
Patch3: 0003-Fix-memory-violation-when-smushing-at-line-start.patch
Patch4: 0004-Relicense-zipio-files-under-the-MIT-license.patch
Patch100: contributed-bdffonts-5x8.patch
Patch101: figlet-shift-in-shift-out-fix.patch
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

%package contributed
Summary: Contributed fonts for FIGlet
Requires: %{name}
Obsoletes: figlet-more-fonts <= 20110110
Conflicts: figlet-more-fonts <= 20110110

%description contributed
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package contains many contributed fonts for figlet.

%package international
Summary: International fonts for FIGlet
Requires: %{name}
Obsoletes: figlet-more-fonts <= 20110110
Conflicts: figlet-more-fonts <= 20110110

%description international
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package contains international fonts for figlet, including
CJK fonts, Hebrew, Cyrillic, Greek, Cherokee, Futhark, Tengwar
and Morse code.

%package c64fonts
Summary: Commodore 64 fonts for FIGlet
Requires: %{name}
Obsoletes: figlet-more-fonts <= 20110110
Conflicts: figlet-more-fonts <= 20110110

%description c64fonts
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package contains Commodore 64 fonts converted for FIGlet by
by David Proper.

%package bdffonts
Summary: X Window System fonts for FIGlet
License: MIT
Requires: %{name}
Obsoletes: figlet-more-fonts <= 20110110
Conflicts: figlet-more-fonts <= 20110110

%description bdffonts
FIGlet is a program that creates large characters out of ordinary
screen characters.

This package contains fonts converted from the BDF format distributed by
the X Consortium, including Lucida Bright, Charter, Courier, Helvetica,
Lucida Sans, New Century Schoolbook, Times Roman, Lucida Sans Typewriter,
Utopia and fixed-width fonts.


%prep
%setup -q -n %{name}%{vertag}
%patch1 -p1 -b .Address-compiler-warnings
%patch2 -p1 -b .Handle-memory-allocation-errors
%patch3 -p1 -b .Fix-memory-violation-when-smushing-at-line-start
%patch4 -p1 -b .Relicense-zipio-files-under-the-MIT-license
tar xzf %{_sourcedir}/contributed.tar.gz
%patch100 -p0 -b .contributed-bdffonts-5x8
%patch101 -p0 -b .shift-in-shift-out-fix
mv contributed/C64-fonts .
mv contributed/bdffonts .
tar xzf %{_sourcedir}/international.tar.gz
(cd international; tar xzf cjkfonts.tar.gz)

%build
%make \
  CFLAGS="%{optflags}" \
  DESTDIR=%{_bindir} \
  MANDIR=%{_mandir}/man6 \
  DEFAULTFONTDIR=%{_fontdir}

%install
rm -rf %{buildroot}
install -D -m755 figlet %{buildroot}%{_bindir}/figlet
install -D -m644 figlet.6 %{buildroot}%{_mandir}/man6/figlet.6
for i in chkfont figlist showfigfonts; do
  install -D -m755 $i %{buildroot}%{_bindir}/$i
  install -D -m644 %{_sourcedir}/$i.6 %{buildroot}%{_mandir}/man6/$i.6
done
mkdir -p %{buildroot}%{_fontdir}/

rm contributed/banner.flf
(cd C64-fonts; for i in *.flf; do mv $i c64-$i; done)
for i in fonts contributed international C64-fonts bdffonts; do
  find $i -name "*.fl[cf]" | sed "s!.*/!%{_fontdir}/!" > $i.list
  find $i -name "*.fl[cf]" -exec cp {} %{buildroot}%{_fontdir}/ \;
done

# Compress fonts
(cd %{buildroot}%{_fontdir}/
chmod 644 *  
for i in *; do
  zip -m $i.zip $i
  mv $i.zip $i
done)

# Install Micah Cowan's replacement JIS X 0201 control file
cp -f %{_sourcedir}/myjis.flc fonts/jis0201.flc

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
%dir %{_fontdir}

%files contributed -f contributed.list
%defattr(0644,root,root,0755)

%files international -f international.list
%defattr(0644,root,root,0755)

%files c64fonts -f C64-fonts.list
%defattr(0644,root,root,0755)

%files bdffonts -f bdffonts.list
%defattr(0644,root,root,0755)
%doc bdffonts/bdffont1.txt bdffonts/bdf2flf.pl
