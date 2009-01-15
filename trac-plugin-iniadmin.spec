%define		trac_ver	0.11
%define		plugin		iniadmin
Summary:	Edit all trac.ini options via the WebAdminPlugin
Name:		trac-plugin-%{plugin}
Version:	0.1
Release:	0.1
License:	BSD-like
Group:		Applications/WWW
# Source0Download: 
Source0:	%{plugin}plugin.zip
# Source0-md5:	a53e12a5746a80f79d4d0a45c65b71d9
URL:		http://trac-hacks.org/wiki/IniAdminPlugin
BuildRequires:	python-devel
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin uses the new configuration option API in Trac 0.10 to
allow modification of any field exposed through this mechanism.

This currently includes all core Trac settings, and although no
plugins are taking advantage of this yet, I'm sure it will only be a
matter of time :)

%prep
%setup -q -n %{plugin}plugin

%build
cd %{trac_ver}
%{__python} setup.py build
%{__python} setup.py egg_info

%install
rm -rf $RPM_BUILD_ROOT
cd %{trac_ver}
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
	%banner -e %{name} <<-'EOF'
	To enable the %{plugin} plugin, add to conf/trac.ini:

	[components]
	iniadmin.iniadmin.iniadminplugin = enabled
EOF
fi

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{plugin}
%{py_sitescriptdir}/*-*.egg-info
