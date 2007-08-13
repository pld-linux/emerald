Summary:	An alternative themeable window decorator
Summary(pl.UTF-8):	Alternatywny dekorator okien z obsługą motywów
Name:		emerald
Version:	0.5.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	149c17b0a1bddf29e1cd66d29777d96e
Patch0:		%{name}-desktop.patch
URL:		http://forum.compiz-fusion.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	compiz-devel >= %{version}
BuildRequires:	dbus-glib-devel >= 0.50
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libwnck-devel >= 2.14.1-2
BuildRequires:	pango-devel >= 1.10.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libXrender-devel >= 0.8.4
BuildRequires:	xorg-lib-libXres-devel >= 1.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	compiz >= %{version}
Obsoletes:	cgwd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
emerald is window manager and tool to configure window decorations in
compiz, it use themes for windows' decorations.

%description -l pl.UTF-8
emerald to zarządca okien oraz narzędzie GTK+ do konfiguracji
dekoracji okien w compizie.

%package devel
Summary:	Header files for Emerald Engines library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Emerald Engines
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	compiz-devel >= %{version}
Requires:	dbus-glib-devel >= 0.50
Requires:	gtk+2-devel >= 2:2.8.0
Requires:	libwnck-devel >= 2.14.1-2
Requires:	pango-devel >= 1.10.0
Requires:	xorg-lib-libXrender-devel >= 0.8.4

%description devel
Header files for Emerald Engines library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Emerald Engines.

%package static
Summary:	Static Emerald Engines library
Summary(pl.UTF-8):	Statyczna biblioteka Emerald Engines
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Emerald Engines library.

%description static -l pl.UTF-8
Statyczna biblioteka Emerald Engines.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-mime-update
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/engines/*.{la,a}
# obsoleted GNOME mime-info stuff
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post
%update_mime_database
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libemeraldengine.so.*.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/engines
%attr(755,root,root) %{_libdir}/%{name}/engines/*.so
%{_datadir}/%{name}
%{_datadir}/mime/packages/emerald.xml
%{_desktopdir}/emerald-theme-manager.desktop
%{_pixmapsdir}/emerald-theme-manager-icon.png
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libemeraldengine.so
%{_libdir}/libemeraldengine.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_pkgconfigdir}/emeraldengine.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libemeraldengine.a
