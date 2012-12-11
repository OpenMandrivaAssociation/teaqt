Summary:	A simple-in-use Qt based text editor
Name:		teaqt
Version:	33.3.0
Release:	1
Group:		Editors
License:	GPLv3+
URL:		http://tea-editor.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/tea-editor/tea-editor/%{version}/tea-%{version}.tar.bz2
Buildrequires:	qt4-devel
BuildRequires:	imagemagick aspell-devel

%description
Teaqt is a simple-in-use Qt-based text editor.

%prep
%setup -q -n tea-%{version}
find . -perm 0600 -exec chmod a+r {} \;

%build
%qmake_qt4 PREFIX=%{_bindir}
%make

%install
make install INSTALL_ROOT=%buildroot

mv %buildroot%_bindir/tea %buildroot%_bindir/%name

# icons
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
convert -resize 16x16 icons/tea_icon_v2.png %buildroot/%_miconsdir/%name.png
convert -resize 32x32 icons/tea_icon_v2.png %buildroot/%_iconsdir/%name.png
convert -resize 48x48 icons/tea_icon_v2.png %buildroot/%_liconsdir/%name.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=tea
Comment=A simple-in-use Qt-based text editor
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;TextEditor;Utility;
EOF

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%_datadir/applications/*


%changelog
* Wed Sep 05 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 33.3.0-1
+ Revision: 816394
- update to 33.3.0

* Mon Jul 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 33.2.0-1
+ Revision: 810642
- update to 33.2.0

* Mon May 28 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 33.1.0-1
+ Revision: 800892
- update to 33.1.0

* Wed May 02 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 33.0.0-1
+ Revision: 795125
- update to 33.0.0

* Mon Apr 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 32.0.2-1
+ Revision: 792906
- update to 32.0.1

* Wed Mar 14 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 32.0.1-1
+ Revision: 785007
- new version 32.0.1

* Sun Mar 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 32.0.0-1
+ Revision: 784119
- new version 32.0.0

* Fri May 20 2011 Funda Wang <fwang@mandriva.org> 29.0.3-1
+ Revision: 676388
- update to new version 29.0.3

* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 29.0.2-1
+ Revision: 652084
- update to new version 29.0.2

* Fri Apr 08 2011 Funda Wang <fwang@mandriva.org> 29.0.1-1
+ Revision: 651956
- update to new version 29.0.1

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 29.0.0-1
+ Revision: 649981
- update to new version 29.0.0

* Fri Dec 24 2010 Funda Wang <fwang@mandriva.org> 28.1.4-1mdv2011.0
+ Revision: 624579
- update to new version 28.1.4

* Fri Oct 15 2010 Funda Wang <fwang@mandriva.org> 28.1.3-1mdv2011.0
+ Revision: 585801
- update to new version 28.1.3

* Wed Sep 22 2010 Funda Wang <fwang@mandriva.org> 28.1.2-1mdv2011.0
+ Revision: 580555
- update to new version 28.1.2

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 28.1.1-1mdv2011.0
+ Revision: 563739
- update to new version 28.1.1

* Sun Jul 11 2010 Funda Wang <fwang@mandriva.org> 28.1.0-1mdv2011.0
+ Revision: 550991
- update to new version 28.1.0

* Sun Jul 11 2010 Funda Wang <fwang@mandriva.org> 28.0.0-1mdv2011.0
+ Revision: 550640
- update to new version 28.0.0

* Tue Apr 13 2010 Funda Wang <fwang@mandriva.org> 27.1.0-1mdv2010.1
+ Revision: 534500
- update to new version 27.1.0

* Thu Apr 01 2010 Funda Wang <fwang@mandriva.org> 27.0.2-1mdv2010.1
+ Revision: 530669
- update to new version 27.0.2

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 27.0.1-1mdv2010.1
+ Revision: 527058
- update to new version 27.0.1

* Fri Feb 26 2010 Funda Wang <fwang@mandriva.org> 27.0.0-1mdv2010.1
+ Revision: 511416
- update to new version 27.0.0

* Sat Jan 23 2010 Frederik Himpe <fhimpe@mandriva.org> 26.2.2-1mdv2010.1
+ Revision: 495276
- update to new version 26.2.2

* Thu Jan 07 2010 Frederik Himpe <fhimpe@mandriva.org> 26.2.1-1mdv2010.1
+ Revision: 487284
- update to new version 26.2.1

* Sat Dec 12 2009 Funda Wang <fwang@mandriva.org> 26.1.0-1mdv2010.1
+ Revision: 477743
- new version 26.1.0

* Sun Nov 08 2009 Frederik Himpe <fhimpe@mandriva.org> 26.0.1-1mdv2010.1
+ Revision: 462908
- update to new version 26.0.1

* Thu Oct 01 2009 Funda Wang <fwang@mandriva.org> 26.0.0-1mdv2010.0
+ Revision: 451926
- New version 26.0.0

* Tue Aug 11 2009 Frederik Himpe <fhimpe@mandriva.org> 25.1.0-1mdv2010.0
+ Revision: 415156
- update to new version 25.1.0

* Sat Jul 25 2009 Frederik Himpe <fhimpe@mandriva.org> 25.0.0-1mdv2010.0
+ Revision: 399876
- update to new version 25.0.0

* Tue Jun 02 2009 Funda Wang <fwang@mandriva.org> 24.0.0-1mdv2010.0
+ Revision: 382091
- New version 24.0.0

* Wed May 27 2009 Funda Wang <fwang@mandriva.org> 23.7.0-1mdv2010.0
+ Revision: 380177
- New version 23.7.0

* Tue May 26 2009 Funda Wang <fwang@mandriva.org> 23.6.0-1mdv2010.0
+ Revision: 379813
- New version 23.6.0

* Thu May 21 2009 Frederik Himpe <fhimpe@mandriva.org> 23.5.0-1mdv2010.0
+ Revision: 378398
- Update to new version 23.5.0
- Rediff prefix patch

* Wed Mar 04 2009 Funda Wang <fwang@mandriva.org> 23.1.1-1mdv2009.1
+ Revision: 348408
- New version 23.1.1

* Tue Feb 10 2009 Funda Wang <fwang@mandriva.org> 23.0.0-1mdv2009.1
+ Revision: 339064
- update to new version 23.0.0

* Wed Jan 21 2009 Funda Wang <fwang@mandriva.org> 22.3.0-1mdv2009.1
+ Revision: 332265
- update to new version 22.3.0

* Tue Jan 20 2009 Funda Wang <fwang@mandriva.org> 22.2.1-1mdv2009.1
+ Revision: 331515
- update to new version 22.2.1

* Sun Jan 18 2009 Funda Wang <fwang@mandriva.org> 22.2.0-1mdv2009.1
+ Revision: 330800
- 22.2.0

* Tue Jan 13 2009 Funda Wang <fwang@mandriva.org> 22.1.0-1mdv2009.1
+ Revision: 328880
- New version 22.1.0

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 22.0.1-1mdv2009.1
+ Revision: 323561
- new version 22.0.1

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 22.0.0-1mdv2009.1
+ Revision: 323307
- New version 22.0.0

* Sun Dec 21 2008 Funda Wang <fwang@mandriva.org> 21.1.3-1mdv2009.1
+ Revision: 317044
- new version 21.1.3

* Sat Dec 20 2008 Funda Wang <fwang@mandriva.org> 21.1.2-1mdv2009.1
+ Revision: 316502
- new version 21.1.2

* Thu Dec 18 2008 Funda Wang <fwang@mandriva.org> 21.1.1-1mdv2009.1
+ Revision: 315478
- new version 21.1.1

* Wed Dec 17 2008 Funda Wang <fwang@mandriva.org> 21.1.0-1mdv2009.1
+ Revision: 315058
- new version 21.1.0

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 21.0.5-1mdv2009.1
+ Revision: 312853
- new version 21.0.5

* Tue Dec 09 2008 Funda Wang <fwang@mandriva.org> 21.0.4-1mdv2009.1
+ Revision: 312120
- new version 21.0.4

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 21.0.3-1mdv2009.1
+ Revision: 308406
- update to new version 21.0.3

* Fri Nov 28 2008 Funda Wang <fwang@mandriva.org> 21.0.2-1mdv2009.1
+ Revision: 307343
- New version 21.0.2

* Thu Nov 20 2008 Funda Wang <fwang@mandriva.org> 21.0.0-1mdv2009.1
+ Revision: 304909
- new version 21.0.0

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 20.0.0-1mdv2009.1
+ Revision: 292800
- new version 20.0.0

* Sun Aug 31 2008 Funda Wang <fwang@mandriva.org> 19.1.0-1mdv2009.0
+ Revision: 278033
- update to new version 19.1.0

* Mon Aug 11 2008 Funda Wang <fwang@mandriva.org> 19.0.5-1mdv2009.0
+ Revision: 270630
- New version 19.0.5

* Sat Aug 09 2008 Funda Wang <fwang@mandriva.org> 19.0.2-1mdv2009.0
+ Revision: 270047
- update to new version 19.0.2

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 19.0.1-1mdv2009.0
+ Revision: 263755
- New version 19.0.1

* Sat Jul 12 2008 Funda Wang <fwang@mandriva.org> 18.0.1-1mdv2009.0
+ Revision: 234080
- New version 18.0.1

* Sat Jul 05 2008 Funda Wang <fwang@mandriva.org> 18.0.0-1mdv2009.0
+ Revision: 232010
- import teaqt


