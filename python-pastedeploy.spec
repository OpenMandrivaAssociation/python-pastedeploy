%define	tarname	PasteDeploy

Summary:	Load, configure, and compose WSGI applications and servers
Name:		python-pastedeploy
Version:	1.5.2
Release:	1
Source0:	http://pypi.python.org/packages/source/P/PasteDeploy/PasteDeploy-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pythonpaste.org/deploy/
BuildArch:	noarch
Requires:	python-paste
BuildRequires:	python-setuptools

%description
This tool provides code to load WSGI applications and servers from
URIs; these URIs can refer to Python Eggs for INI-style configuration
files.

%prep
%setup -q -n %{tarname}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc docs/*



%changelog
* Tue Nov 09 2010 Lev Givon <lev@mandriva.org> 1.3.4-1mdv2011.0
+ Revision: 595342
- import python-pastedeploy



