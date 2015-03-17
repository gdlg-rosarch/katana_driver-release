Name:           ros-hydro-katana-moveit-ikfast-plugin
Version:        1.0.1
Release:        0%{?dist}
Summary:        ROS katana_moveit_ikfast_plugin package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/katana_moveit_ikfast_plugin
Source0:        %{name}-%{version}.tar.gz

Requires:       lapack-devel
Requires:       ros-hydro-moveit-core
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-tf-conversions
BuildRequires:  lapack-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-moveit-core
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-tf-conversions

%description
The katana_moveit_ikfast_plugin package

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
* Tue Mar 17 2015 Martin Günther <mguenthe@uos.de> - 1.0.1-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Martin Günther <mguenthe@uos.de> - 1.0.0-0
- Autogenerated by Bloom

