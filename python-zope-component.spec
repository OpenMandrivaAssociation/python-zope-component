%define	module	zope.component
%define name	python-zope-component
%define version 4.0.0
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary:	Zope Component Architecture
Name:	    %{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/z/%{module}/%{module}-%{version}.tar.gz
License:	ZPL
Group:		Development/Python
Url:		http://pypi.python.org/pypi/zope.component/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-zope-interface >= 3.8.0
Requires:	python-zope-event
BuildRequires:	python-setuptools

%description
This package represents the core of the Zope Component
Architecture. Together with the 'zope.interface' package, it provides
facilities for defining, registering and looking up components.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%py_sitedir/zope*


%changelog
* Mon Jul 02 2012 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 807787
- Update to 4.0.0.

* Wed Jun 20 2012 Lev Givon <lev@mandriva.org> 3.12.1-1
+ Revision: 806510
- imported package python-zope-component

