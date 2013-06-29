Name:           xf86-input-synaptics
Version:        1.6.2
Release:        0
License:        MIT
Summary:        Synaptics touchpad input driver for the Xorg X server
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Servers/XF86_4
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Source1001: 	xf86-input-synaptics.manifest
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.2
BuildRequires:  pkgconfig(xorg-macros) >= 1.13
BuildRequires:  pkgconfig(xorg-server) >= 1.7
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtst)
Requires:       udev

%description
synaptics is an Xorg input driver for touchpads.

Even though touchpads can be handled by the normal evdev or mouse
drivers, this driver allows more advanced features of the touchpad to
become available.

%package devel
Summary:        Synaptics touchpad input driver for the Xorg X server -- Development Files
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}

%description devel
synaptics is an Xorg input driver for touchpads.

Even though touchpads can be handled by the normal evdev or mouse
drivers, this driver allows more advanced features of the touchpad to
become available.

%prep
%setup -q
cp %{SOURCE1001} .

%build
autoreconf -fi
%configure --with-xorg-conf-dir=/etc/X11/xorg.conf.d
make %{?_smp_mflags}

%install
%make_install

%remove_docs
%post
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change
exit 0

%postun
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change
exit 0

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc COPYING README
%config %{_sysconfdir}/X11/xorg.conf.d/50-synaptics.conf
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/synaptics_drv.so
%{_bindir}/synclient
%{_bindir}/syndaemon

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/xorg/synaptics.h
%{_includedir}/xorg/synaptics-properties.h
%{_libdir}/pkgconfig/xorg-synaptics.pc

%changelog
