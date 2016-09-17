Summary:	An abstract library implementation of a VT220/xterm/ECMA-48 terminal emulator
Name:		libvterm
Version:	0.1
Release:	1
License:	MIT
Group:		Libraries
# using github mirror
# as it's just easier to get tarball
Source0:	https://github.com/neovim/libvterm/archive/487f21d/%{name}-%{version}.tar.gz
# Source0-md5:	29f2831ef7ca7a651e38bca91e8caf55
# https://launchpad.net/libvterm
URL:		http://www.leonerd.org.uk/code/libvterm/
BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An abstract C99 library which implements a VT220 or xterm-like
terminal emulator. It doesn't use any particular graphics toolkit or
output system, instead it invokes callback function pointers that its
embedding program should provide it to draw on its behalf. It avoids
calling malloc() during normal running state, allowing it to be used
in embedded kernel situations.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -c %{name}-%{version}
mv %{name}-*/* .

%build
%{__make} \
	VERBOSE=1 \
	CFLAGS="%{optflags} -std=gnu99" \
	INCDIR="%{_includedir}" \
	LIBDIR="%{_libdir}" \
	MANDIR="%{_mandir}" \
	PREFIX="%{_prefix}" \

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
    CFLAGS="%{optflags} -std=gnu99" \
    INCDIR="%{_includedir}" \
    LIBDIR="%{_libdir}" \
    MANDIR="%{_mandir}" \
    PREFIX="%{_prefix}" \
    DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvterm.a
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvterm.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/unterm
%attr(755,root,root) %{_bindir}/vterm-ctrl
%attr(755,root,root) %{_bindir}/vterm-dump
%attr(755,root,root) %{_libdir}/libvterm.so.*.*.*
%ghost %{_libdir}/libvterm.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/vterm.h
%{_includedir}/vterm_keycodes.h
%{_libdir}/libvterm.so
%{_pkgconfigdir}/vterm.pc
