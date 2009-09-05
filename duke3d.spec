%define		ver 	032696
%define		rel		0.1
Summary:	Duke Nukem 3D
Summary(pl.UTF-8):	Duke Nukem 3D
Name:		duke3d
Version:	1.5
Release:	0.%{ver}.%{rel}
License:	GPL
Group:		X11/Applications/Games
Source0:	%{name}.tar.bz2
# Source0-md5:	1fce8602af6e3dcdfd63307993643e75
Patch0:		%{name}-opt.patch
URL:		http://icculus.org/duke3d/
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL-devel
BuildRequires:	nasm
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Duke Nukem 3D.

You will need files from Atomic Edition to run this game.

%description -l pl.UTF-8
Duke Nukem 3D.

Aby uruchomić grę wymagane są pliki z Atomic Edition.

%prep
%setup -q -n %{name}
%patch0 -p1

ver=$(awk -F'"' '/DUKE NUKEM BUILD/{a=$(NF-1); sub(/.*: V/, "", a); print a}' source/astub.c)
if [ "$ver" != %{ver} ]; then
	exit 1
fi

%build
%{__make} -C source/buildengine \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags} -fno-omit-frame-pointer -funsigned-char"

%{__make} -C source \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags} -funsigned-char"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/duke3d}

install source/duke3d $RPM_BUILD_ROOT%{_bindir}
cp -a testdata/defs.con $RPM_BUILD_ROOT%{_datadir}/duke3d/DEFS.CON
cp -a testdata/game.con $RPM_BUILD_ROOT%{_datadir}/duke3d/GAME.CON
cp -a testdata/user.con $RPM_BUILD_ROOT%{_datadir}/duke3d/USER.CON
cp -a testdata/lookup.dat $RPM_BUILD_ROOT%{_datadir}/duke3d/LOOKUP.DAT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/duke3d
%{_datadir}/duke3d
