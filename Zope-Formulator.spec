%include        /usr/lib/rpm/macros.python

%define 	zope_subname	Formulator

Summary:	Zope framework that eases the creation and validation of web forms
Summary(pl):	Dodatek do Zope u³atwiaj±cy tworzenie i sprawdzanie poprawno¶ci formularzy WWW
Name:		Zope-%{zope_subname}
Version:	1.5.0
Release:	2
License:	BSD-like
Group:		Development/Tools
Source0:	http://www.zope.org/Members/infrae/Formulator/Formulator-%{version}/%{zope_subname}-%{version}.tgz
# Source0-md5:	3a8dbedbc72f9176ca7fe5a54043e8d4
URL:		http://www.zope.org/Members/infrae/Formulator/
%pyrequires_eq  python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         product_dir     /usr/lib/zope/Products

%description
%{zope_subname} is a tool to help with the creation and validation of web
forms. Form fields are stored as objects in Zope, in a special Form folder.

%description -l pl
%{zope_subname} jest narzêdziem pomagaj±cym przy tworzeniu i sprawdzaniu
poprawno¶ci formularzy WWW. Pola formularza s± zapisywane jako obiekty
w Zope, w specjalnym folderze Form.

%prep
%setup -q -n %{zope_subname}

%build
mkdir docs
mv -f {CREDITS.txt,HISTORY.txt,INSTALL.txt,README.txt,TODO.txt} docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
        /etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
        /etc/rc.d/init.d/zope restart >&2
fi
		
%files
%defattr(644,root,root,755)
%doc docs/*
%{product_dir}/%{zope_subname}
