# Script generated with Bloom
pkgdesc="ROS - This package contains test and demo programs for the katana_driver stack."
url='http://ros.org/wiki/katana_tutorials'

pkgname='ros-kinetic-katana-tutorials'
pkgver='1.1.2_1'
pkgrel=1
arch=('any')
license=('GPL'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-catkin'
'ros-kinetic-control-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-trajectory-msgs'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-control-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-trajectory-msgs'
)

conflicts=()
replaces=()

_dir=katana_tutorials
source=()
md5sums=()

prepare() {
    cp -R $startdir/katana_tutorials $srcdir/katana_tutorials
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

