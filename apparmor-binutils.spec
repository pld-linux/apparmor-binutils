#
# Conditional build:
%bcond_with	static	# link statically with libapparmor

Summary:	Basic AppArmor binary utilities
Summary(pl.UTF-8):	Podstawowe narzędzia AppArmor w postaci binarnej
Name:		apparmor-binutils
Version:	2.13.3
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://launchpad.net/apparmor/2.13/%{version}/+download/apparmor-%{version}.tar.gz
# Source0-md5:	81468fb2b7ba7966910f617371073391
URL:		http://wiki.apparmor.net/
BuildRequires:	libapparmor-devel >= 1:%{version}
%{?with_static:BuildRequires:	libapparmor-static >= 1:%{version}}
%{!?with_static:Requires:	libapparmor >= 1:%{version}}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic AppArmor utilities written in compiled languages.

%description -l pl.UTF-8
Podstawowe narzędzia AppArmor napisane w językach kompilowanych.

%prep
%setup -q -n apparmor-%{version}

%build
%{__make} -C binutils \
	%{!?with_static:AALIB="-lapparmor -lpthread"} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	USE_SYSTEM=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C binutils install \
	DESTDIR=$RPM_BUILD_ROOT \
	USE_SYSTEM=1

%find_lang aa-binutils

%clean
rm -rf $RPM_BUILD_ROOT

%files -f aa-binutils.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aa-enabled
%attr(755,root,root) %{_bindir}/aa-exec
%{_mandir}/man1/aa-enabled.1*
%{_mandir}/man1/aa-exec.1*
