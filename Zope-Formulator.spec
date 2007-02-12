
%define 	zope_subname	Formulator
Summary:	Zope framework that eases the creation and validation of web forms
Summary(pl.UTF-8):	Dodatek do Zope ułatwiający tworzenie i sprawdzanie poprawności formularzy WWW
Name:		Zope-%{zope_subname}
Version:	1.11.1
Release:	1
License:	BSD-like
Group:		Development/Tools
Source0:	http://www.infrae.com/download/%{zope_subname}/%{version}/%{zope_subname}-%{version}.tgz
# Source0-md5:	c50bc1997ed8a4509ffcf75b7d1a495e
URL:		http://www.infrae.com/products/formulator/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{zope_subname} is a tool to help with the creation and validation of
web forms. Form fields are stored as objects in Zope, in a special
Form folder.

%description -l pl.UTF-8
%{zope_subname} jest narzędziem pomagającym przy tworzeniu i
sprawdzaniu poprawności formularzy WWW. Pola formularza są zapisywane
jako obiekty w Zope, w specjalnym folderze Form.

%prep
%setup -q -n %{zope_subname}
mkdir docs
mv -f {CREDITS.txt,HISTORY.txt,INSTALL.txt,README.txt,TODO.txt} docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af {dtml,help,i18n,tests,www,*.py,*.html,refresh.txt,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc docs/*
%{_datadir}/%{name}
