# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       lnav

# >> macros
# << macros

Summary:    Log file navigator
Version:    0.10.1
Release:    0
Group:      Tools
License:    BSD-2-Clause
URL:        https://lnav.org
Source0:    %{name}-%{version}.tar.gz
Source100:  lnav.yaml
Requires:   sailfish-version >= 3.3.0
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  gcc-c++
BuildRequires:  bzip2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ( pkgconfig(readline) or readline-devel )

%description

%if "%{?vendor}" == "chum"
PackageName: LNAV -- The Logfile Navigator
PackagerName: nephros
Type: console-application
Categories:
  - Utility
  - FileTools
Custom:
  Repo: https://github.com/tstack/lnav
  PackagingRepo: https://github.com/sailfishos-chum/lnav
  DescriptionMD: https://raw.githubusercontent.com/tstack/lnav/master/README.md
Screenshots:
  - https://github.com/tstack/lnav/raw/master/docs/assets/images/lnav-syslog.png
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%reconfigure --disable-static

# >> build post
pushd src
make %{?_smp_mflags}
popd
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
pushd src
%make_install
popd
# << install post

%files
%defattr(-,root,root,-)
# >> files
%{_bindir}/%{name}
# << files
