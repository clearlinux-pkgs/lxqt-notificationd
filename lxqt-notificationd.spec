#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE793007AD22DF7E (tsujan2000@gmail.com)
#
Name     : lxqt-notificationd
Version  : 1.2.0
Release  : 12
URL      : https://github.com/lxqt/lxqt-notificationd/releases/download/1.2.0/lxqt-notificationd-1.2.0.tar.xz
Source0  : https://github.com/lxqt/lxqt-notificationd/releases/download/1.2.0/lxqt-notificationd-1.2.0.tar.xz
Source1  : https://github.com/lxqt/lxqt-notificationd/releases/download/1.2.0/lxqt-notificationd-1.2.0.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: lxqt-notificationd-bin = %{version}-%{release}
Requires: lxqt-notificationd-data = %{version}-%{release}
Requires: lxqt-notificationd-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kwindowsystem-dev
BuildRequires : liblxqt-dev
BuildRequires : lxqt-build-tools
BuildRequires : qtbase-dev
BuildRequires : qttools-dev

%description
# lxqt-notificationd
## Overview
`lxqt-notificationd` is LXQt's implementation of a daemon according to the
[Desktop Notifications Specification](https://specifications.freedesktop.org/notification-spec/latest/).

%package bin
Summary: bin components for the lxqt-notificationd package.
Group: Binaries
Requires: lxqt-notificationd-data = %{version}-%{release}
Requires: lxqt-notificationd-license = %{version}-%{release}

%description bin
bin components for the lxqt-notificationd package.


%package data
Summary: data components for the lxqt-notificationd package.
Group: Data

%description data
data components for the lxqt-notificationd package.


%package license
Summary: license components for the lxqt-notificationd package.
Group: Default

%description license
license components for the lxqt-notificationd package.


%prep
%setup -q -n lxqt-notificationd-1.2.0
cd %{_builddir}/lxqt-notificationd-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667856025
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1667856025
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxqt-notificationd
cp %{_builddir}/lxqt-notificationd-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/lxqt-notificationd/7fab4cd4eb7f499d60fe183607f046484acd6e2d || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lxqt-config-notificationd
/usr/bin/lxqt-notificationd

%files data
%defattr(-,root,root,-)
/usr/share/applications/lxqt-config-notificationd.desktop
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_ar.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_arn.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_ast.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_bg.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_ca.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_cs.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_cy.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_da.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_de.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_el.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_en_GB.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_es.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_et.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_fr.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_gl.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_he.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_hr.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_hu.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_id.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_it.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_ja.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_ko.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_lt.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_lv.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_nb_NO.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_nl.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_oc.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_pl.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_pt.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_pt_BR.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_ru.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_si.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_sk_SK.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_tr.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_uk.qm
/usr/share/lxqt/translations/lxqt-config-notificationd/lxqt-config-notificationd_zh_CN.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_ar.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_arn.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_ast.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_bg.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_ca.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_cs.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_cy.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_da.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_de.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_el.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_en_GB.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_es.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_et.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_fr.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_gl.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_he.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_hr.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_hu.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_id.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_it.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_ja.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_ko.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_lt.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_lv.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_nb_NO.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_nl.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_pl.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_pt.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_pt_BR.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_ru.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_si.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_sk_SK.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_sv.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_tr.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_uk.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_vi.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_zh_CN.qm
/usr/share/lxqt/translations/lxqt-notificationd/lxqt-notificationd_zh_TW.qm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxqt-notificationd/7fab4cd4eb7f499d60fe183607f046484acd6e2d
