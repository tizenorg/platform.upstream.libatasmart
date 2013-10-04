Name:     libatasmart
Summary:  The libatasmart
Version:  0.19
Release:  1
License:  GPL 2
Group:    System Environment/Kernel
URL:      http://code.google.com/p/cryptsetup/
Source0:  %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(systemd)
BuildRequires: device-mapper-devel
BuildRequires: pkgconfig(libudev)


%description
setup cryptographic volumes for dm-crypt (including LUKS extension)

%prep
%setup -q

%build
./autogen.sh
%configure CFLAGS='-g -O0 -Wp,-U_FORTIFY_SOURCE' --sysconfdir=/etc --localstatedir=/var --libdir=/usr/lib --libexecdir=/usr/lib

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%clean

%post

%files
/usr/include/atasmart.h
/usr/lib/libatasmart.so
/usr/lib/libatasmart.so.4
/usr/lib/libatasmart.so.4.0.5
/usr/lib/pkgconfig/libatasmart.pc
/usr/sbin/skdump
/usr/sbin/sktest
/usr/share/doc/libatasmart/README
/usr/share/vala/vapi/atasmart.vapi
