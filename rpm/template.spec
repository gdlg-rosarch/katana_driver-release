Name:           ros-kinetic-katana-arm-gazebo
Version:        1.0.8
Release:        0%{?dist}
Summary:        ROS katana_arm_gazebo package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/katana_arm_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-controller-manager-msgs
Requires:       ros-kinetic-gazebo-ros
Requires:       ros-kinetic-joint-trajectory-controller
Requires:       ros-kinetic-katana-description
Requires:       ros-kinetic-katana-gazebo-plugins
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-urdf
Requires:       ros-kinetic-xacro
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-manager
BuildRequires:  ros-kinetic-controller-manager-msgs
BuildRequires:  ros-kinetic-gazebo-ros
BuildRequires:  ros-kinetic-joint-trajectory-controller
BuildRequires:  ros-kinetic-katana-description
BuildRequires:  ros-kinetic-katana-gazebo-plugins
BuildRequires:  ros-kinetic-robot-state-publisher
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-urdf
BuildRequires:  ros-kinetic-xacro

%description
This package starts a Neuronics Katana robot arm in the Gazebo simulation
environment. It is modeled after the pr2_arm_gazebo package by John Hsu.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri May 26 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.8-0
- Autogenerated by Bloom

* Sat Feb 11 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.7-0
- Autogenerated by Bloom

* Sat Jan 28 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.6-0
- Autogenerated by Bloom

