#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Session-Store-File
Summary:	Catalyst::Plugin::Session::Store::File - File storage backend for session data.
#Summary(pl):	
Name:		perl-Catalyst-Plugin-Session-Store-File
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2796715237ffcc1c7b6ca7065d4a1792
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Cache-Cache >= 1.02
BuildRequires:	perl-Catalyst-Plugin-Session >= 0.01
BuildRequires:	perl-Class-Accessor >= 0.22
BuildRequires:	perl-Class-Data-Inheritable >= 0.04
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catalyst::Plugin::Session::Store::File is an easy to use storage
plugin for Catalyst that uses an simple file to act as a shared memory
interprocess cache. It is based on Cache::FileCache.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes readme
%{perl_vendorlib}/Catalyst/Plugin/Session/Store/*.pm
%{_mandir}/man3/*
