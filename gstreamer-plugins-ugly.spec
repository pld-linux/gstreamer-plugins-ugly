#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	cdio		# cdio plugin
%bcond_without	sid		# sid plugin

%define		gstname		gst-plugins-ugly
%define		gstmver		1.0
%define		gst_ver		1.26.0
%define		gstpb_ver	1.26.0

Summary:	Ugly GStreamer Streaming-media framework plugins
Summary(pl.UTF-8):	Brzydkie wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-ugly
Version:	1.26.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://gstreamer.freedesktop.org/src/gst-plugins-ugly/%{gstname}-%{version}.tar.xz
# Source0-md5:	d6c8e12dd135a52f976c9de9c379f101
URL:		https://gstreamer.freedesktop.org/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.64.0
BuildRequires:	gstreamer-devel >= %{gst_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_ver}
%{?with_apidocs:BuildRequires:	hotdoc >= 0.11.0}
BuildRequires:	meson >= 1.4
BuildRequires:	ninja >= 1.5
BuildRequires:	orc-devel >= 0.4.41
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
##
## plugins
##
BuildRequires:	a52dec-libs-devel
%{?with_cdio:BuildRequires:	libcdio-devel >= 0.76}
BuildRequires:	libdvdread-devel >= 0.5.0
BuildRequires:	libmpeg2-devel >= 0.5.1
%{?with_sid:BuildRequires:	libsidplay-devel >= 1.36.57}
# ABI 156
BuildRequires:	libx264-devel >= 0.1.3-1.20190110_2245.1
Requires:	glib2 >= 1:2.64.0
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	orc >= 0.4.41
Obsoletes:	gstreamer-asf < 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir	%{_libdir}/gstreamer-%{gstmver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

%package apidocs
Summary:	Ugly GStreamer streaming-media framework plugins API documentation
Summary(pl.UTF-8):	Dokumentacja API brzydkich wtyczek środowiska obróbki strumieni GStreamer
Group:		Documentation
BuildArch:	noarch

%description apidocs
Ugly GStreamer streaming-media framework plugins API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API brzydkich wtyczek środowiska obróbki strumieni
GStreamer.

##
## Plugins
##

%package -n gstreamer-a52dec
Summary:	GStreamer VOB decoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera dekodująca VOB
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-a52dec
Plugin for decoding of VOB files.

%description -n gstreamer-a52dec -l pl.UTF-8
Wtyczka dekodująca pliki VOB.

%package -n gstreamer-cdio
Summary:	GStreamer plugin for CD audio input using libcdio
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca płyty CD-Audio przy użyciu libcdio
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libcdio >= 0.76
# for NLS
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-cdio
Plugin for playing audio tracks using libcdio under GStreamer.

%description -n gstreamer-cdio -l pl.UTF-8
Wtyczka do odtwarzania ścieżek dźwiękowych pod GStreamerem za pomocą
libcdio.

%package -n gstreamer-dvdread
Summary:	GStreamer plugin for DVD playback
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca DVD
Group:		Libraries
# for NLS
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libdvdread >= 0.5.0
Obsoletes:	gstreamer-libdvdread < 0.11

%description -n gstreamer-dvdread
GStreamer plugin for DVD playback.

%description -n gstreamer-dvdread -l pl.UTF-8
Wtyczka odtwarzająca DVD do GStreamera.

%package -n gstreamer-mpeg
Summary:	GStreamer plugins for MPEG video playback
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca obraz MPEG
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libmpeg2 >= 0.5.1

%description -n gstreamer-mpeg
Plugins for playing MPEG videos.

%description -n gstreamer-mpeg -l pl.UTF-8
Wtyczki do odtwarzania obrazu MPEG.

%package -n gstreamer-sid
Summary:	GStreamer Sid C64 music plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca muzykę Sid C64
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libsidplay >= 1.36.57

%description -n gstreamer-sid
Plugin for playback of C64 SID format music files.

%description -n gstreamer-sid -l pl.UTF-8
Wtyczka do odtwarzania plików z muzyką w formacie C64 SID.

%package -n gstreamer-x264
Summary:	GStreamer x264 encoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera kodująca przy użyciu biblioteki x264
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gst_ver}

%description -n gstreamer-x264
GStreamer x264 encoder plugin.

%description -n gstreamer-x264 -l pl.UTF-8
Wtyczka do GStreamera kodująca przy użyciu biblioteki x264.

%prep
%setup -q -n %{gstname}-%{version}

%build
%meson \
	--default-library=shared \
	-Da52dec=enabled \
	-Dasfdemux=enabled \
	-Ddvdlpcmdec=enabled \
	-Ddvdread=enabled \
	-Ddvdsub=enabled \
	-Dcdio=%{__enabled_disabled cdio} \
	-Ddoc=%{__enabled_disabled apidocs} \
	-Dglib_debug=disabled \
	-Dglib_assert=false \
	-Dglib_checks=false \
	-Dgpl=enabled \
	-Dmpeg2dec=enabled \
	-Dnls=enabled \
	-Dorc=enabled \
	-Drealmedia=enabled \
	-Dsidplay=%{__enabled_disabled sid} \
	-Dtests=disabled \
	-Dx264=enabled

%meson_build

%if %{with apidocs}
%meson_build build-hotdoc-configs

cd build/docs
for config in plugin-*.json ; do
	LC_ALL=C.UTF-8 hotdoc run --conf-file "$config"
done
%endif

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_docdir}/gstreamer-%{gstmver}
for d in build/docs/plugin-* ; do
	[ ! -d "$d" ] || cp -pr "$d" $RPM_BUILD_ROOT%{_docdir}/gstreamer-%{gstmver}
done
%endif

%find_lang %{gstname}-%{gstmver}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{gstname}-%{gstmver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md RELEASE
%attr(755,root,root) %{gstlibdir}/libgstasf.so
%attr(755,root,root) %{gstlibdir}/libgstdvdlpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstdvdsub.so
%attr(755,root,root) %{gstlibdir}/libgstrealmedia.so
%{_datadir}/gstreamer-%{gstmver}/presets

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_docdir}/gstreamer-%{gstmver}/plugin-a52dec
%{_docdir}/gstreamer-%{gstmver}/plugin-asf
%{_docdir}/gstreamer-%{gstmver}/plugin-cdio
%{_docdir}/gstreamer-%{gstmver}/plugin-dvdlpcmdec
%{_docdir}/gstreamer-%{gstmver}/plugin-dvdread
%{_docdir}/gstreamer-%{gstmver}/plugin-dvdsub
%{_docdir}/gstreamer-%{gstmver}/plugin-mpeg2dec
%{_docdir}/gstreamer-%{gstmver}/plugin-realmedia
%{_docdir}/gstreamer-%{gstmver}/plugin-sid
%{_docdir}/gstreamer-%{gstmver}/plugin-x264
%endif

##
## Plugins
##

%files -n gstreamer-a52dec
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsta52dec.so

%if %{with cdio}
%files -n gstreamer-cdio
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcdio.so
%endif

%files -n gstreamer-dvdread
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdvdread.so

%files -n gstreamer-mpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmpeg2dec.so

%if %{with sid}
%files -n gstreamer-sid
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsid.so
%endif

%files -n gstreamer-x264
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstx264.so
