Summary:	A GTK+ tool to configure window decorations in beryl
Summary(pl):	Narzêdzie GTK+ do konfiguracji dekoracji okien w berylu
Name:		emerald
Version:	20061201
Release:	1
License:	GPL/MIT
Group:		X11
#Source0:	http://distfiles.xgl-coffee.org/emerald/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	e0ec3812a8d1a284ff8ac2ea94b56fdc
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	beryl-core-devel
BuildRequires:	dbus-glib-devel >= 0.50
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libwnck-devel >= 2.14.1-2
BuildRequires:	pango-devel >= 1.10.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXrender-devel >= 0.8.4
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
Requires:	beryl-core-devel
Requires:	dbus-glib-devel >= 0.50
Requires:	gtk+2-devel >= 2:2.8.0
Requires:	libwnck-devel >= 2.14.1-2
Requires:	pango-devel >= 1.10.0
Requires:	xorg-lib-libXrender-devel >= 0.8.4

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libemeraldengine.so.*.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/engines
%attr(755,root,root) %{_libdir}/%{name}/engines/*.so
%{_desktopdir}/emerald-theme-manager.desktop
%{_datadir}/mime-info/emerald.mime
%{_datadir}/mime/packages/emerald.xml
%{_datadir}/%{name}
%{_pixmapsdir}/emerald-theme-manager-icon.png
%{_iconsdir}/hicolor/*/*/*.png
%{_pkgconfigdir}/emeraldengine.pc
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libemeraldengine.so
%{_libdir}/libemeraldengine.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libemeraldengine.a
