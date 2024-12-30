Name:           readymade
Version:        0.6.0
Release:        1%?dist
Summary:        Install ready-made distribution images!
License:        MIT
URL:            https://github.com/FyraLabs/readymade
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	anda-srpm-macros rust-packaging mold
BuildRequires:  pkgconfig(libhelium-1)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  clang-devel

Requires:  efibootmgr

%description
Readymade is a Linux Distribution installer based on the great distinst library by System76.

It is created as a replacement to Red Hat's Anaconda installer for Ultramarine Linux and tauOS after we have heard many complaints about the poor UX design of Anaconda, and the lack of working alternative installers for RPM-based distributions.

%prep
%autosetup
%cargo_prep_online

%build

%install
%cargo_install
./install.sh %buildroot
ln -sf %{_datadir}/applications/com.fyralabs.Readymade.desktop %{buildroot}%{_datadir}/applications/liveinst.desktop

%find_lang com.fyralabs.Readymade

%files -f com.fyralabs.Readymade.lang
%_bindir/readymade
%_datadir/polkit-1/actions/com.fyralabs.pkexec.readymade.policy
%_datadir/applications/com.fyralabs.Readymade.desktop
%_datadir/applications/liveinst.desktop
%_datadir/readymade
%_sysconfdir/readymade.toml
