
%define prod_name Formulator

Summary:	Zope framework that eases the creation and validation of web forms. 
Name:		Zope-%{prod_name}
Version:	1.0.1
Release:	1
License:	BSD-style
Source0:	http://www.zope.org/Members/faassen/%{prod_name}/%{prod_name}-%{version}.tgz
URL:		http://www.zope.org/Members/faassen/%{prod_name}
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	Zope
BuildRequires:	python >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

%define zope_dir	   %{_libdir}/zope
%define zope_productsdir   %{zope_dir}/Products 	

%description
%{prod_name} is a tool to help with the creation and validation of web                            
forms. Form fields are stored as objects in Zope, in a special Form folder.

%prep
%setup -q -n %{prod_name}

%build
%{python_compile}
%{python_compile_opt}

find . -name \*.py | xargs -r rm -f
gzip -9nf *.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}

cp -a . $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}
rm -f $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}/*.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%{zope_productsdir}/%{prod_name}
