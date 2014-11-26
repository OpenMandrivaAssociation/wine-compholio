%define	lib_major	1
%define	lib_name	%mklibname %{name} %{lib_major}
%define	lib_name_devel	%{mklibname -d %{name}}

%define _fortify_cflags %nil

Name:		wine-compholio
Version:	1.7.31
Release:	1
Epoch:		1
Summary:	WINE Is Not An Emulator - runs MS Windows programs
License:	LGPLv2+
Group:		Emulators
URL:		http://www.winehq.com/
Source0:	http://mirrors.ibiblio.org/wine/source/1.7/wine-%{version}.tar.bz2
Source1:	http://mirrors.ibiblio.org/wine/source/1.7/wine-%{version}.tar.bz2.sign
Source2:	wine-compholio-%{version}.tar.gz # wine patches
Source3:	wine-compholio.rpmlintrc

%ifarch x86_64
%define	wine	%{name}64
%define	mark64	()(64bit)
%else
%define	wine	%{name}
%define	mark64	%{nil}
%endif

%define _prefix /opt/%{name}
Prefix:     /opt/%{name}

# (anssi) Wine needs GCC 4.4+ on x86_64 for MS ABI support. Note also that
# 64-bit wine cannot run 32-bit programs without wine32.
ExclusiveArch:	%{ix86}
%if %{mdkversion} >= 201010
ExclusiveArch:	x86_64
%endif
%ifarch x86_64
BuildRequires:	gcc >= 4.4
%endif

BuildRequires:	wget
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gpm-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(sane-backends)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	autoconf
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd-sgml
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd-sgml
BuildRequires:	sgml-tools
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	isdn4k-utils-devel
BuildRequires:	glibc-static-devel
BuildRequires:	chrpath
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	desktop-file-utils
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	valgrind
BuildRequires:	gsm-devel
BuildRequires:	unixODBC-devel
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xinerama) 
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(sm)
BuildRequires:	fontforge
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	prelink

# Wine-compholio specific
BuildRequires:	gawk unzip coreutils util-linux

%ifarch x86_64
%package -n	%{wine}
%endif
Summary:	WINE Is Not An Emulator - runs MS Windows programs
Group:		Emulators
%ifarch x86_64
Conflicts:	%{name}
Suggests:	%{name}-common = %{EVRD}
%else
Conflicts:	%{name}64
Requires:	%{name}-common = %{EVRD}
%endif
Provides:	%{lib_name} = %{EVRD}
Obsoletes:	%{lib_name} <= %{EVRD}
Provides:	%{name}-bin = %{EVRD}

%ifarch %{ix86}
%package -n	%{name}-common
Summary:	WINE Is Not An Emulator - runs MS Windows programs (32-bit common files)
Group:		Emulators
Requires:	%{name}-bin = %{EVRD}
%endif


%define desc Wine is a program which allows running Microsoft Windows programs \
(including DOS, Windows 3.x and Win32 executables) on Unix. It \
consists of a program loader which loads and executes a Microsoft \
Windows binary, and a library (called Winelib) that implements Windows \
API calls using their Unix or X11 equivalents.  The library may also \
be used for porting Win32 code into native Unix executables. \
This specific build contains patches to increase the compatibility \
with Silverlight and Netflix.

%description
%desc

%ifarch x86_64
%description -n %{wine}
%desc
%else
%description -n	%{name}-common
Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x and Win32 executables) on Unix.

This package contains the files needed to support 32-bit Windows
programs, and is used by both wine-compholio and wine-compholio64.
%endif

%package -n	%{wine}-devel
Summary:	Static libraries and headers for %{name} (64-bit)
Group:		Development/C
Requires:	%{wine} = %{EVRD}
%ifarch x86_64
Conflicts:	%{name}-devel
%else
Conflicts:	%{name}64-devel
%endif
Provides:	%{lib_name_devel} = %{EVRD}
Obsoletes:	%{lib_name_devel} <= %{EVRD}
%description -n	%{wine}-devel
Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x and Win32 executables) on Unix.

This package contains the libraries and header files needed to
develop programs which make use of wine.

%prep
%setup -q -n wine-%{version}
/usr/bin/gzip -dc "%{SOURCE2}" | /bin/tar -xf - --strip-components=1

%build
make -C "patches" DESTDIR="%{_builddir}/wine-%{version}" install
%ifarch %ix86
export CFLAGS="%{optflags} -fno-omit-frame-pointer"
%endif

# Clang doesn't support M$ ABI on 64bit
export CC=gcc
export CXX=g+

export CFLAGS="$CFLAGS -DHAVE_ATTR_XATTR_H=1"
%ifarch x86_64
%configure	--with-x --with-xattr --without-gstreamer --enable-win64
%else
%configure	--with-x --with-xattr --without-gstreamer
%endif
%make depend
%make

%install
%makeinstall_std LDCONFIG=/bin/true
%ifarch x86_64
sed -i 's,Exec=wine ,Exec=wine64 ,' %{buildroot}%{_datadir}/applications/wine.desktop
%endif

%files -n %{wine}
%doc ANNOUNCE AUTHORS README
%ifarch x86_64
%{_bindir}/wine64
%{_bindir}/wine64-preloader
%endif
%{_bindir}/winecfg
%{_bindir}/wineconsole*
%{_bindir}/wineserver
%{_bindir}/wineboot
%{_bindir}/function_grep.pl
%{_bindir}/msiexec
%{_bindir}/notepad
%{_bindir}/regedit
%{_bindir}/winemine
%{_bindir}/winepath
%{_bindir}/regsvr32
%{_bindir}/winefile
%{_mandir}/man?/wine.?*
%lang(de) %{_mandir}/de.UTF-8/man?/wine.?*
%lang(de) %{_mandir}/de.UTF-8/man?/winemaker.?*
%lang(de) %{_mandir}/de.UTF-8/man?/wineserver.?*
%lang(fr) %{_mandir}/fr.UTF-8/man?/*
%lang(pl) %{_mandir}/pl.UTF-8/man?/wine.?*
%{_mandir}/man?/wineserver.?*
%{_mandir}/man?/msiexec.?*
%{_mandir}/man?/notepad.?*
%{_mandir}/man?/regedit.?*
%{_mandir}/man?/regsvr32.?*
%{_mandir}/man?/wineboot.?*
%{_mandir}/man?/winecfg.?*
%{_mandir}/man?/wineconsole.?*
%{_mandir}/man?/winefile.?*
%{_mandir}/man?/winemine.?*
%{_mandir}/man?/winepath.?*
%dir %{_datadir}/wine
%{_datadir}/wine/wine.inf
%{_datadir}/wine/l_intl.nls
%{_datadir}/applications/*.desktop
%dir %{_datadir}/wine/fonts
%{_datadir}/wine/fonts/*

%ifarch %{ix86}
%files -n %{name}-common
%{_bindir}/wine
%{_bindir}/wine-preloader
%endif

%{_libdir}/libwine*.so.%{lib_major}*
%dir %{_libdir}/wine
%{_libdir}/wine/*.cpl.so
%{_libdir}/wine/*.drv.so
%{_libdir}/wine/*.dll.so
%{_libdir}/wine/*.exe.so
%{_libdir}/wine/*.acm.so
%{_libdir}/wine/*.ocx.so
%ifarch %{ix86}
%{_libdir}/wine/*.vxd.so
%{_libdir}/wine/*16.so
%endif
%{_libdir}/wine/*.tlb.so
%{_libdir}/wine/*.ds.so
%{_libdir}/wine/*.sys.so
%{_libdir}/wine/fakedlls

%files -n %{wine}-devel
%{_libdir}/wine/*.a
%{_libdir}/libwine*.so
%{_libdir}/wine/*.def
%{_includedir}/*
%{_bindir}/wmc
%{_bindir}/wrc
%{_bindir}/winebuild
%{_bindir}/winegcc
%{_bindir}/wineg++
%{_bindir}/winecpp
%{_bindir}/widl
%{_bindir}/winedbg
%{_bindir}/winemaker
%{_bindir}/winedump
%{_mandir}/man1/wmc.1*
%{_mandir}/man1/wrc.1*
%{_mandir}/man1/winebuild.1*
%{_mandir}/man1/winemaker.1*
%{_mandir}/man1/winedump.1*
%{_mandir}/man1/widl.1*
%{_mandir}/man1/winedbg.1*
%{_mandir}/man1/wineg++.1*
%{_mandir}/man1/winegcc.1*
%{_mandir}/man1/winecpp.1*

