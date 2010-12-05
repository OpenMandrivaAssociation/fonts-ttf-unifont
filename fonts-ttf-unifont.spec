%define pkgname		unifont
%define name		fonts-ttf-%{pkgname}
%define version		5.1.20080907
%define release		%mkrel 3

Summary:		GNU Unifont glyphs
Name:			%{name}
Version:		%{version}
Release:		%{release}
Source0:		%{pkgname}-%{version}.ttf.gz
License:		GPLv2
Group:			System/Fonts/True type
Url:			http://unifoundry.com/unifont.html
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:		noarch
BuildRequires:		freetype-tools

%description
GNU Unifont provides glyphs for every printable code point in the
Unicode 5.1 Basic Multilingual Plane (BMP).  The BMP occupies the
first 65,536 code points of the Unicode space, denoted as
U+0000..U+FFFF.

%prep
%setup -q -T -c %{name}-%{version}
cp -f %SOURCE0 .
gunzip -f *.gz

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/%{pkgname}

install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/%{pkgname}
ttmkfdir %{buildroot}/%{_datadir}/fonts/TTF/%{pkgname}  > %{buildroot}%{_datadir}/fonts/TTF/%{pkgname}/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/%{pkgname}/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/%{pkgname} \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-%{pkgname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/fonts/TTF/%{pkgname}
%{_datadir}/fonts/TTF/%{pkgname}/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/%{pkgname}/fonts.dir
%{_datadir}/fonts/TTF/%{pkgname}/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-%{pkgname}:pri=50
