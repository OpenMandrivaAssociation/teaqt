Summary:	A simple-in-use Qt based text editor
Name:		teaqt
Version:	27.0.1
Release:	%mkrel 1
Group:		Editors
License:	GPLv3+
URL:		http://tea-editor.sourceforge.net/
Source0:	http://downloads.sourceforge.net/tea-editor/tea-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
Buildrequires:	qt4-devel
BuildRequires:	imagemagick aspell-devel

%description
Teaqt is a simple-in-use Qt-based text editor.

%prep
%setup -q -n tea-%version

%build
%qmake_qt4 PREFIX=%{_bindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std INSTALL_ROOT=%buildroot

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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%_datadir/applications/*
