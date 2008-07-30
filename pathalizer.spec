%define name pathalizer
%define version 0.7
%define release %mkrel 3

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



