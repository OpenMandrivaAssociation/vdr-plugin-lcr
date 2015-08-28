%define plugin	lcr

Summary:	VDR plugin: Displays telephone rates on OSD
Name:		vdr-plugin-%plugin
Version:	0.0.9
Release:	5
Group:		Video
License:	GPL
URL:		http://lcr.vdr-developer.org/
Source:		http://lcr.vdr-developer.org/downloads/vdr-%plugin-%version.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Least Cost Routing is a plugin that displays information about the lowest
rates for telephoning AT THE MOMENT on the osd. It retrieves its data from
"www.teltarif.de" and displays them in a table on the osd.
For the retrieval an additional (perl) script is needed (retrieve-data.pl).

%prep
%setup -q -n %plugin-%version
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
%vdr_plugin_install

install -d -m755 %{buildroot}%{_bindir}
install -m755 contrib/*.pl %{buildroot}%{_bindir}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY CONTRIBUTORS skins
%{_bindir}/vdr-lcr-retrieve_data.pl


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.9-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 0.0.9-1mdv2010.0
+ Revision: 396129
- new version
- drop patches, fixed upstream

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.8-15mdv2009.1
+ Revision: 359331
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.8-14mdv2009.0
+ Revision: 197943
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.8-13mdv2009.0
+ Revision: 197685
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of VDR 1.5.15 (P0 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.8-12mdv2008.1
+ Revision: 145108
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.8-11mdv2008.1
+ Revision: 103148
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.8-10mdv2008.0
+ Revision: 50013
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.8-9mdv2008.0
+ Revision: 42099
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.8-8mdv2008.0
+ Revision: 22745
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.8-7mdv2007.0
+ Revision: 90937
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.8-6mdv2007.1
+ Revision: 74035
- rebuild for new vdr
- Import vdr-plugin-lcr

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.8-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.8-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.8-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.8-2mdv2007.0
- rebuild for new vdr

* Fri Jul 14 2006 Anssi Hannula <anssi@mandriva.org> 0.0.8-1mdv2007.0
- initial Mandriva release

