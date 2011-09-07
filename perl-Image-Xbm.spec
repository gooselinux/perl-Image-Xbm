Name:           perl-Image-Xbm
Version:        1.08
Release:        12%{?dist}
Summary:        Load, create, manipulate and save xbm image files in Perl

Group:          Development/Libraries
License:        LGPLv2+
URL:            http://search.cpan.org/dist/Image-Xbm/
Source0:        http://www.cpan.org/authors/id/S/SU/SUMMER/Image-Xbm-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Image::Base)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This class module provides basic load, manipulate and save functionality for
the xbm file format.  It inherits from Image::Base which provides additional
manipulation functionality.


%prep
%setup -q -n Image-Xbm-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README
%{perl_vendorlib}/Image/
%{_mandir}/man3/*.3pm*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.08-12
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-8
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-7
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-6.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Sep  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-6
- Rebuild for FC6.

* Fri Feb 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-5
- Rebuild for FC5 (perl 5.8.8).

* Fri Dec 30 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-4
- Dist tag.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.08-3
- rebuilt

* Thu Jun  3 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.08-0.fdr.2
- Bring up to date with current fedora.us perl spec template.

* Sun Oct 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.08-0.fdr.1
- First build.
