Summary:	Duke Nukem 3D
Summary(pl):	Duke Nukem 3D
Name:		duke3d
Version:	1.5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	%{name}-20030909.tar.bz2
# Source0-md5:	c8e9660eb7be0df459079c8837212bf8
URL:		http://icculus.org/duke3d/
Patch0:		%{name}-opt.patch
ExclusiveArch:	%{ix86}
BuildRequires:	SDL_mixer-devel
BuildRequires:	nasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Duke Nukem 3D.
You will need files from Atomic Edition to run this game.

%description -l pl
Duke Nukem 3D.
Aby uruchomi� gr� wymagane s� pliki z Atomic Edition.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
cd source/buildengine
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -DUDP_NETWORKING=1 -DPLATFORM_UNIX -fno-omit-frame-pointer -funsigned-char"
cd ..
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -DUSE_SDL=1 -DPLATFORM_UNIX=1 -DUSE_EXECINFO=1 -funsigned-char -c"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/duke3d}

install source/duke3d $RPM_BUILD_ROOT%{_bindir}
install testdata/defs.con $RPM_BUILD_ROOT%{_datadir}/duke3d/DEFS.CON
install testdata/game.con $RPM_BUILD_ROOT%{_datadir}/duke3d/GAME.CON
install testdata/user.con $RPM_BUILD_ROOT%{_datadir}/duke3d/USER.CON
install testdata/lookup.dat $RPM_BUILD_ROOT%{_datadir}/duke3d/LOOKUP.DAT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/duke3d
