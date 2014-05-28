#
# spec file for package wine-pipelight
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# The 32bit package (wine-32bit) can be obtained using the following command:
#   osc build --baselibs --disable-debuginfo <openSUSE version> i586 wine.spec
#
# If the package is to be installed with a different prefix, change it here
# using %%define _prefix /usr/lib/wine-<suffix>
%define _prefix /opt/wine-compholio
%define changedprefix %(test %_prefix != /usr && echo "1" || echo "0")

%if 0%{?changedprefix}
%define _bindir %_prefix/bin
%ifarch  x86_64
%define _libdir %_prefix/lib64
%else
%define _libdir %_prefix/lib
%endif
%define _mandir %_prefix/man
%define _includedir %_prefix/include
%define _defaultdocdir %_prefix/share/doc
%endif

# The variable prjname points to the wine project name, and should therefor
# probably stay the same forever.
#
# The package name, that is defined by the rpm tag Name, may be changed
# which will result in a different package name.  In combination with a
# different file path location (_prefix), it could be installed along side
# the wine package that is provided by openSUSE (the distribution).
%define prjname wine

Name:           wine-compholio

# Is this a native (openSUSE distribution) package?
# modpkgname: Modified Package Name
%define modpkgname %(test %name != "wine" && echo "1" || echo "0")

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
Release:        1
Summary:        An MS Windows Emulator (with pipelight patches)
License:        LGPL-2.1+
Group:          Emulators
Url:            http://www.winehq.org/
Source0:        http://mirrors.ibiblio.org/wine/source/%(echo %version |cut -d. -f1-2)/%{prjname}-%{version}.tar.bz2
#Source0:	http://77.254.128.249/src/%{prjname}/%{prjname}-%{version}.tar.bz2
#Source42:	http://77.254.128.249/src/%{prjname}/%{prjname}-%{version}.tar.bz2.sign
Source41:       wine.keyring
Source42:       http://mirrors.ibiblio.org/wine/source/%(echo %version |cut -d. -f1-2)/%{prjname}-%{version}.tar.bz2.sign
Patch0:         susepatches.patch
Source1:        winetricks
Source11:       winetricks.1
Source2:        http://kegel.com/wine/wisotool
Source3:        README.SuSE
Source4:        wine.desktop
Source5:        ubuntuwine.tar.bz2
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

%if %{modpkgname}
  %if %{changedprefix}
    %define pkgconflict 0
  %else
    %define pkgconflict 1
Conflicts:      wine
  %endif
%else
  %define pkgconflict 0
%endif

%if 0%{?suse_version} > 1120
%ifarch x86_64
Requires:       %{name}32 = %{version}
%endif
%endif
%ifarch %ix86 x86_64
Requires:       wine-gecko >= 2.24
%endif
# for ntlm_auth helper
Requires:       samba-winbind
# wine-mp3 is built at Packman, not in OBS
Recommends:     wine-mp3
# We built it here, but it is kind of large
Recommends:     wine-mono
# for DOS support
Recommends:     dosbox
# To have correct Pulseaudio support.
Recommends:     alsa-plugins
Recommends:     alsa-plugins-pulse
# for winetricks:
Requires:       cabextract
Requires:       unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%if 0%{?suse_version} > 1220
%if ! %{modpkgname}
%gpg_verify %{S:42}
%endif
%endif
%setup -q -n wine-%realver
%patch0 -p1

### Netflix patches

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
#
cp %{SOURCE3} .
#

%build
cat VERSION
%ifarch %ix86
# Steam wants proper %ebp frames to hook functions
export RPM_OPT_FLAGS=`echo %{optflags}|sed -e 's/-fomit-frame-pointer//'`
%endif
%if 0%{?suse_version} == 1110
if [ -f /usr/bin/gcc-4.6 ]; then
	export CC=gcc-4.6
fi
if [ -f /usr/bin/gcc-4.7 ]; then
	export CC=gcc-4.7
fi
%else
export CC=gcc
%endif

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
%ifarch %ix86
grep SONAME_ config.log
( echo "# autogenerated in .spec file"
  echo "%name"
  echo " +^%{_prefix}/bin/wine\$"
  echo " +^%{_prefix}/bin/wine-preloader\$"
  echo " +^%{_prefix}/lib/wine/fakedlls"
  %if %{pkgconflict}
    echo " conflicts \"wine\""
  %endif
  grep SONAME_ config.log|grep -v 'so"'|sed -e 's/^.*\(".*"\).*$/	requires \1/;'|sort -u
%if 0%{?suse_version} >= 1210
  echo " recommends \"alsa-plugins-pulse-32bit\""
  echo " recommends \"alsa-plugins-32bit\""
%endif
%if 0%{?suse_version} >= 1310
  echo " requires \"p11-kit-32bit\""
%endif
  echo "%name-devel"
  echo "  +^%{_prefix}/lib/wine/.*def"
) > %SOURCE7
cat %SOURCE7
%endif

make %{?_smp_mflags} depend
make %{?_smp_mflags} all

%install
make install DESTDIR=$RPM_BUILD_ROOT
# install desktop file
install -d %{buildroot}%{_datadir}/applications/
install -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/applications/
install -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/applications/
install -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/
mv %{buildroot}/%{_mandir}/de.UTF-8 %{buildroot}/%{_mandir}/de
mv %{buildroot}/%{_mandir}/fr.UTF-8 %{buildroot}/%{_mandir}/fr
mv %{buildroot}/%{_mandir}/pl.UTF-8 %{buildroot}/%{_mandir}/pl
install -c %{SOURCE11} %{buildroot}/%{_mandir}/man1/

%if 0%{?changedprefix}

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

tar xjf %{SOURCE5}
# Copied from Ubuntu Wine out of debian.diff
# https://launchpad.net/~ubuntu-wine/+archive/ppa/+packages
# taken on 1.2rc2 time.
( cd ubuntuwine

  install -d %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
  %if ! 0%{?changedprefix}
    # Do not install the menu file, when the prefix has changed (it is not the default
    # openSUSE package anymore).  A solution could be to change the installed file name
    # to e.g. %%name.menu, but that could result in a duplicated menu structure, besides
    # that the menu related files (.desktop, .directory, etc) probably not installed in
    # a directory that is searched by the menu maker.  Leave it here as a todo item.
    install -c -m 644 wine.menu %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
  %endif

  # Install application-specific desktop files
  install -d %{buildroot}%{_datadir}/applications
  install -c -m 644 *.desktop %{buildroot}%{_datadir}/applications/

  install -d %{buildroot}%{_datadir}/desktop-directories/
  install -c -m 644 *.directory %{buildroot}%{_datadir}/desktop-directories/

  # Install icons
  install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
  install -c -m 644 *.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
)

# breaks btrfs installation, see bnc#723402
# fdupes %{buildroot}

%if 0%{?suse_version}
%suse_update_desktop_file wine
%endif


%clean
rm -rf %{buildroot}

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
%dir %{_sysconfdir}/xdg/menus/
%dir %{_sysconfdir}/xdg/menus/applications-merged
%if ! 0%{?changedprefix}
%config %{_sysconfdir}/xdg/menus/applications-merged/*.menu
%endif
%{_datadir}/applications/*.desktop
%dir %{_datadir}/desktop-directories/
%{_datadir}/desktop-directories/*.directory
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%ifarch %ix86
%{_bindir}/wine
%{_bindir}/wine-preloader
%endif
%ifarch x86_64
%{_bindir}/wine64
%{_bindir}/wine64-preloader
%endif
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
%if 0%{?changedprefix}
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

