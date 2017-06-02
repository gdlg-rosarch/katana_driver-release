Name:           ros-jade-katana-arm-gazebo
Version:        1.1.2
Release:        0%{?dist}
Summary:        ROS katana_arm_gazebo package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/katana_arm_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-controller-manager
Requires:       ros-jade-controller-manager-msgs
Requires:       ros-jade-gazebo-ros
Requires:       ros-jade-joint-trajectory-controller
Requires:       ros-jade-katana-description
Requires:       ros-jade-katana-gazebo-plugins
Requires:       ros-jade-robot-state-publisher
Requires:       ros-jade-roscpp
Requires:       ros-jade-std-msgs
Requires:       ros-jade-urdf
Requires:       ros-jade-xacro
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-controller-manager
BuildRequires:  ros-jade-controller-manager-msgs
BuildRequires:  ros-jade-gazebo-ros
BuildRequires:  ros-jade-joint-trajectory-controller
BuildRequires:  ros-jade-katana-description
BuildRequires:  ros-jade-katana-gazebo-plugins
BuildRequires:  ros-jade-robot-state-publisher
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-urdf
BuildRequires:  ros-jade-xacro

%description
This package starts a Neuronics Katana robot arm in the Gazebo simulation
environment. It is modeled after the pr2_arm_gazebo package by John Hsu.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Jun 02 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.1.2-0
- Autogenerated by Bloom

* Sat Feb 11 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.7-0
- Autogenerated by Bloom

* Sat Jan 28 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.6-0
- Autogenerated by Bloom

* Fri Jan 27 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.5-1
- Autogenerated by Bloom

* Tue Apr 12 2016 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.5-0
- Autogenerated by Bloom

* Mon Apr 11 2016 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.4-0
- Autogenerated by Bloom

