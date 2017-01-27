Name:           ros-indigo-katana-teleop
Version:        1.0.6
Release:        0%{?dist}
Summary:        ROS katana_teleop package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/katana_teleop
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-katana-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-katana-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
This package provides tele-operation nodes to control the Neuronics Katana 450
arm via keyboard commands or with a playstation 3 controller.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Jan 27 2017 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.6-0
- Autogenerated by Bloom

* Tue Apr 12 2016 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.5-0
- Autogenerated by Bloom

* Mon Apr 11 2016 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.4-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.3-0
- Autogenerated by Bloom

* Wed May 06 2015 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.2-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.1-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Henning Deeken <hdeeken@uni-osnabrueck.de> - 1.0.0-0
- Autogenerated by Bloom

