#
# Conditional build:
# _with_arts			- enable aRts support (at cost of ALSA support)
# _without_kdemultimedia	- without linking with arts
#
%define		_name		rosegarden
%define         _htmldir        /usr/share/doc/kde/HTML
Summary:	Rosegarden - an attractive audio and MIDI sequencer
Summary(pl):	Rosegarden - interaktywny sekwencer MIDI i audio
Name:		rosegarden4
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/%{_name}/%{_name}-4-%{version}.tar.gz
# Source0-md5:	f8b3c44da48b125be8a7459664bfa4cb
Patch0:		%{_name}-desktop.patch
URL:		http://www.all-day-breakfast.com/rosegarden/
BuildRequires:	alsa-lib-devel
%{!?_without_kdemultimedia:BuildRequires:	arts-kde-devel}
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
%{!?_without_kdemultimedia:BuildRequires: kdemultimedia-devel >= 3.0}
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
	%{!?_with_arts:--with-alsa} \
	%{?_with_arts:--with-arts}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
