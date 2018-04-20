# Script generated with Bloom
pkgdesc="ROS - This package provides ROS interfaces to the Neuronics Katana 450 arm. It wraps the <a href="/wiki/kni">KNI</a> library for low-level communication with the Katana arm."
url='http://ros.org/wiki/katana'

pkgname='ros-kinetic-katana'
pkgver='1.1.2_1'
pkgrel=1
arch=('any')
license=('GPL'
)

makedepends=('armadillo'
'ros-kinetic-actionlib'
'ros-kinetic-catkin'
'ros-kinetic-control-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-katana-msgs'
'ros-kinetic-kni'
'ros-kinetic-moveit-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
)

depends=('armadillo'
'ros-kinetic-actionlib'
'ros-kinetic-control-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-katana-msgs'
'ros-kinetic-kni'
'ros-kinetic-moveit-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-urdf'
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

