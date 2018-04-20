# Script generated with Bloom
pkgdesc="ROS - This stack contains all descriptions, drivers and bringup facilities for Neuronics Katana 450 arm."
url='http://ros.org/wiki/katana_driver'

pkgname='ros-kinetic-katana-driver'
pkgver='1.1.2_1'
pkgrel=1
arch=('any')
license=('BSD, GPL'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-katana'
'ros-kinetic-katana-arm-gazebo'
'ros-kinetic-katana-description'
'ros-kinetic-katana-gazebo-plugins'
'ros-kinetic-katana-moveit-ikfast-plugin'
'ros-kinetic-katana-msgs'
'ros-kinetic-katana-teleop'
'ros-kinetic-katana-tutorials'
'ros-kinetic-kni'
)

conflicts=()
replaces=()

_dir=katana_driver
source=()
md5sums=()

prepare() {
    cp -R $startdir/katana_driver $srcdir/katana_driver
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

