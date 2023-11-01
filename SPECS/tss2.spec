#
# Spec file for IBM's TSS for the TPM 2.0
#
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}

%global incname ibmtss

Name:		tss2
Version:	1.6.0
Release:	1%{?dist}
Epoch:	        1
Summary:	IBM's TCG Software Stack (TSS) for TPM 2.0 and related utilities

License:	BSD
URL:		http://sourceforge.net/projects/ibmtpm20tss/
Source0:	https://sourceforge.net/projects/ibmtpm20tss/files/ibmtss%{version}.tar.gz
Patch0:         tss2-1.6.0-manpage-cleanup.patch

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires:  gcc
BuildRequires:	openssl-devel
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
%autosetup -p1 -c %{name}-%{version}

%build
autoreconf -vi
%configure --disable-static --disable-tpm-1.2 --program-prefix=tss
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
* Tue May 18 2021 Jerry Snitselaar <jsnitsel@redhat.com> - 1.6.0-1
- Rebase to v1.6.0 release.
- Manpage cleanup.
resolves: rhbz#1822073

* Thu Jun 06 2019 Jerry Snitselaar <jsnitsel@redhat.com> - 1331-2
- Fix bounds check in IMA_Event_PcrExtend
resolves: rhbz#1669239

* Thu May 30 2019 Jerry Snitselaar <jsnitsel@redhat.com> - 1331-1
- Rebase to v1331
- Add initial CI gating support
resolves: rhbz#1669239

* Fri Oct 05 2018 Jerry Snitselaar <jsnitsel@redhat.com> - 1234-5
- Move header files to ibmtss directory.
- Check return value of TSS_Hash_Generate.
resolves: rhbz#1636245

* Tue Oct 02 2018 Jerry Snitselaar <jsnitsel@redhat.com> - 1234-4
- Fix compile and link flags
resolves: rhbz#1624182

* Thu Jul 19 2018 Jerry Snitselaar <jsnitsel@redhat.com> - 1234-3
- Clean up covscan issues.

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
