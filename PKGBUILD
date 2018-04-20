# Script generated with Bloom
pkgdesc="ROS - This package starts a Neuronics Katana robot arm in the Gazebo simulation environment. It is modeled after the <a href="http://www.ros.org/wiki/pr2_arm_gazebo">pr2_arm_gazebo</a> package by John Hsu."
url='http://ros.org/wiki/katana_arm_gazebo'

pkgname='ros-kinetic-katana-arm-gazebo'
pkgver='1.1.2_1'
pkgrel=1
arch=('any')
license=('GPL'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-catkin'
'ros-kinetic-controller-manager'
'ros-kinetic-controller-manager-msgs'
'ros-kinetic-gazebo-ros'
'ros-kinetic-joint-trajectory-controller'
'ros-kinetic-katana-description'
'ros-kinetic-katana-gazebo-plugins'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-urdf'
'ros-kinetic-xacro'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-controller-manager'
'ros-kinetic-controller-manager-msgs'
'ros-kinetic-gazebo-ros'
'ros-kinetic-joint-trajectory-controller'
'ros-kinetic-katana-description'
'ros-kinetic-katana-gazebo-plugins'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
'ros-kinetic-urdf'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=katana_arm_gazebo
source=()
md5sums=()

prepare() {
    cp -R $startdir/katana_arm_gazebo $srcdir/katana_arm_gazebo
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

