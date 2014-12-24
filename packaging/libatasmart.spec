Name:     libatasmart
Summary:  The libatasmart
Version:  0.19
Release:  1
License:  GPL-2.0
Group:    Base/Device Management
URL:      http://code.google.com/p/cryptsetup/
Source0:  %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libudev)
BuildRequires: device-mapper-devel

Requires:      libdevmapper

%description
setup cryptographic volumes for dm-crypt (including LUKS extension)

%package devel
License:  LGPL-2.1
Summary:  The development libatasmart
Group:    Base/Device Management
Requires: %{name} = %{version}-%{release}

%description devel
setup cryptographic volumes for dm-crypt (including LUKS extension) - development package.

%prep
%setup -q

%build
./autogen.sh
%configure CFLAGS="${CFLAGS} -g -O0 -Wp,-U_FORTIFY_SOURCE" --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --libdir=%{_libdir} --libexecdir=%{_libdir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean

%files
%{_libdir}/libatasmart.so
%{_libdir}/libatasmart.so.4
%{_libdir}/libatasmart.so.4.0.5
%{_sbindir}/skdump
%{_sbindir}/sktest
%{_datarootdir}/doc/libatasmart/README
%{_datarootdir}/vala/vapi/atasmart.vapi

%files devel
%{_includedir}/atasmart.h
%{_libdir}/libatasmart.so
%{_libdir}/pkgconfig/libatasmart.pc
