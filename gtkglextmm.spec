Summary:	C++ wrapper for GtkGLExt library
Summary(pl.UTF-8):	Interfejs C++ do biblioteki GtkGLExt
Name:		gtkglextmm
Version:	1.2.0
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gtkglext/%{name}-%{version}.tar.bz2
# Source0-md5:	27c05f4d45c5fd07b6fb0f044add3056
Patch0:		gdkspanfunc.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-glibmm.patch
URL:		http://gtkglext.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	gtkglext-devel >= 1.0.0
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	mm-common
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
gtkglextmm is C++ wrapper for GtkGLExt, OpenGL Extension to GTK.

%description -l pl.UTF-8
gtkglextmm to interfejs C++ do GtkGLExt - rozszerzenia OpenGL dla GTK.

%package devel
Summary:	Header files for gtkglextmm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gtkglextmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkglext-devel >= 1.0.0
Requires:	gtkmm-devel >= 2.4.0

%description devel
Header files for gtkglextmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtkglextmm.

%package static
Summary:	Static gtkglextmm library
Summary(pl.UTF-8):	Statyczna biblioteka gtkglextmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtkglextmm library.

%description static -l pl.UTF-8
Statyczna biblioteka gtkglextmm.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgdkglextmm-x11-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdkglextmm-x11-1.2.so.0
%attr(755,root,root) %{_libdir}/libgtkglextmm-x11-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkglextmm-x11-1.2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdkglextmm-x11-1.2.so
%attr(755,root,root) %{_libdir}/libgtkglextmm-x11-1.2.so
%{_libdir}/gtkglextmm-1.2
%{_includedir}/gtkglextmm-1.2
%{_aclocaldir}/gtkglextmm-1.2.m4
%{_pkgconfigdir}/gdkglextmm-1.2.pc
%{_pkgconfigdir}/gdkglextmm-x11-1.2.pc
%{_pkgconfigdir}/gtkglextmm-1.2.pc
%{_pkgconfigdir}/gtkglextmm-x11-1.2.pc
%{_gtkdocdir}/gtkglextmm-1.2

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdkglextmm-x11-1.2.a
%{_libdir}/libgtkglextmm-x11-1.2.a
