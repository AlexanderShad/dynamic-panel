%define exID dynamic-panel@velhlkj.com
%define nameU dynamic-panel

Name: gnome-shell-extension-dynamic-panel
Version: 3.0
Release: alt1

Summary: Dynamic top panel

BuildArch: noarch

License: Apache-2.0 license
Group:  Graphical desktop/GNOME
Url: https://github.com/velade/dynamic-panel.git

Source: %nameU-%version.tar

Requires: gnome-shell >= 46.0

%description
The design of the floating panel inspired by KDE Plasma6 presents a translucent floating bar effect when there is no window nearby, and a solid panel style when the window is close. Supports gnome's dark mode and light mode switching.

%prep
%setup -n %nameU-%version -c
%build
%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -R %_builddir/%nameU-%version/locale %buildroot%_datadir/gnome-shell/extensions/%exID/locale
cp -R %_builddir/%nameU-%version/schemas %buildroot%_datadir/gnome-shell/extensions/%exID/schemas
cp %_builddir/%nameU-%version/extension.js %buildroot%_datadir/gnome-shell/extensions/%exID/extension.js
cp %_builddir/%nameU-%version/LICENSE %buildroot%_datadir/gnome-shell/extensions/%exID/LICENSE
cp %_builddir/%nameU-%version/metadata.json %buildroot%_datadir/gnome-shell/extensions/%exID/metadata.json
cp %_builddir/%nameU-%version/prefs.js %buildroot%_datadir/gnome-shell/extensions/%exID/prefs.js

%files
%_datadir/gnome-shell/extensions/%exID/*
%doc *.md

%changelog
* Thu Sep 26 2024 Aleksander Shamaraev <shad@altlinux.ru> 3.0-alt1
- Initial build for Sisyphus

