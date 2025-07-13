#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Python 3 compatible Python 2.7 "random" Module
Summary(pl.UTF-8):	Moduł "random" z Pythona 2.7 zgodny z Pythonem 3
Name:		python3-random2
Version:	1.0.2
Release:	1
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/random2/
Source0:	https://files.pythonhosted.org/packages/source/r/random2/random2-%{version}.tar.gz
# Source0-md5:	cde24fb34f34e506818fad62faeb4a7c
URL:		https://pypi.org/project/random2/
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Python 3 ported version of Python 2.7's random
module.

In Python 3, the implementation of randrange() was changed, so that
even with the same seed you get different sequences in Python 2 and 3.
Note that several high-level functions such as randint() and choice()
use randrange().

%description -l pl.UTF-8
Ten pakiet dostarcza wersję modułu random z Pythona 2.7 sportowaną do
Pythona 3.

W Pythonie 3 implementacja randrange() została zmieniona, więc nawet z
tym samym zarodkiem otrzymamy inne sekwencje w Pythonie 2 i 3. Należy
zauważyć, że kilka funkcji wysokopoziomowych, takich jak randint() i
choice(), wykorzystuje randrange().

%prep
%setup -q -n random2-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} src/tests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py3_sitescriptdir}/random2.py
%{py3_sitescriptdir}/__pycache__/random2.cpython-*.pyc
%{py3_sitescriptdir}/random2-%{version}-py*.egg-info
