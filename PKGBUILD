# Maintainer: Philip Müller <philm[at]manjaro[dog]org>

pkgname=tcalamares
_pkgname=calamares
pkgver=3.2.39.3
pkgrel=2
pkgdesc='Distribution-independent installer framework'
arch=('i686' 'x86_64')
license=(GPL)
url="https://github.com/calamares/calamares/releases/download"
license=('LGPL')
depends=('kconfig' 'kcoreaddons' 'kiconthemes' 'ki18n' 'kio' 'solid' 'yaml-cpp' 'kpmcore' 'mkinitcpio-openswap'
         'boost-libs' 'ckbcomp' 'hwinfo' 'qt5-svg' 'polkit-qt5' 'gtk-update-icon-cache' 'plasma-framework'
         'qt5-xmlpatterns' 'squashfs-tools' 'libpwquality') # 'pythonqt>=3.2')
makedepends=('extra-cmake-modules' 'qt5-tools' 'qt5-translations' 'git' 'boost')
backup=('usr/share/calamares/modules/bootloader.conf'
        'usr/share/calamares/modules/displaymanager.conf'
        'usr/share/calamares/modules/initcpio.conf'
        'usr/share/calamares/modules/unpackfs.conf')

source=("$_pkgname-$pkgver-$pkgrel.tar.gz::$url/v$pkgver/calamares-$pkgver.tar.gz")
sha256sums=('7e4a10564ca17690534e4661db50799df82a3b3739c619fabbf25c1dd449a0be')

prepare() {
	cd ${srcdir}/calamares-${pkgver}
	sed -i -e 's/"Install configuration files" OFF/"Install configuration files" ON/' CMakeLists.txt

	# patches here

	# change version
	_ver="$(cat CMakeLists.txt | grep -m3 -e "  VERSION" | grep -o "[[:digit:]]*" | xargs | sed s'/ /./g')"
	printf 'Version: %s-%s' "${_ver}" "${pkgrel}"
	sed -i -e "s|\${CALAMARES_VERSION_MAJOR}.\${CALAMARES_VERSION_MINOR}.\${CALAMARES_VERSION_PATCH}|${_ver}-${pkgrel}|g" CMakeLists.txt
	sed -i -e "s|CALAMARES_VERSION_RC 1|CALAMARES_VERSION_RC 0|g" CMakeLists.txt

}

build() {
	cd ${srcdir}/calamares-${pkgver}

	mkdir -p build
	cd build
        cmake .. \
              -DCMAKE_BUILD_TYPE=Release \
              -DCMAKE_INSTALL_PREFIX=/usr \
              -DCMAKE_INSTALL_LIBDIR=lib \
              -DWITH_PYTHONQT:BOOL=ON \
              -DBoost_NO_BOOST_CMAKE=ON \
              -DSKIP_MODULES="tracking webview interactiveterminal initramfs \
                              initramfscfg dracut dracutlukscfg \
                              dummyprocess dummypython dummycpp \
                              dummypythonqt services-openrc"
        make
}

package() {
	cd ${srcdir}/calamares-${pkgver}/build
	make DESTDIR="$pkgdir" install
	#install -Dm644 "../data/manjaro-icon.svg" "$pkgdir/usr/share/icons/hicolor/scalable/apps/calamares.svg"
	#install -Dm644 "../data/calamares.desktop" "$pkgdir/usr/share/applications/calamares.desktop"
	#install -Dm755 "../data/calamares_polkit" "$pkgdir/usr/bin/calamares_polkit"
	#install -Dm644 "../data/49-nopasswd-calamares.rules" "$pkgdir/etc/polkit-1/rules.d/49-nopasswd-calamares.rules"
	#chmod 750      "$pkgdir"/etc/polkit-1/rules.d

	# rename services-systemd back to services
	#mv "$pkgdir/usr/lib/calamares/modules/services-systemd" "$pkgdir/usr/lib/calamares/modules/services"
	#mv "$pkgdir/usr/share/calamares/modules/services-systemd.conf" "$pkgdir/usr/share/calamares/modules/services.conf"
	#sed -i -e 's/-systemd//' "$pkgdir/usr/lib/calamares/modules/services/module.desc"
	#sed -i -e 's/-systemd//' "$pkgdir/usr/share/calamares/settings.conf"
}
