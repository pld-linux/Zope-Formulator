
%include        /usr/lib/rpm/macros.python
%define 	zope_subname	Formulator
Summary:	Zope framework that eases the creation and validation of web forms
Summary(pl):	Dodatek do Zope u³atwiaj±cy tworzenie i sprawdzanie poprawno¶ci formularzy WWW
Name:		Zope-%{zope_subname}
Version:	1.6.2
Release:	1
License:	BSD-like
Group:		Development/Tools
Source0:	http://www.zope.org/Members/infrae/Formulator/Formulator-%{version}/%{zope_subname}-%{version}.tgz
# Source0-md5:	c5eb395918349036c7ac400dbbff98e9
URL:		http://www.zope.org/Members/infrae/Formulator/
%pyrequires_eq  python-modules
Requires:	Zope
Requires(post,postun):  /usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af {dtml,help,tests,www,*.py,*.html,refresh.txt,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname} 
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc docs/*
%{_datadir}/%{name}
