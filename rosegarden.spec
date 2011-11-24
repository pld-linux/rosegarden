#
%define		_name		rosegarden
#
Summary:	Rosegarden - an attractive audio and MIDI sequencer
Summary(pl.UTF-8):	Rosegarden - interaktywny sekwencer MIDI i audio
Name:		rosegarden
Version:	11.11.11
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/rosegarden/%{_name}-%{version}.tar.bz2
# Source0-md5:	1e6529625b1e793288c3f1f8cdec955a
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-dssi_lib64.patch
URL:		http://www.rosegardenmusic.com/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	dssi-devel >= 1.0.0
BuildRequires:	fftw3-single-devel
BuildRequires:	gettext-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	ladspa-devel
BuildRequires:	liblo-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	liblrdf-devel
BuildRequires:	lirc-devel
BuildRequires:	pkgconfig >= 0.15
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	rpmbuild(macros) >= 1.129
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
Rosegarden jest interaktywnym sekwencerem MIDI i audio, edytorem zapisu
nutowego, a jego głównym zadaniem jest komponowanie i edycja muzyki.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%if "%{_lib}" == "lib64"
%patch1 -p1
%endif

%build

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

#%find_lang %{_name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

#%%files -f %{_name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/rosegarden
%{_desktopdir}/rosegarden.desktop
%{_iconsdir}/[!l]*/*/*/*.png
%{_datadir}/mime/packages/*.xml
