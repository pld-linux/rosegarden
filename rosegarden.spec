#
# Conditional build:
%bcond_with arts		# enable aRts support (at cost of ALSA support)
%bcond_without sound		# build without ANY sound support (only sequencer)
#
%define		_name		rosegarden
%define         _htmldir        /usr/share/doc/kde/HTML
Summary:	Rosegarden - an attractive audio and MIDI sequencer
Summary(pl):	Rosegarden - interaktywny sekwencer MIDI i audio
Name:		rosegarden4
Version:	0.9.5
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/%{_name}/%{_name}-4-%{version}.tar.gz
# Source0-md5:	49bd200dda08de37a2e13a12c1456acf
Patch0:		%{_name}-desktop.patch
URL:		http://www.all-day-breakfast.com/rosegarden/
%{?with_sound:BuildRequires:	alsa-lib-devel}
BuildRequires:	jack-audio-connection-kit-devel >= 0.80.0
BuildRequires:	ladspa-devel
BuildRequires:	liblrdf-devel
BuildRequires:	kdelibs-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
Rosegarden is an attractive, user-friendly audio and MIDI sequencer,
score editor, and general-purpose music composition and editing
application.

%description -l pl
Rosegarden jest interaktywnym sewencerem MIDI i audio, edytorem zapisu
nutowego, a jego g³ównym zadaniem jest komponowanie i edycja muzyki.

%prep
%setup -q -n %{_name}-4-%{version}
%patch0 -p1

%build
kde_icondir="%{_pixmapsdir}"; export kde_icondir
kde_htmldir="%{_htmldir}"; export kde_htmldir
%configure \
	%{?with_arts:--with-arts} \
	%{!?with_sound:--disable-sound}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{_name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libRosegardenSequencer.so.*.*
%{_datadir}/apps/%{_name}
%{_pixmapsdir}/*/*/apps/%{_name}.xpm
%{_desktopdir}/%{_name}.desktop
# devel? but no headers
%attr(755,root,root) %{_libdir}/libRosegardenSequencer.so
%{_libdir}/libRosegardenSequencer.la
