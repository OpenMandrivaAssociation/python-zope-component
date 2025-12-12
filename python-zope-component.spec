%define	pypi_name	zope_component

Name:	    python-zope-component
Summary:	Zope Component Architecture
Version:	7.0
Release:	1
License:	ZPL-2.1
Group:		Development/Python
URL:		https://pypi.org/project/zope.component
Source0:	https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This package represents the core of the Zope Component
Architecture. Together with the 'zope.interface' package, it provides
facilities for defining, registering and looking up components.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

# Remove bundled egg-info
rm -rf src/zope.component.egg-info

%files
%doc README.rst
%license LICENSE.txt COPYRIGHT.txt
%{python_sitelib}/zope
%{python_sitelib}/%{pypi_name}-%{version}.dist-info


%changelog
* Mon Jul 02 2012 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 807787
- Update to 4.0.0.

* Wed Jun 20 2012 Lev Givon <lev@mandriva.org> 3.12.1-1
+ Revision: 806510
- imported package python-zope-component

