%define debug_package %{nil}
Name:           ukui-system-monitor
Version:        1.0.4
Release:        1
Summary:        A simple system monitor written in QT
License:        GPL-3+ GPL-2+
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires: cmake >= 2.6
BuildRequires: qt5-qtbase-devel >= 5.1
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qttools-devel
BuildRequires: pkgconf
BuildRequires: glib2-devel >= 2.46.0
BuildRequires: libgtop2-devel
BuildRequires: systemd-devel >= 209
BuildRequires: gsettings-qt-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: libpcap-devel
BuildRequires: kf5-kwindowsystem-devel

Requires: libcap
Requires: glib2

%description
A simple system monitor written in QT

%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build}
popd

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd

%post
setcap "cap_net_admin,cap_net_raw+ep" /usr/bin/ukui-system-monitor
set -e
glib-compile-schemas /usr/share/glib-2.0/schemas/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc debian/changelog
%{_bindir}/ukui-system-monitor
%{_datadir}/applications/ukui-system-monitor.desktop
%{_datadir}/icons/hicolor/ukui-system-monitor.png
%{_datadir}/glib-2.0/schemas/org.ukui.system-monitor.menu.gschema.xml

%changelog
* Wed Dec 16 2020 lvhan <lvhan@kylinos.cn> - 1.0.4-1
- update to upstream version 1.0.4-1

* Wed Dec 16 2020 lvhan <lvhan@kylinos.cn> - 1.0.1-2
- removes transparency

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 1.0.1-1
- update to upstream version 1.0.0-1+1027

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 0.1.1-1
- Init package for openEuler
