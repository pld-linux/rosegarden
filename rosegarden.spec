#
# Conditional build:
%bcond_with	qt4	# Qt 4 instead of Qt 5
#
Summary:	Rosegarden - an attractive audio and MIDI sequencer
Summary(pl.UTF-8):	Rosegarden - interaktywny sekwencer MIDI i audio
Name:		rosegarden
Version:	16.06
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/rosegarden/%{name}-%{version}.tar.bz2
# Source0-md5:	a8679dcd852a78eee064d8a4a4f4a961
Patch0:		%{name}-desktop.patch
URL:		http://www.rosegardenmusic.com/
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4.8.0
BuildRequires:	QtGui-devel >= 4.8.0
BuildRequires:	QtNetwork-devel >= 4.8.0
BuildRequires:	QtTest-devel >= 4.8.0
BuildRequires:	QtXml-devel >= 4.8.0
%else
BuildRequires:	Qt5Core-devel >= 5.1.0
BuildRequires:	Qt5Network-devel >= 5.1.0
BuildRequires:	Qt5PrintSupport-devel >= 5.1.0
BuildRequires:	Qt5Test-devel >= 5.1.0
BuildRequires:	Qt5Xml-devel >= 5.1.0
BuildRequires:	Qt5Widgets-devel >= 5.1.0
%endif
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	dssi-devel >= 1.0.0
BuildRequires:	fftw3-single-devel >= 3.0.0
BuildRequires:	gettext-tools
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	ladspa-devel
BuildRequires:	liblo-devel >= 0.7
BuildRequires:	liblrdf-devel >= 0.2
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	libsndfile-devel >= 1.0.16
BuildRequires:	libstdc++-devel
BuildRequires:	lirc-devel
BuildRequires:	pkgconfig >= 1:0.15
%if %{with qt4}
BuildRequires:	qt4-build >= 4.8.0
BuildRequires:	qt4-linguist >= 4.8.0
%else
BuildRequires:	qt5-build >= 5.1.0
BuildRequires:	qt5-linguist >= 5.1.0
%endif
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-makedepend
BuildRequires:	zlib-devel
Requires(post,postun):	shared-mime-info
%if %{with qt4}
Requires:	QtCore >= 4.8.0
Requires:	QtGui >= 4.8.0
Requires:	QtNetwork >= 4.8.0
Requires:	QtXml >= 4.8.0
%else
Requires:	Qt5Core >= 5.1.0
Requires:	Qt5Network >= 5.1.0
Requires:	Qt5PrintSupport >= 5.1.0
Requires:	Qt5Xml >= 5.1.0
Requires:	Qt5Widgets >= 5.1.0
%endif
Requires:	liblo >= 0.7
Requires:	liblrdf >= 0.2
Requires:	libsamplerate >= 0.1.2
Requires:	libsndfile >= 1.0.16
Suggests:	libsndfile-progs >= 1.0.16
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
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_iconsdir}/hicolor/*x*/apps/rosegarden.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-rosegarden-*.png
%{_datadir}/appdata/rosegarden.appdata.xml
%{_datadir}/mime/packages/rosegarden.xml
