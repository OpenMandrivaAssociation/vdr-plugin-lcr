
%define plugin	lcr
%define name	vdr-plugin-%plugin
%define version	0.0.8
%define rel	15

Summary:	VDR plugin: Displays telephone rates on OSD
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://lcr.vdr-developer.org/
Source:		http://lcr.vdr-developer.org/downloads/vdr-%plugin-%version.tar.bz2
Patch0:		lcr-91_vdr-1.5.15.dpatch
Patch1:		lcr-0.0.8-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Least Cost Routing is a plugin that displays information about the lowest
rates for telephoning AT THE MOMENT on the osd. It retrieves its data from
"www.teltarif.de" and displays them in a table on the osd.
For the retrieval an additional (perl) script is needed (retrieve-data.pl).

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep
chmod 0644 README*

%vdr_plugin_params_begin %plugin
# alternative data retrieval script
var=SCRIPT
param=--script=SCRIPT
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_bindir}
install -m755 contrib/*.pl %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY CONTRIBUTORS skins
%{_bindir}/vdr-lcr-retrieve_data.pl
