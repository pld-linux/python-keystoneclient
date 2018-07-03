#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Client Library for OpenStack Identity
Name:		python-keystoneclient
Version:	3.13.0
Release:	2
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/python-keystoneclient/%{name}-%{version}.tar.gz
# Source0-md5:	e9f5d8f1476be5fb835e074b79557c64
URL:		https://pypi.python.org/pypi/python-keystoneclient
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-debtcollector >= 1.2.0
Requires:	python-keystoneauth1 >= 3.0.1
Requires:	python-oslo.config >= 4.0.0
Requires:	python-oslo.i18n >= 2.1.0
Requires:	python-oslo.serialization >= 1.10.0
Requires:	python-oslo.utils >= 3.20.0
Requires:	python-pbr >= 2.0.0
Requires:	python-positional >= 1.1.1
Requires:	python-requests >= 2.14.2
Requires:	python-six >= 1.9.0
Requires:	python-stevedore >= 1.20.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a client for the OpenStack Identity API, implemented by the
Keystone team; it contains a Python API (the keystoneclient module)
for OpenStack's Identity Service.

%package -n python3-keystoneclient
Summary:	Client Library for OpenStack Identity
Group:		Libraries/Python
Requires:	python3-debtcollector >= 1.2.0
Requires:	python3-keystoneauth1 >= 3.0.1
Requires:	python3-oslo.config >= 4.0.0
Requires:	python3-oslo.i18n >= 2.1.0
Requires:	python3-oslo.serialization >= 1.10.0
Requires:	python3-oslo.utils >= 3.20.0
Requires:	python3-pbr >= 2.0.0
Requires:	python3-positional >= 1.1.1
Requires:	python3-requests >= 2.14.2
Requires:	python3-six >= 1.9.0
Requires:	python3-stevedore >= 1.20.0

%description -n python3-keystoneclient
This is a client for the OpenStack Identity API, implemented by the
Keystone team; it contains a Python API (the keystoneclient module)
for OpenStack's Identity Service.

%package apidocs
Summary:	API documentation for Python keystoneclient module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona keystoneclient
Group:		Documentation

%description apidocs
API documentation for Pythona keystoneclient module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona keystoneclient.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/keystoneclient
%{py_sitescriptdir}/python_keystoneclient-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-keystoneclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/keystoneclient
%{py3_sitescriptdir}/python_keystoneclient-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
