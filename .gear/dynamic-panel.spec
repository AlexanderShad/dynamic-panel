%define exID dynamic-panel@velhlkj.com

Name: gnome-shell-extension-dynamic-panel
Version: 2.8
Release: alt1

Summary: Dynamic top panel

BuildArch: noarch

License: Apache-2.0 license
Group:  Graphical desktop/GNOME
Url: https://github.com/velade/dynamic-panel.git

Source: %name-%version.tar

Requires: gnome-shell >= 46.0

%description
The design of the floating panel inspired by KDE Plasma6 presents a translucent floating bar effect when there is no window nearby, and a solid panel style when the window is close. Supports gnome's dark mode and light mode switching.

%prep
%setup
%build
%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -R %_builddir/%name-%version/locale %buildroot%_datadir/gnome-shell/extensions/%exID/locale
cp -R %_builddir/%name-%version/schemas %buildroot%_datadir/gnome-shell/extensions/%exID/schemas
cp %_builddir/%name-%version/extension.js %buildroot%_datadir/gnome-shell/extensions/%exID/extension.js
cp %_builddir/%name-%version/LICENSE %buildroot%_datadir/gnome-shell/extensions/%exID/LICENSE
cp %_builddir/%name-%version/metadata.json %buildroot%_datadir/gnome-shell/extensions/%exID/metadata.json
cp %_builddir/%name-%version/prefs.js %buildroot%_datadir/gnome-shell/extensions/%exID/prefs.js
cp %_builddir/%name-%version/stylesheet.css %buildroot%_datadir/gnome-shell/extensions/%exID/stylesheet.css

%files
%_datadir/gnome-shell/extensions/%exID/*
%doc README.md

%changelog
* Sat Sep 21 2024 Aleksander Shamaraev <shad@altlinux.ru> 2.8-alt1
- Initial build for Sisyphus

