Name:           ros-jade-katana-msgs
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS katana_msgs package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/katana_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib-msgs
Requires:       ros-jade-message-runtime
Requires:       ros-jade-sensor-msgs
BuildRequires:  ros-jade-actionlib-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-sensor-msgs

%description
This package contains messages specific to the Neuronics Katana arm.

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
* Tue Apr 12 2016 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.5-0
- Autogenerated by Bloom

* Mon Apr 11 2016 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.4-0
- Autogenerated by Bloom

