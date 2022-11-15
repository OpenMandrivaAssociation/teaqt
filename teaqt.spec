%undefine _debugsource_packages

Summary:	A simple-in-use Qt based text editor
Name:		teaqt
Version:	62.0.2
Release:	1
Group:		Editors
License:	GPLv3+
URL:		http://tea.ourproject.org/
Source0:	https://github.com/psemiletov/tea-qt/archive/%{version}.tar.gz
BuildRequires:	qt5-devel
BuildRequires:	imagemagick aspell-devel
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	qmake5

%description
Teaqt is a simple-in-use Qt-based text editor.

%prep
%autosetup -p1 -n tea-qt-%{version}
find . -perm 0600 -exec chmod a+r {} \;

%build
%qmake_qt5 PREFIX=%{_bindir}
%make

%install
make install INSTALL_ROOT=%buildroot

# Fix syntax error in desktop file
sed -i -e 's, $,,g' %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root)
%{_bindir}/*
%_datadir/applications/*
%{_datadir}/icons/hicolor/*/apps/*.*
