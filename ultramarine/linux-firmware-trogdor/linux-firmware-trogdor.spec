%global	_commit	bae7f2275cd7ccd73111662e25b124c082f296ea
%global	_shortcommit	%(c=%{commit}; echo ${c:0:7})

%global _modemfwdir     qcom/sc7180-trogdor
%global	_firmwarepath	/usr/lib/firmware/%_modemfwdir

Name:		linux-firmware-trogdor
Version:	20230713
Release:	1%{?dist}
Summary:	Modem firmware for trodgor ChromeOS devices
BuildArch:	noarch
ExclusiveArch:	aarch64
License:	Proprietary
URL:		https://gitlab.com/jenneron/firmware-google-trogdor
Source0:	%url/-/archive/%_commit/firmware-google-trogdor-$_commit.tar.gz

Requires:	linux-firmware

%description
Modem firmware for trodgor ChromeOS devices. Also required for WiFi on non-LTE models.

%prep
%autosetup -n firmware-google-trogdor-%_commit

%build

%install
install -Dm644 %_modemfwdir/modem/mba.mbn -t %{buildroot}/%_firmwarepath/modem
install -Dm644 %_modemfwdir/modem/qdsp6sw.mbn -t %{buildroot}/%_firmwarepath/modem
install -Dm644 %_modemfwdir/modem-nolte/mba.mbn -t %{buildroot}/%_firmwarepath/modem-nolte
install -Dm644 %_modemfwdir/modem-nolte/qdsp6sw.mbn -t %{buildroot}/%_firmwarepath/modem-nolte


%files
%_firmwarepath/modem/*
%_firmwarepath/modem-nolte/*

%changelog
* Sun Oct 27 2024 WeirdTreeThing <bradyn127@protonmail.com>
- Initial release
