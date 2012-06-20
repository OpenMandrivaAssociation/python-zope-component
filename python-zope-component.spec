%define	module	zope.component
%define name	python-zope-component
%define version 3.12.1
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
Source0:	http://pypi.python.org/packages/source/z/%{module}/%{module}-%{version}.zip
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
