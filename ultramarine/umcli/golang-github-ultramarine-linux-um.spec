%define debug_package %nil
# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/Ultramarine-Linux/um
%global goipath         github.com/Ultramarine-Linux/um

%global common_description %{expand:
A CLI tool for managing an Ultramarine Linux system.}

%global godocs          README.md

Name:           golang-github-ultramarine-linux-um
Version:        0.2.0
Release:        %autorelease -p
Summary:        A CLI tool for managing an Ultramarine Linux system

License:        GPL-3.0-or-later
URL:            %{gourl}
Source:         https://github.com/Ultramarine-Linux/um/archive/v%version.tar.gz
Provides:       umcli
Provides:       um
BuildRequires:  git-core
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(flatpak)

%description %{common_description}

%gopkg

%prep
%autosetup -n um-%version -p1
go mod download

%build
mkdir -p build/bin
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n') -s -w" -buildmode=pie -o %{gobuilddir}/bin/um %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%if %{without bootstrap}
%files
%doc README.md
%{_bindir}/um
%endif

%dnl %gopkgfiles

%changelog
%autochangelog
