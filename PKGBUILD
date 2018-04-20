# Script generated with Bloom
pkgdesc="ROS - This package provides ROS interfaces to the Neuronics Katana 450 arm. It wraps the <a href="/wiki/kni">KNI</a> library for low-level communication with the Katana arm."
url='http://ros.org/wiki/katana'

pkgname='ros-lunar-katana'
pkgver='1.1.2_1'
pkgrel=1
arch=('any')
license=('GPL'
)

makedepends=('armadillo'
'ros-lunar-actionlib'
'ros-lunar-catkin'
'ros-lunar-control-msgs'
'ros-lunar-geometry-msgs'
'ros-lunar-katana-msgs'
'ros-lunar-kni'
'ros-lunar-moveit-msgs'
'ros-lunar-roscpp'
'ros-lunar-roslib'
'ros-lunar-sensor-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf'
'ros-lunar-trajectory-msgs'
'ros-lunar-urdf'
)

depends=('armadillo'
'ros-lunar-actionlib'
'ros-lunar-control-msgs'
'ros-lunar-geometry-msgs'
'ros-lunar-katana-msgs'
'ros-lunar-kni'
'ros-lunar-moveit-msgs'
'ros-lunar-roscpp'
'ros-lunar-roslib'
'ros-lunar-sensor-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf'
'ros-lunar-trajectory-msgs'
'ros-lunar-urdf'
)

conflicts=()
replaces=()

_dir=katana
source=()
md5sums=()

prepare() {
    cp -R $startdir/katana $srcdir/katana
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

