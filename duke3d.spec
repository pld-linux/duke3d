Summary:	Duke Nukem 3D
Summary(pl):	Duke Nukem 3D
Name:		duke3d
Version:	1.5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	%{name}-20030404.tar.bz2
URL:		http://icculus.org/duke3d/
ExclusiveArch:	%{ix86}
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Duke Nukem 3D.

You will need files from Atomic Edition to run this game.

%description -l pl
Duke Nukem 3D.

Aby uruchomiæ grê wymagane s± pliki z Atomic Edition.

%prep
%setup -q -n %{name}

%build
cd source/buildengine
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -DUSE_I386_ASM -DPLATFORM_UNIX -fasm -fno-omit-frame-pointer -funsigned-char"
cd ..
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -DUSE_SDL=1 -DPLATFORM_UNIX=1 -DUSE_I386_ASM=1"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install source/duke3d $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/*
