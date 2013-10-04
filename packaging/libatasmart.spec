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
%configure CFLAGS='-g -O0 -Wp,-U_FORTIFY_SOURCE' --sysconfdir=/etc --localstatedir=/var --libdir=/usr/lib --libexecdir=/usr/lib

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean

%files
/usr/lib/libatasmart.so
/usr/lib/libatasmart.so.4
/usr/lib/libatasmart.so.4.0.5
/usr/sbin/skdump
/usr/sbin/sktest
/usr/share/doc/libatasmart/README
/usr/share/vala/vapi/atasmart.vapi

%files devel
/usr/include/atasmart.h
/usr/lib/libatasmart.so
/usr/lib/pkgconfig/libatasmart.pc
