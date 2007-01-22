Summary:	A GTK+ tool to configure window decorations in beryl
Summary(pl):	Narzêdzie GTK+ do konfiguracji dekoracji okien w berylu
Name:		emerald
Version:	0.1.99.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	fdcc88cd8e75e144a07138525e342370
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	beryl-core-devel >= 1:0.1.99.2
BuildRequires:	dbus-glib-devel >= 0.50
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libwnck-devel >= 2.14.1-2
BuildRequires:	pango-devel >= 1.10.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXrender-devel >= 0.8.4
Requires:	beryl-core >= 1:0.1.99.2
Obsoletes:	cgwd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
emerald is window manager and tool to configure window decorations in
beryl, it use themes for windows' decorations.

%description -l pl
emerald to zarz±dca okien oraz narzêdzie GTK+ do konfiguracji
dekoracji okien w berylu.

%package devel
Summary:	Header files for Emerald Engines library
Summary(pl):	Pliki nag³ówkowe biblioteki Emerald Engines
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	beryl-core-devel >= 1:0.1.3
Requires:	dbus-glib-devel >= 0.50
Requires:	gtk+2-devel >= 2:2.8.0
Requires:	libwnck-devel >= 2.14.1-2
Requires:	pango-devel >= 1.10.0
Requires:	xorg-lib-libXrender-devel >= 0.8.4

%description devel
Header files for Emerald Engines library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Emerald Engines.

%package static
Summary:	Static Emerald Engines library
Summary(pl):	Statyczna biblioteka Emerald Engines
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Emerald Engines library.

%description static -l pl
Statyczna biblioteka Emerald Engines.

%prep
%setup -q

mv -f po/{ca_ES,ca}.po
mv -f po/{es_ES,es}.po
mv -f po/{fr_FR,fr}.po
mv -f po/{gu_IN,gu}.po
mv -f po/{hu_HU,hu}.po
mv -f po/{it_IT,it}.po
mv -f po/{ja_JP,ja}.po
mv -f po/{ko_KR,ko}.po
mv -f po/{pt_PT,pt}.po
mv -f po/{sv_SE,sv}.po
mv -f po/{tr_TR,tr}.po
# sv_FI is identical to sv_SE

# NOTE: check the list after any upgrade!
cat > po/LINGUAS <<EOF
ca
en_GB
es
es_AR
fr
gu
hu
it
ja
ko
pt
PT_BR
sv
tr
zh_CN
zh_HK
zh_TW
EOF

%build
%{__intltoolize}
%{__glib_gettextize}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libemeraldengine.so.*.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/engines
%attr(755,root,root) %{_libdir}/%{name}/engines/*.so
%{_datadir}/%{name}
%{_datadir}/mime-info/emerald.mime
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
