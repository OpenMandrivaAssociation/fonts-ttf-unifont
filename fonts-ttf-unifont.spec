%define pkgname		unifont
%define name		fonts-ttf-%{pkgname}
%define version		5.1.20080907
%define release		%mkrel 4

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
BuildRequires: fontconfig
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


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 5.1.20080907-4mdv2011.0
+ Revision: 675579
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 5.1.20080907-3mdv2011.0
+ Revision: 610737
- rebuild

* Wed Feb 24 2010 Lev Givon <lev@mandriva.org> 5.1.20080907-2mdv2010.1
+ Revision: 510643
- fc-cache is now called by an rpm trigger.

* Mon Nov 02 2009 Lev Givon <lev@mandriva.org> 5.1.20080907-1mdv2010.0
+ Revision: 460381
- import fonts-ttf-unifont


