#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Catalyst
%define	pnam	Plugin-Session-Store-File
Summary:	Catalyst::Plugin::Session::Store::File - File storage backend for session data
Summary(pl.UTF-8):	Catalyst::Plugin::Session::Store::File - przechowywanie danych sesji w pliku
Name:		perl-Catalyst-Plugin-Session-Store-File
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f1d2d3ed5ef2f800df5e7518a57ea1e1
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Session-Store-File/
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

%description -l pl.UTF-8
Catalyst::Plugin::Session::Store::File to łatwa w użyciu wtyczka
przechowywania danych dla Catalysta używajaca zwykłego pliku jako
pamięci podręcznej współdzielonej między procesami. Jest oparta na
Cache::FileCache.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -we 'WriteMakefile(NAME=>"Catalyst::Plugin::Session::Store::File")' \
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
%doc Changes
%{perl_vendorlib}/Catalyst/Plugin/Session/Store/*.pm
%{_mandir}/man3/*
