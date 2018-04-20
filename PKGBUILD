# Script generated with Bloom
pkgdesc="ROS - This package contains messages specific to the Neuronics Katana arm."
url='http://ros.org/wiki/katana_msgs'

pkgname='ros-kinetic-katana-msgs'
pkgver='1.1.2_1'
pkgrel=1
arch=('any')
license=('GPL'
)

makedepends=('ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-message-generation'
'ros-kinetic-sensor-msgs'
)

depends=('ros-kinetic-actionlib-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-sensor-msgs'
)

conflicts=()
replaces=()

_dir=katana_msgs
source=()
md5sums=()

prepare() {
    cp -R $startdir/katana_msgs $srcdir/katana_msgs
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

