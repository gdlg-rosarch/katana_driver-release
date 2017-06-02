Name:           ros-kinetic-katana-msgs
Version:        1.1.2
Release:        0%{?dist}
Summary:        ROS katana_msgs package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/katana_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-sensor-msgs

%description
This package contains messages specific to the Neuronics Katana arm.

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
* Fri Jun 02 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.1.2-0
- Autogenerated by Bloom

* Fri May 26 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.8-0
- Autogenerated by Bloom

* Sat Feb 11 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.7-0
- Autogenerated by Bloom

* Sat Jan 28 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.6-0
- Autogenerated by Bloom

