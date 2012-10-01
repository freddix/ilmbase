Summary:	Base math and exception libraries from OpenEXR project
Name:		ilmbase
Version:	1.0.2
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://download.savannah.nongnu.org/releases/openexr/%{name}-%{version}.tar.gz
# Source0-md5:	26c133ee8ca48e1196fbfb3ffe292ab4
Patch0:		%{name}-link.patch
Patch1:		%{name}-gcc.patch
URL:		http://www.openexr.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IlmBase consists of the following libraries:

Half is a class that encapsulates our 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.  It currently supports pthreads and
Windows threads.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%package devel
Summary:	Header files for IlmBase libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for IlmBase libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libHalf.so.6
%attr(755,root,root) %ghost %{_libdir}/libIex.so.6
%attr(755,root,root) %ghost %{_libdir}/libIlmThread.so.6
%attr(755,root,root) %ghost %{_libdir}/libImath.so.6
%attr(755,root,root) %{_libdir}/libHalf.so.*.*.*
%attr(755,root,root) %{_libdir}/libIex.so.*.*.*
%attr(755,root,root) %{_libdir}/libIlmThread.so.*.*.*
%attr(755,root,root) %{_libdir}/libImath.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libHalf.so
%attr(755,root,root) %{_libdir}/libIex.so
%attr(755,root,root) %{_libdir}/libIlmThread.so
%attr(755,root,root) %{_libdir}/libImath.so
%{_libdir}/libHalf.la
%{_libdir}/libIex.la
%{_libdir}/libIlmThread.la
%{_libdir}/libImath.la
%dir %{_includedir}/OpenEXR
%{_includedir}/OpenEXR/Iex*.h
%{_includedir}/OpenEXR/IlmBaseConfig.h
%{_includedir}/OpenEXR/IlmThread*.h
%{_includedir}/OpenEXR/Imath*.h
%{_includedir}/OpenEXR/half*.h
%{_pkgconfigdir}/IlmBase.pc
