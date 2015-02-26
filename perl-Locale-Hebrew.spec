#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	Hebrew
Summary:	Locale::Hebrew - Bidirectional Hebrew support
Summary(pl.UTF-8):	Locale::Hebrew - obsługa języka hebrajskiego z dwukierunkowym pismem
Name:		perl-Locale-Hebrew
Version:	1.05
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AU/AUDREYT/Locale-Hebrew-%{version}.tar.gz
# Source0-md5:	424209b23bf423f1923f9b24b5ae2179
Patch0:		format-security.patch
URL:		http://search.cpan.org/dist/Locale-Hebrew/
%{?with_tests:BuildRequires:	perl-Encode}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is based on code from the Unicode Consortium.

The charset on their code was bogus, therefore this module had to work
the real charset from scratch. There might have some mistakes, though.

One function, hebrewflip, is exported by default.

%description -l pl.UTF-8
Ten moduł jest oparty na kodzie z Unicode Consortium. Zestaw znaków w
tamtym kodzie był błędny, więc obsługa prawdziwego zestawu znaków
musiała być napisana od zera. Może jednak zawierać błędy.

Domyślnie eksportowana jest jedna funkcja - hebrewflip.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Locale/*.pm
%dir %{perl_vendorarch}/auto/Locale/Hebrew
%{perl_vendorarch}/auto/Locale/Hebrew/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Locale/Hebrew/*.so
%{_mandir}/man3/*
