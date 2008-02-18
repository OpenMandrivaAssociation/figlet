%define name figlet
%define version 222
%define release %mkrel 5

Summary: Program for making large letters out of ordinary text 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}%{version}.tar.bz2
License: Artistic
Group: Toys
Url: http://www.figlet.org/
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
FIGlet is a program for making large letters out 
of ordinary text.

Install figlet-more-fonts to have extra fonts no longer include
in this package.

%prep
%setup -q -n %name%version

%build
export CFLAGS=$RPM_OPT_FLAGS
%make \
    DESTDIR=%_bindir \
    MANDIR=%_mandir/man6 \
    DEFAULTFONTDIR=%_datadir/%name

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT{%_bindir,%_mandir/man6,%_datadir/%name}
make install \
    DESTDIR=$RPM_BUILD_ROOT%_bindir \
    MANDIR=$RPM_BUILD_ROOT%_mandir/man6 \
    DEFAULTFONTDIR=$RPM_BUILD_ROOT%_datadir/%name

chmod 755 $RPM_BUILD_ROOT%_bindir/*
chmod 644 $RPM_BUILD_ROOT%_datadir/%name/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES FAQ
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*
%_mandir/man6/*


