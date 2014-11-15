%define git 0a72d61

Name:           korora-icon-theme-base
Version:        0.2
Release:        1%{?dist}
Summary:        Base Icons for the Korora Project
License:        GPLv3
URL:            https://kororaproject.org/
Source0:        https://github.com/numixproject/numix-icon-theme/tarball/%{git}
Patch0:         0001-updated-udpated-theme-to-indicate-Korora-derivative.patch
Patch1:         0002-updated-icon-theme-name-change.patch
BuildArch:      noarch

%description
This is an icon theme based on the Numix project that has been adapated to the
Korora Project styling.

%prep
%setup -q -n numixproject-numix-icon-theme-%{git}
%patch0 -p1
%patch1 -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}/icons/korora-base
cp -apR Numix/* %{buildroot}%{_datadir}/icons/korora-base
chmod 644 %{buildroot}%{_datadir}/icons/korora-base/index.theme

%post
touch --no-create %{_datadir}/icons/korora-base &>/dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/korora-base &>/dev/null
  gtk-update-icon-cache -q %{_datadir}/icons/korora-base &>/dev/null ||:
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/korora-base &>/dev/null ||:

%files
%doc license
%{_datadir}/icons/korora-base/

%changelog
* Sat Nov 15 2014 Ian Firns <firnsy@kororaproject.org> - 0.2-1
- Updated to latest upstream.

* Sat Oct 04 2014 Ian Firns <firnsy@kororaproject.org> - 0.1-1
- Intial rpm build
