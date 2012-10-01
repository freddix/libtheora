Summary:	Theora - video codec intended for use within Ogg multimedia streaming system
Name:		libtheora
Version:	1.1.1
Release:	4
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.bz2
# Source0-md5:	292ab65cedd5021d6b7ddd117e07cd8e
Patch0:		%{name}-libadd.patch
URL:		http://www.theora.org/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	doxygen
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkg-config
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Theora is Xiph.Org's first publicly released video codec, intended for
use within the Ogg's project's Ogg multimedia streaming system. Theora
is derived directly from On2's VP3 codec; Currently the two are nearly
identical, varying only in framing headers, but Theora will diverge
and improve from the main VP3 development lineage as time progresses.

%package devel
Summary:	Header files for Theora library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Theora library.

%prep
%setup -q
%patch0 -p1

%build
%{__sed} -i 's,CFLAGS="-g -O2 ,CFLAGS=",' configure.ac

%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-examples \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/libtheora-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/theora
%{_pkgconfigdir}/*.pc

