Name:           intel-sgx-debugger
Summary:        Debugger for Intel SGX
Version:        0.0.20200227
Release:        1%{?dist}
License:        Apache-2.0

Source0: 	https://github.com/lkatalin/intel-sgx-debugger/blob/master/intel-sgx-sdk.tar

%{?systemd_requires}
BuildRequires:  systemd
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libmnl)

Provides:       %{name}-kmod-common = %{version}
Requires:       %{name}-kmod >= %{version}

%description
This contains the Intel SGX SDK with debugger.

%prep
%autosetup -n intel-sgx-%{version}
#%setup -q

# Remove .gitignore files in examples
find contrib/ -type f -name ".gitignore" -exec rm "{}" \;

%build
%set_build_flags
%make_build V=1 -C src/tools


%install
%make_install -C src/tools \
        WITH_BASHCOMPLETION=yes \
        WITH_SYSTEMDUNITS=yes


%files
%doc README.md
%license COPYING
%{_bindir}/intel-sgx-debugger
%{_sysconfdir}/intel-sgx-debugger


%changelog
* Thu Feb 27 2020 Lily Sturmann <lsturman@redhat.com> - 0.0.20200227
- Initial package
