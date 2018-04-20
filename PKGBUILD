# Script generated with Bloom
pkgdesc="ROS - This package provides Gazebo plugins to simulate the Katana arm."
url='http://ros.org/wiki/katana_gazebo_plugins'

pkgname='ros-lunar-katana-gazebo-plugins'
pkgver='1.1.2_1'
pkgrel=1
arch=('any')
license=('GPL'
)

makedepends=('ros-lunar-actionlib'
'ros-lunar-catkin'
'ros-lunar-control-msgs'
'ros-lunar-control-toolbox'
'ros-lunar-gazebo-ros'
'ros-lunar-katana-msgs'
'ros-lunar-sensor-msgs'
'ros-lunar-trajectory-msgs'
)

depends=('ros-lunar-actionlib'
'ros-lunar-control-msgs'
'ros-lunar-control-toolbox'
'ros-lunar-gazebo-ros'
'ros-lunar-katana-msgs'
'ros-lunar-sensor-msgs'
'ros-lunar-trajectory-msgs'
)

conflicts=()
replaces=()

_dir=katana_gazebo_plugins
source=()
md5sums=()

prepare() {
    cp -R $startdir/katana_gazebo_plugins $srcdir/katana_gazebo_plugins
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

