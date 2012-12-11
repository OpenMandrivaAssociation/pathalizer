%define name pathalizer
%define version 0.7
%define release %mkrel 4

Summary: A web path analyzer
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Monitoring
Url: http://pathalizer.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Pathalizer is a tool to visualize the paths most users take when
browsing a website. This information can then be used to decide
how to improve the navigation of the site, and 
which parts are most worth improving and keeping up to date.

%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/%_sysconfdir/
%makeinstall_std PREFIX=%buildroot/%_prefix/
cat << EOF >%buildroot/%_sysconfdir/pathalizer.conf
ignore \.css
unify "Home Page" : "^/$" "^/index.html" "^/index.htm" "^/index.php"
ignore_refresh 1
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README INSTALL CHANGELOG
%{_bindir}/*
%config(noreplace) %_sysconfdir/pathalizer.conf





%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.7-4mdv2010.0
+ Revision: 430242
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7-3mdv2009.0
+ Revision: 255049
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.7-1mdv2008.1
+ Revision: 141041
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 27 2007 Erwan Velu <erwan@mandriva.org> 0.7-1mdv2007.1
+ Revision: 149059
- Fixing summary
- Import pathalizer

