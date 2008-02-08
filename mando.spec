Name:		mando
Version:	1.6
Release:	%mkrel 1
Summary:	Interactive Camera-Projector System
Source:		http://vision.eng.shu.ac.uk/jan/%{name}-%{version}.tar.bz2
URL:		http://vision.eng.shu.ac.uk/mediawiki/index.php/Interactive_Camera-Projector_System
Group:		Office
License:	GPLv2+
BuildRequires:	qt4-devel boost-devel f2c fftw3-devel
BuildRequires:	dc1394-devel lapack-devel mesaglut-devel
BuildRequires:	ImageMagick libxtst-devel blas-devel

%description
A software for camera-projector interaction.
The software makes use of a low cost off-the shelf webcam that is calibrated
against a standard projector screen. The webcam is used to determine the
position of physical pointer (e.g. a pen) which is then used to virtually move
the X11 pointer. Point-and-click functionality has also been implemented.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -f %buildroot
%makeinstall_std

mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/mandriva-%name.desktop <<EOF
[Desktop Entry]
Name=Mando
Comment=Control the mouse pointer in a projector using a webcam
Exec=mando
Icon=mando
Type=Application
Terminal=false
Categories=Qt;Utility;Accessibility;
EOF

mkdir -p %buildroot{%_iconsdir,%_liconsdir,%_miconsdir}
convert -resize 48x48 mandologo.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 mandologo.png %buildroot%_iconsdir/%name.png
convert -resize 16x16 mandologo.png %buildroot%_miconsdir/%name.png

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc ChangeLog COPYING
%_bindir/%name
%_datadir/applications/*.desktop
%_iconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
