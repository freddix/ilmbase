Summary:	Base math and exception libraries from OpenEXR project
Name:		ilmbase
Version:	2.2.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://download.savannah.nongnu.org/releases/openexr/%{name}-%{version}.tar.gz
# Source0-md5:	b540db502c5fa42078249f43d18a4652
Patch0:		%{name}-link.patch
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
Requires:	libstdc++-devel
%description devel
Header files for IlmBase libraries.

%prep
%setup -q
%patch0 -p1

%{__sed} -i "s|AM_CONFIG_HEADER|AC_CONFIG_HEADERS|" configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}
# fails on i686
#%%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libHalf.so.12
%attr(755,root,root) %ghost %{_libdir}/libIex-*.so.12
%attr(755,root,root) %ghost %{_libdir}/libIexMath-*.so.12
%attr(755,root,root) %ghost %{_libdir}/libIlmThread-*.so.12
%attr(755,root,root) %ghost %{_libdir}/libImath-*.so.12
%attr(755,root,root) %{_libdir}/libHalf.so.*.*.*
%attr(755,root,root) %{_libdir}/libIex-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libIexMath-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libIlmThread-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libImath-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libHalf.so
%attr(755,root,root) %{_libdir}/libIex.so
%attr(755,root,root) %{_libdir}/libIexMath.so
%attr(755,root,root) %{_libdir}/libIlmThread.so
%attr(755,root,root) %{_libdir}/libImath.so
%dir %{_includedir}/OpenEXR
%{_includedir}/OpenEXR/Iex*.h
%{_includedir}/OpenEXR/IlmBaseConfig.h
%{_includedir}/OpenEXR/IlmThread*.h
%{_includedir}/OpenEXR/Imath*.h
%{_includedir}/OpenEXR/half*.h
%{_pkgconfigdir}/IlmBase.pc

