%define _prefix /opt/wine-compholio
%define testpfx %(test %_prefix != /usr && echo "1" || echo "0")

%if 0%{?testpfx}
%define _bindir %_prefix/bin
%ifarch  x86_64
%define _libdir %_prefix/lib64
%else
%define _libdir %_prefix/lib
%endif
%define _includedir %_prefix/include
%define _mandir %_prefix/man
%define _defaultdocdir %_prefix/share/doc
%endif
%define virtname wine
#realname
Name:	wine-compholio

%define testpname %(test %name != "wine" && echo "1" || echo "0")

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
%if "%{distepoch}" >= "2011.0"
BuildRequires:	prelink
%endif

%define realver 1.7.19
Version:        1.7.19
Release:        2
Summary:        An MS Windows Emulator (with pipelight patches)
License:        LGPL-2.1+
Group:          Emulators
Url:            http://www.winehq.org/
Source0:        http://mirrors.ibiblio.org/wine/source/%(echo %version |cut -d. -f1-2)/%{virtname}-%{version}.tar.bz2
Patch0:         pdfpatch.patch
Source1:        winetricks
Source11:       winetricks.1
Source2:        http://kegel.com/wine/wisotool
Source4:        wine.desktop
Source6:        wine-msi.desktop
Source7:        baselibs.conf
Source100:      wine-compholio.rpmlintrc

### pipelight patches
# From: http://fds-team.de/mirror/wine-patches-minimal.tar.gz (minimal patch set)
Patch1001:      0001-server-Implement-socket-specific-ioctl-routine.patch
Patch1002:      0002-server-Add-delayed-processing-for-socket-specific-io.patch
Patch1003:      0003-server-Add-socket-side-support-for-the-interface-cha.patch
Patch1004:      0004-server-Implement-the-interface-change-notification-o.patch
Patch1005:      0005-ws2_32-Add-an-interactive-test-for-interface-change-.patch
Patch1006:      0006-server-Unify-the-storage-of-security-attributes-for-.patch
Patch1007:      0007-server-Unify-the-retrieval-of-security-attributes-fo.patch
Patch1008:      0008-server-Store-file-security-attributes-with-extended-.patch
Patch1009:      0009-server-Store-user-and-group-inside-stored-extended-f.patch
Patch1010:      0010-server-Retrieve-file-security-attributes-with-extend.patch
Patch1011:      0011-server-Convert-return-of-file-security-masks-with-ge.patch
Patch1012:      0012-server-Inherit-security-attributes-from-parent-direc.patch
Patch1013:      0013-server-Inherit-security-attributes-from-parent-direc.patch
Patch1014:      0014-shell32-Set-the-default-security-attributes-for-user.patch
Patch1015:      0015-server-Add-compatibility-code-for-handling-the-old-m.patch
Patch1016:      0016-winex11-Update-gl_drawable-for-embedded-windows.patch
Patch1017:      0017-winex11-Enable-disable-windows-when-they-are-un-mapped.patch
Patch1018:      0018-kernel32-Change-return-value-of-stub-SetNamedPipeHandl.patch
Patch1019:      0019-winex11-Implement-X11DRV_FLUSH_GDI_DISPLAY-ExtEscape-c.patch
Patch1020:      0020-user32-Decrease-minimum-SetTimer-interval-to-5-ms.patch
Patch1021:      0021-wined3d-Allow-to-set-strictDrawOrdering-via-environmen.patch
Patch1022:      0022-quartz-tests-Add-tests-for-IVMRMonitorConfig-and-IVMRM.patch
Patch1023:      0023-wined3d-Silence-repeated-resource_check_usage-FIXME.patch
Patch1024:      0024-kernel32-Silence-repeated-CompareStringEx-FIXME.patch
Patch1025:      0025-wined3d-Silence-repeated-wined3d_swapchain_present-F.patch
Patch1026:      0026-shlwapi-tests-Add-additional-tests-for-UrlCombine-and-.patch
Patch1027:      0027-shlwapi-UrlCombineW-workaround-for-relative-paths.patch
Patch1028:      0028-patch-list.patch

%if %{testpname}
  %if %{testpfx}
    %define pconflict 0
  %else
    %define pconflict 1
Conflicts:      wine
  %endif
%else
  %define pconflict 0
%endif

Requires:       wine-gecko >= 2.24
Requires:       samba-winbind
Requires:       cabextract
Requires:       unzip
Recommends:     alsa-plugins-pulse-config


%description
An MS Windows emulator, consisting of both runtime and also source
compatibility functions. You can run your MS executables with it, and
you can write your Windows programs under Linux and link against the
WINE libraries.

It is not necessary to have a Windows installation to run WINE.

Please have a look at /usr/share/doc/packages/wine/README.SuSE. There
is more documentation available in that directory. Read 'man wine' for
further information.

You can invoke wine by entering: 'wine program.exe' wine can be
configured by running 'winecfg'.

%package devel
Summary:        Files for wine development
Group:          Development/C

%description devel
This RPM contains the header files and development tools for the WINE
libraries.

%prep
%setup -q -n wine-%realver
%patch0 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
%patch1008 -p1
%patch1009 -p1
%patch1010 -p1
%patch1011 -p1
%patch1012 -p1
%patch1013 -p1
%patch1014 -p1
%patch1015 -p1
%patch1016 -p1
%patch1017 -p1
%patch1018 -p1
%patch1019 -p1
%patch1020 -p1
%patch1021 -p1
%patch1022 -p1
%patch1023 -p1
%patch1024 -p1
%patch1025 -p1
%patch1026 -p1
%patch1027 -p1
%patch1028 -p1

%build

export RPM_OPT_FLAGS=`echo %{optflags}|sed -e 's/-fomit-frame-pointer//'`
export CC=gcc
CFLAGS="-DLDAP_DEPRECATED=1 $RPM_OPT_FLAGS" \
autoreconf
%configure \
	--with-x --verbose --with-xattr \
%ifarch x86_64
        --enable-win64 \
%endif

grep "have_x=yes" config.log || exit 1
# Required for pipelight
grep "xattr_h=yes" config.log || exit 1

# generate baselibs.conf
grep SONAME_ config.log
( echo "# autogenerated in .spec file"
  echo "%name"
  echo " +^%{_prefix}/bin/wine\$"
  echo " +^%{_prefix}/bin/wine-preloader\$"
  echo " +^%{_prefix}/lib/wine/fakedlls"
  %if %{pconflict}
    echo " conflicts \"wine\""
  %endif
  grep SONAME_ config.log|grep -v 'so"'|sed -e 's/^.*\(".*"\).*$/	requires \1/;'|sort -u
  echo "%name-devel"
  echo "  +^%{_prefix}/lib/wine/.*def"
) > %SOURCE7
cat %SOURCE7
make %{?_smp_mflags} depend
make %{?_smp_mflags} all

%install
make install DESTDIR=$RPM_BUILD_ROOT
# install desktop file
install -d %{buildroot}%{_datadir}/applications/
install -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/
install -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/applications/
install -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/applications/
mv %{buildroot}/%{_mandir}/de.UTF-8 %{buildroot}/%{_mandir}/de
mv %{buildroot}/%{_mandir}/fr.UTF-8 %{buildroot}/%{_mandir}/fr
mv %{buildroot}/%{_mandir}/pl.UTF-8 %{buildroot}/%{_mandir}/pl
install -c %{SOURCE11} %{buildroot}/%{_mandir}/man1/

%if 0%{?testpfx}

  # When this wine package is not installed in the standard %prefix (/usr);
  # Create the doc directory
  install -d -m 755 %{buildroot}/%{_defaultdocdir}

  # The manpages are not automatically compressed.  Take care that they
  # are compressed.
  find %{buildroot}/%{_mandir} -type f -name "*.1"
  for MAN in $(find %{buildroot}/%{_mandir} -type f -name "*.1"); do
    gzip $MAN
  done

  ( cd %{buildroot}/%{_mandir}/man1
    rm winecpp.1 wineg++.1
    ln -s winegcc.1.gz winecpp.1.gz
    ln -s winegcc.1.gz wineg++.1.gz
  )
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%if 0%{?changedprefix}
%dir %_prefix
%dir %_bindir
%dir %_libdir
%dir %_mandir
%dir %_mandir/man1
%dir %_mandir/de
%dir %_mandir/de/man1
%dir %_mandir/fr
%dir %_mandir/fr/man1
%dir %_datadir
%dir %_datadir/applications
%dir %_datadir/icons
%dir %_defaultdocdir
%endif
%doc ANNOUNCE AUTHORS LICENSE LICENSE.OLD README*
%{_bindir}/function_grep.pl
%{_bindir}/msiexec
%{_bindir}/notepad
%{_bindir}/regedit
%{_bindir}/regsvr32
%{_bindir}/wineboot
%{_bindir}/winecfg
%{_bindir}/wineconsole
%{_bindir}/winedbg
%{_bindir}/winefile
%{_bindir}/winemine
%{_bindir}/winepath
%{_bindir}/wineserver
%{_bindir}/winetricks
%{_bindir}/wisotool
%{_datadir}/wine
#{_datadir}/applications/wine.desktop
%dir %doc %{_mandir}/pl
%dir %doc %{_mandir}/pl/man1
%doc %{_mandir}/man1/wine.1*
%doc %{_mandir}/man1/winedbg.1*
%doc %{_mandir}/man1/wineserver.1*
%doc %{_mandir}/*/man1/wine.1*
%doc %{_mandir}/*/man1/wineserver.1*
%doc %{_mandir}/man1/msiexec.1.*
%doc %{_mandir}/man1/notepad.1.*
%doc %{_mandir}/man1/regedit.1.*
%doc %{_mandir}/man1/regsvr32.1.*
%doc %{_mandir}/man1/wineboot.1.*
%doc %{_mandir}/man1/winecfg.1.*
%doc %{_mandir}/man1/wineconsole.1.*
%doc %{_mandir}/man1/winefile.1.*
%doc %{_mandir}/man1/winemine.1.*
%doc %{_mandir}/man1/winetricks.1.*
%doc %{_mandir}/man1/winepath.1.*
%{_bindir}/wine
%{_bindir}/wine-preloader
%ifarch ppc %arm
%{_bindir}/wine
%endif
%{_libdir}/wine/*.so
%{_libdir}/lib*.so.*
%dir %{_libdir}/wine
%dir %{_libdir}/wine/fakedlls
%{_libdir}/wine/fakedlls/*

%files devel
%defattr(-,root,root)
%if 0%{?testpfx}
%dir %_includedir
%endif
%{_includedir}/wine
%{_bindir}/widl
%{_bindir}/winebuild
%{_bindir}/winecpp
%{_bindir}/winedump
%{_bindir}/wineg++
%{_bindir}/winegcc
%{_bindir}/winemaker
%{_bindir}/wmc
%{_bindir}/wrc
%{_libdir}/wine/*.def
%{_libdir}/wine/*.a
%{_libdir}/lib*.so
%doc %{_mandir}/man1/winemaker.1*
%doc %{_mandir}/*/man1/winemaker.1*
%doc %{_mandir}/man1/widl.1*
%doc %{_mandir}/man1/winebuild.1.*
%doc %{_mandir}/man1/winedump.1*
%doc %{_mandir}/man1/wineg++.1*
%doc %{_mandir}/man1/winegcc.1*
%doc %{_mandir}/man1/winecpp.1.*
%doc %{_mandir}/man1/wmc.1*
%doc %{_mandir}/man1/wrc.1*



%changelog

