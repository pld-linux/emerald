Summary:	A GTK+ tool to configure window decorations in beryl
Summary(pl):	Narzêdzie GTK+ do konfiguracji dekoracji okien w berylu
Name:		emerald
Version:	0.1.0
Release:	1
License:	GPL/MIT
Group:		X11
Source0:	http://distfiles.xgl-coffee.org/emerald/%{name}-%{version}.tar.bz2
# Source0-md5:	48befb8a43e7025297eb69126cd9c824
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	beryl-core-devel
BuildRequires:	dbus-devel
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool
BuildRequires:	libwnck-devel >= 2.14.1-2
BuildRequires:	pango-devel
BuildRequires:	xorg-lib-libXrandr-devel
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
emerald is window manager and tool to configure window decorations in
beryl, it use themes for windows' decorations.

%description -l pl
emerald to zarz±dca okien oraz narzêdzie GTK+ do konfiguracji
dekoracji okien w berylu.

%package devel
Summary:	Header files for emerald
Summary(pl):	Pliki nag³ówkowe dla emerald
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-devel
Requires:	libpng-devel
Requires:	startup-notification-devel >= 0.7
Requires:	xorg-lib-libSM-devel
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXrandr-devel

%description devel
Header files for emerald.

%description devel -l pl
Pliki nag³ówkowe dla emerald.

%package static
Summary:	Static files for emerald
Summary(pl):	Pliki statyczne dla emerald
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static files for emerald.

%description static -l pl
Pliki statyczne dla emerald.

%prep
%setup -q -n %{name}

%build
autoreconf -v --install
%{__intltoolize}
%{__glib_gettextize} --copy --force
%configure \
	--disable-mime-update
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/engines/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post  -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libemeraldengine.so.*.*.*
%attr(755,root,root) %{_libdir}/libemeraldengine.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/engines
%attr(755,root,root) %{_libdir}/%{name}/engines/*.so
%{_desktopdir}/emerald-theme-manager.desktop
%{_datadir}/mime-info/emerald.mime
%{_datadir}/mime/packages/emerald.xml
%{_pixmapsdir}/emerald-theme-manager-icon.png
%{_iconsdir}/hicolor/*/*/*.png
%{_pkgconfigdir}/emeraldengine.pc

%files devel
%defattr(644,root,root,755)
%{_libdir}/libemeraldengine.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libemeraldengine.a
