Name:           ros-indigo-katana
Version:        1.0.7
Release:        0%{?dist}
Summary:        ROS katana package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/katana
Source0:        %{name}-%{version}.tar.gz

Requires:       armadillo-devel
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-katana-msgs
Requires:       ros-indigo-kni
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-urdf
BuildRequires:  armadillo-devel
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-katana-msgs
BuildRequires:  ros-indigo-kni
BuildRequires:  ros-indigo-moveit-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-urdf

%description
This package provides ROS interfaces to the Neuronics Katana 450 arm. It wraps
the KNI library for low-level communication with the Katana arm.

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
* Sat Feb 11 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.7-0
- Autogenerated by Bloom

* Fri Jan 27 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.6-0
- Autogenerated by Bloom

* Tue Apr 12 2016 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.5-0
- Autogenerated by Bloom

* Mon Apr 11 2016 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.4-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.3-0
- Autogenerated by Bloom

* Wed May 06 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.2-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.1-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.0-0
- Autogenerated by Bloom

