# Script generated with Bloom
pkgdesc="ROS - This package starts a Neuronics Katana robot arm in the Gazebo simulation environment. It is modeled after the <a href="http://www.ros.org/wiki/pr2_arm_gazebo">pr2_arm_gazebo</a> package by John Hsu."
url='http://ros.org/wiki/katana_arm_gazebo'

pkgname='ros-lunar-katana-arm-gazebo'
pkgver='1.1.2_1'
pkgrel=1
arch=('any')
license=('GPL'
)

makedepends=('ros-lunar-actionlib'
'ros-lunar-catkin'
'ros-lunar-controller-manager'
'ros-lunar-controller-manager-msgs'
'ros-lunar-gazebo-ros'
'ros-lunar-joint-trajectory-controller'
'ros-lunar-katana-description'
'ros-lunar-katana-gazebo-plugins'
'ros-lunar-robot-state-publisher'
'ros-lunar-roscpp'
'ros-lunar-std-msgs'
'ros-lunar-urdf'
'ros-lunar-xacro'
)

depends=('ros-lunar-actionlib'
'ros-lunar-controller-manager'
'ros-lunar-controller-manager-msgs'
'ros-lunar-gazebo-ros'
'ros-lunar-joint-trajectory-controller'
'ros-lunar-katana-description'
'ros-lunar-katana-gazebo-plugins'
'ros-lunar-robot-state-publisher'
'ros-lunar-roscpp'
'ros-lunar-std-msgs'
'ros-lunar-urdf'
'ros-lunar-xacro'
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

