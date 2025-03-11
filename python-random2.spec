#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 3 compatible Python 2.7 "random" Module
Summary(pl.UTF-8):	Moduł "random" z Pythona 2.7 zgodny z Pythonem 3
Name:		python-random2
Version:	1.0.1
Release:	3
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/random2/
Source0:	https://files.pythonhosted.org/packages/source/r/random2/random2-%{version}.zip
# Source0-md5:	48a0a86fe00e447212d0095de8cf3e21
URL:		https://pypi.org/project/random2/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Python 3 ported version of Python 2.7's random
module. It has also been back-ported to work in Python 2.6.

In Python 3, the implementation of randrange() was changed, so that
even with the same seed you get different sequences in Python 2 and 3.
Note that several high-level functions such as randint() and choice()
use randrange().

%description -l pl.UTF-8
Ten pakiet dostarcza wersję modułu random z Pythona 2.7 sportowaną do
Pythona 3, a także zbackportowaną, aby działała w Pythonie 2.6.

W Pythonie 3 implementacja randrange() została zmieniona, więc nawet z
tym samym zarodkiem otrzymamy inne sekwencje w Pythonie 2 i 3. Należy
zauważyć, że kilka funkcji wysokopoziomowych, takich jak randint() i
choice(), wykorzystuje randrange().

%package -n python3-random2
Summary:	Python 3 compatible Python 2.7 "random" Module
Summary(pl.UTF-8):	Moduł "random" z Pythona 2.7 zgodny z Pythonem 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-random2
This package provides a Python 3 ported version of Python 2.7's random
module. It has also been back-ported to work in Python 2.6.

In Python 3, the implementation of randrange() was changed, so that
even with the same seed you get different sequences in Python 2 and 3.
Note that several high-level functions such as randint() and choice()
use randrange().

%description -n python3-random2 -l pl.UTF-8
Ten pakiet dostarcza wersję modułu random z Pythona 2.7 sportowaną do
Pythona 3, a także zbackportowaną, aby działała w Pythonie 2.6.

W Pythonie 3 implementacja randrange() została zmieniona, więc nawet z
tym samym zarodkiem otrzymamy inne sekwencje w Pythonie 2 i 3. Należy
zauważyć, że kilka funkcji wysokopoziomowych, takich jak randint() i
choice(), wykorzystuje randrange().

%prep
%setup -q -n random2-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc CHANGES.txt README.txt
%{py_sitescriptdir}/random2.py[co]
%{py_sitescriptdir}/random2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-random2
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%{py3_sitescriptdir}/random2.py
%{py3_sitescriptdir}/__pycache__/random2.cpython-*.pyc
%{py3_sitescriptdir}/random2-%{version}-py*.egg-info
%endif
