%define upstream_name    App-SmokeBox-PerlVersion
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	SmokeBox helper module to determine perl version
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(POE)
BuildRequires:	perl(POE::Quickie)
BuildArch:	noarch

%description
App::SmokeBox::PerlVersion is a simple helper module for the
App::SmokeBox::Mini manpage and the minismokebox manpage that determines
and version and architecture of a given 'perl' executable.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 654215
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 625083
- import perl-App-SmokeBox-PerlVersion

