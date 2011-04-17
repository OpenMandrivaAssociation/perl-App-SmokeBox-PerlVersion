%define upstream_name    App-SmokeBox-PerlVersion
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    SmokeBox helper module to determine perl version
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IPC::Cmd)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Quickie)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
App::SmokeBox::PerlVersion is a simple helper module for the
App::SmokeBox::Mini manpage and the minismokebox manpage that determines
and version and architecture of a given 'perl' executable.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


