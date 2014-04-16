Summary:	A web path analyzer
Name:		pathalizer
Version:	0.7
Release:	5
License:	GPLv2+
Group:		Monitoring
Url:		http://pathalizer.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2

%description
Pathalizer is a tool to visualize the paths most users take when browsing
a website. This information can then be used to decide how to improve the
navigation of the site, and which parts are most worth improving and keeping
up to date.

%files
%doc README CHANGELOG
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/pathalizer.conf

#----------------------------------------------------------------------------

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
%makeinstall_std PREFIX=%{buildroot}%{_prefix}
cat << EOF >%{buildroot}%{_sysconfdir}/pathalizer.conf
ignore \.css
unify "Home Page" : "^/$" "^/index.html" "^/index.htm" "^/index.php"
ignore_refresh 1
EOF

