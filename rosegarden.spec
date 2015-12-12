Summary:	Rosegarden - an attractive audio and MIDI sequencer
Summary(pl.UTF-8):	Rosegarden - interaktywny sekwencer MIDI i audio
Name:		rosegarden
Version:	15.10
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/rosegarden/%{name}-%{version}.tar.bz2
# Source0-md5:	6423f90ae392ff3673578ddc10020efd
Patch0:		%{name}-desktop.patch
URL:		http://www.rosegardenmusic.com/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	dssi-devel >= 1.0.0
BuildRequires:	fftw3-single-devel >= 3.0.0
BuildRequires:	gettext-tools
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	ladspa-devel
BuildRequires:	liblo-devel >= 0.7
BuildRequires:	liblrdf-devel >= 0.2
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	libsndfile-devel >= 1.0.16
BuildRequires:	lirc-devel
BuildRequires:	pkgconfig >= 0.15
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xorg-util-makedepend
BuildRequires:	zlib
Requires(post,postun):	shared-mime-info
Suggests:	libsndfile-progs
Suggests:	lilypond
Suggests:	perl-XML-Twig
Obsoletes:	rosegarden4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rosegarden is an attractive, user-friendly audio and MIDI sequencer,
score editor, and general-purpose music composition and editing
application.

%description -l pl.UTF-8
Rosegarden jest interaktywnym sekwencerem MIDI i audio, edytorem
zapisu nutowego, a jego głównym zadaniem jest komponowanie i edycja
muzyki.

%prep
%setup -q
%patch0 -p1

%build

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/rosegarden
%{_desktopdir}/rosegarden.desktop
%{_iconsdir}/[!l]*/*/*/*.png
%{_datadir}/mime/packages/*.xml
%{_datadir}/appdata/rosegarden.appdata.xml
