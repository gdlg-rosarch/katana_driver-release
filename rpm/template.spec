Name:           ros-hydro-katana-driver
Version:        1.0.3
Release:        0%{?dist}
Summary:        ROS katana_driver package

Group:          Development/Libraries
License:        BSD, GPL
URL:            http://ros.org/wiki/katana_driver
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-katana
Requires:       ros-hydro-katana-arm-gazebo
Requires:       ros-hydro-katana-description
Requires:       ros-hydro-katana-gazebo-plugins
Requires:       ros-hydro-katana-moveit-ikfast-plugin
Requires:       ros-hydro-katana-msgs
Requires:       ros-hydro-katana-teleop
Requires:       ros-hydro-katana-tutorials
Requires:       ros-hydro-kni
BuildRequires:  ros-hydro-catkin

%description
This stack contains all descriptions, drivers and bringup facilities for
Neuronics Katana 450 arm.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Jun 29 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.3-0
- Autogenerated by Bloom

* Wed May 06 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.2-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.1-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.0-0
- Autogenerated by Bloom

