#
# Conditional build:
%bcond_with	arts	# enable aRts support (at cost of ALSA support)
%bcond_without	sound	# build without ANY sound support (only sequencer)
#
%define		_name		rosegarden

Summary:	Rosegarden - an attractive audio and MIDI sequencer
Summary(pl):	Rosegarden - interaktywny sekwencer MIDI i audio
Name:		rosegarden4
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/%{_name}/%{_name}-4-%{version}.tar.bz2
# Source0-md5:	ca63f343e2a6240a0f64d32e362bf436
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-qt.patch
URL:		http://www.rosegardenmusic.com/
%{?with_sound:BuildRequires:	alsa-lib-devel}
%{!?with_arts:BuildRequires:	alsa-lib-devel}
BuildRequires:	dssi >= 0.4
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	ladspa-devel
BuildRequires:	liblrdf-devel
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rosegarden is an attractive, user-friendly audio and MIDI sequencer,
score editor, and general-purpose music composition and editing
application.

%description -l pl
Rosegarden jest interaktywnym sekwencerem MIDI i audio, edytorem zapisu
nutowego, a jego g³ównym zadaniem jest komponowanie i edycja muzyki.

%prep
%setup -q -n %{_name}-4-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-rpath \
	%{!?with_sound:--disable-sound} \
	%{?with_arts:--with-arts}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/rosegarden.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{_name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO TRANSLATORS
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libRosegardenSequencer.la
%{_libdir}/libRosegardenSequencer.so
%attr(755,root,root) %{_libdir}/libRosegardenSequencer.so.*.*.*
%{_datadir}/apps/rosegarden
%{_desktopdir}/kde/rosegarden.desktop
%{_iconsdir}/[!l]*/*/apps/*rosegarden.png
%{_datadir}/mimelnk/audio/x-*.desktop
