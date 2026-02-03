%define	module	zope_component

Name:	    python-zope-component
Summary:	Zope Component Architecture
Version:	7.1
Release:	1
License:	ZPL-2.1
Group:		Development/Python
URL:		https://pypi.org/project/zope.component
Source0:	https://files.pythonhosted.org/packages/source/z/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This package represents the core of the Zope Component
Architecture. Together with the 'zope.interface' package, it provides
facilities for defining, registering and looking up components.

%prep -a
# Remove bundled egg-info
rm -rf src/zope.component.egg-info

%files
%doc README.rst
%license LICENSE.txt COPYRIGHT.txt
%{python_sitelib}/zope
%{python_sitelib}/%{module}-%{version}.dist-info
