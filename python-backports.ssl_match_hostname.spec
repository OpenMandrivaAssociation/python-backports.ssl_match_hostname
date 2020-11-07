%define pkgname backports.ssl_match_hostname

Name:           python-%{pkgname}
Version:        3.7.0.1
Release:        1
Summary:        The ssl.match_hostname() function from Python 3.7
License:        PSF
URL:            https://pypi.org/project/backports.ssl_match_hostname/
Source0:        https://files.pythonhosted.org/packages/ff/2b/8265224812912bc5b7a607c44bf7b027554e1b9775e9ee0de8032e3de4b2/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python2-devel

%{?python_provide:%python_provide python-%{pkgname}}

%description
The ssl.match_hostname() function from Python 3.7
=================================================

The Secure Sockets Layer is only actually *secure*
if you check the hostname in the certificate returned
by the server to which you are connecting,
and verify that it matches to hostname
that you are trying to reach.

But the matching logic, defined in `RFC2818`_,
can be a bit tricky to implement on your own.
So the ``ssl`` package in the Standard Library of Python 3.2
and greater now includes a ``match_hostname()`` function
for performing this check instead of requiring every application
to implement the check separately.

This backport brings ``match_hostname()`` to users
of earlier versions of Python.
Simply make this distribution a dependency of your package,
and then use it like this::

%prep
%autosetup -n %{pkgname}-%{version}

%build
%{__python} setup.py build

pushd %{py2dir}
%{__python2} setup.py build
popd

%install

pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc  README.rst LICENSE
%{python_sitelib}/*/*

%files -n python2-%{pkgname}
%doc  README.rst LICENSE
%{python2_sitelib}/*/*
