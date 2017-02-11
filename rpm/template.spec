Name:           ros-jade-katana-teleop
Version:        1.0.7
Release:        0%{?dist}
Summary:        ROS katana_teleop package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/katana_teleop
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-control-msgs
Requires:       ros-jade-katana-msgs
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-control-msgs
BuildRequires:  ros-jade-katana-msgs
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs

%description
This package provides tele-operation nodes to control the Neuronics Katana 450
arm via keyboard commands or with a playstation 3 controller.

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
* Sat Feb 11 2017 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.7-0
- Autogenerated by Bloom

* Sat Jan 28 2017 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.6-0
- Autogenerated by Bloom

* Fri Jan 27 2017 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.5-1
- Autogenerated by Bloom

* Tue Apr 12 2016 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.5-0
- Autogenerated by Bloom

* Mon Apr 11 2016 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.4-0
- Autogenerated by Bloom

