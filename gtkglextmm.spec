Summary:	C++ wrapper for GtkGLExt library
Summary(pl):	Interfejs C++ do biblioteki GtkGLExt
Name:		gtkglextmm
Version:	1.0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtkglext/%{name}-%{version}.tar.bz2
# Source0-md5:	129239375d6f7162b8426c0192fc3475
URL:		http://gtkglext.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gtkglext-devel >= 1.0.0
BuildRequires:	gtkmm-devel >= 2.1
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
gtkglextmm is C++ wrapper for GtkGLExt, OpenGL Extension to GTK.

%description -l pl
gtkglextmm to interfejs C++ do GtkGLExt - rozszerzenia OpenGL dla GTK.

%package devel
Summary:	Header files for gtkglextmm library
Summary(pl):	Pliki nag³ówkowe biblioteki gtkglextmm
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtkglext-devel >= 1.0.0
Requires:	gtkmm-devel >= 2.1

%description devel
Header files for gtkglextmm library.

%description devel -l pl
Pliki nag³ówkowe biblioteki gtkglextmm.

%package static
Summary:	Static gtkglextmm library
Summary(pl):	Statyczna biblioteka gtkglextmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gtkglextmm library.

%description static -l pl
Statyczna biblioteka gtkglextmm.

%prep
%setup -q

%build
# relink issue
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/gtkglextmm-1.0
%{_includedir}/gtkglextmm-1.0
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/gtkglextmm-1.0

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
