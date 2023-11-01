#
# Spec file for IBM's TSS for the TPM 2.0
#
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}

%global incname ibmtss

Name:		tss2
Version:	1.6.0
Release:	7%{?dist}
Epoch:	        1
Summary:	IBM's TCG Software Stack (TSS) for TPM 2.0 and related utilities

License:	BSD
URL:		http://sourceforge.net/projects/ibmtpm20tss/
Source0:	https://sourceforge.net/projects/ibmtpm20tss/files/ibmtss%{version}.tar.gz
Patch0:         tss2-1.6.0-manpage-cleanup.patch
Patch1:		0001-utils-Update-certifyx509-for-Openssl-3.0.0.patch
Patch2:		0002-utils-Remove-unused-variables-from-certifyx509.patch
Patch3:		0003-Update-certifyx509-for-Windows.patch
Patch4:		0004-utils-Clean-up-certifyx509-memory-allocation.patch
Patch5:		0005-utils-Fix-errors-detected-by-gcc-asan.patch
Patch6:		0006-tss-Port-HMAC-operations-to-openssl-3.0.patch
Patch7:		0007-utils-Port-to-openssl-3.0.0-replaces-RSA-with-EVP_PK.patch
Patch8:		0001-utils-Generate-X509-certificate-serial-number-using-.patch
Patch9:		0001-tss-Add-missing-parameter-union-members.patch
Patch10:	0002-regtest-Update-to-SHA-256-without-restricting-the-sc.patch
Patch11:	0003-tss-Restrict-usage-of-SHA-1.patch
Patch12:	0004-man-Include-information-about-possible-hash-restrict.patch


BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires:  gcc
BuildRequires:	openssl-devel
BuildRequires:	git
Requires:	openssl

%description
TSS2 is a user space Trusted Computing Group's Software Stack (TSS) for
TPM 2.0.  It implements the functionality equivalent to the TCG TSS
working group's ESAPI, SAPI, and TCTI layers (and perhaps more) but with
a hopefully far simpler interface.

It comes with about 80 "TPM tools" that can be used for rapid prototyping,
education and debugging. 

%package devel
Summary:	Development libraries and headers for IBM's TSS 2.0
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Development libraries and headers for IBM's TSS 2.0. You will need this in
order to build TSS 2.0 applications.

%prep
%autosetup -S git -p1 -c %{name}-%{version}

%build
autoreconf -vi
%configure --disable-static --disable-tpm-1.2 --program-prefix=tss --enable-nodeprecatedalgs
CCFLAGS="%{optflags}" \
LNFLAGS="%{__global_ldflags}" \
%{make_build}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets

%files
%license LICENSE
%{_bindir}/tss*
%{_libdir}/libibmtss.so.*
%{_libdir}/libibmtssutils.so.*
%attr(0644, root, root) %{_mandir}/man1/tss*.1*

%files devel
%{_includedir}/%{incname}
%{_libdir}/libibmtss.so
%{_libdir}/libibmtssutils.so
%doc ibmtss.doc

%changelog
* Fri Jul 8 2022 Stepan Horacek <shoracek@redhat.com> - 1:1.6.0-7
- Version bump
  Resolves: rhbz#2060768

* Wed Jun 29 2022 Stepan Horacek <shoracek@redhat.com> - 1:1.6.0-6
- Restrict SHA-1 usage
  Resolves: rhbz#2060768

* Fri Jan 28 2022 Stepan Horacek <shoracek@redhat.com> - 1:1.6.0-5
- Fix failures introduced with OpenSSL 3
  Resolves: rhbz#1984621
  Resolves: rhbz#1992339

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1:1.6.0-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 16 2021 Mohan Boddu <mboddu@redhat.com> - 1:1.6.0-3
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1:1.6.0-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Feb 8 2021 Jerry Snitselaar <jsnitsel@redhat.com> - 1.6.0-1
- Rebase to v1.6.0 release.
- Manpage cleanup.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1331-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1331-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Tom Stellard <tstellar@redhat.com> - 1331-5
- Use make_build macro
- https://docs.fedoraproject.org/en-US/packaging-guidelines/#_parallel_make

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1331-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 1331-3
- Ensure tssprintcmd has the compilation compilation flags,
  PIC in particular

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1331-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jerry Snitselaar <jsnitsel@redhat.com> - 1331-1
- Rebase to version 1331

* Tue May 28 2019 Jerry Snitselaar <jsnitsel@redhat.com> - 1234-4
- Fix covscan issues
- Fix compile and linker flag issues

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1234-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1234-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jerry Snitselaar <jsnitsel@redhat.com> - 1234-1
- Version bump.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1027-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Merlin Mathesius <mmathesi@redhat.com> - 1027-1
- Version bump. Now supported for all architectures.
- Generate man pages since they are no longer included in source archive.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 713-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 713-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 713-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 05 2016 Hon Ching(Vicky) Lo <lo1@us.ibm.com> - 713-7
- Removed defattr from the devel subpackage 

* Mon Sep 26 2016 Hon Ching(Vicky) Lo <lo1@us.ibm.com> - 713-6
- Added s390x arch as another "ExcludeArch"

* Mon Sep 26 2016 Hon Ching(Vicky) Lo <lo1@us.ibm.com> - 713-5
- Replaced ExclusiveArch with ExcludeArch 
 
* Mon Sep 19 2016 Hon Ching(Vicky) Lo <lo1@us.ibm.com> - 713-4
- Used ExclusiveArch instead of BuildArch tag
- Removed attr from symlink in devel subpackage 
- Added manpages and modified the Source0
- Added CCFLAGS and LNFLAGS to enforce hardening and optimization

* Wed Aug 17 2016 Hon Ching(Vicky) Lo <lo1@us.ibm.com> - 713-3
- Modified supported arch to ppc64le

* Sat Aug 13 2016 Hon Ching(Vicky) Lo <lo1@us.ibm.com> - 713-2
- Minor spec fixes 

* Tue Aug 09 2016 Hon Ching(Vicky) Lo <lo1@us.ibm.com> - 713-1
- Updated for initial submission 

* Fri Mar 20 2015 George Wilson <gcwilson@us.ibm.com>
- Initial implementation
