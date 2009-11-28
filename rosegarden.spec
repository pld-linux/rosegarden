# TODO:
#	- installed but unpackaged
#	   /usr/share/apps/profiles/rosegarden.profile.xml
#	   /usr/share/locale/en/LC_MESSAGES/rosegarden.mo
#
%define		_name		rosegarden
#
Summary:	Rosegarden - an attractive audio and MIDI sequencer
Summary(pl.UTF-8):	Rosegarden - interaktywny sekwencer MIDI i audio
Name:		rosegarden
Version:	1.7.3
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/rosegarden/%{_name}-%{version}.tar.bz2
# Source0-md5:	122eab42e375d2f3b009c8540ae8069c
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-link_order.patch
URL:		http://www.rosegardenmusic.com/
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	dssi >= 0.4
BuildRequires:	fftw3-single-devel
BuildRequires:	gettext-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	kde4-kde3support-devel >= 3.5.10-15
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	ladspa-devel
BuildRequires:	liblrdf-devel
BuildRequires:	lirc-devel
BuildRequires:	pkgconfig >= 0.15
BuildRequires:	rpmbuild(macros) >= 1.129
Suggests:	kde4-kdebase-kdialog
Suggests:	libsndfile-progs
Suggests:	lilypond
Suggests:	perl-XML-Twig
Obsoletes:	rosegarden4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_smp_mflags %{nil}

%description
Rosegarden is an attractive, user-friendly audio and MIDI sequencer,
score editor, and general-purpose music composition and editing
application.

%description -l pl.UTF-8
Rosegarden jest interaktywnym sekwencerem MIDI i audio, edytorem zapisu
nutowego, a jego głównym zadaniem jest komponowanie i edycja muzyki.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
export CMAKE_LIBRARY_PATH=/usr/lib/kde3dev
export CMAKE_INCLUDE_PATH=/usr/include/kde3
%cmake . \
	-DWANT_LIRC=YES
%{__make}
	
%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{_name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TRANSLATORS
%attr(755,root,root) %{_bindir}/rosegarden
%attr(755,root,root) %{_bindir}/rosegarden-audiofile-importer
%attr(755,root,root) %{_bindir}/rosegarden-lilypondview
%attr(755,root,root) %{_bindir}/rosegarden-project-package
%attr(755,root,root) %{_bindir}/rosegardensequencer
%{_datadir}/apps/rosegarden
%{_desktopdir}/kde/rosegarden.desktop
%{_iconsdir}/[!l]*/*/*/*.png
%{_datadir}/mimelnk/audio/x-*.desktop
