%define	tarname	PasteDeploy
%define name	python-pastedeploy
%define version 1.3.4
%define release %mkrel 1

Summary:	Load, configure, and compose WSGI applications and servers
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
Patch0:		exclude-tests.patch
License:	MIT
Group:		Development/Python
Url:		http://pythonpaste.org/deploy/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-paste
BuildRequires:	python-setuptools

%description
This tool provides code to load WSGI applications and servers from
URIs; these URIs can refer to Python Eggs for INI-style configuration
files.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p0

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc docs/*

