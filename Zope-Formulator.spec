
%define prod_name Formulator

Summary:	Zope framework that eases the creation and validation of web forms
Summary(pl):	Dodatek do Zope u�atwiaj�cy tworzenie i sprawdzanie poprawno�ci formularzy WWW
Name:		Zope-%{prod_name}
Version:	1.0.1
Release:	1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://www.zope.org/Members/faassen/Formulator/%{prod_name}-%{version}.tgz
# Source0-md5:	ee9d0f3b000f14f66962440fc2e638ae
URL:		http://www.zope.org/Members/faassen/Formulator/
Requires:	Zope
BuildRequires:	python >= 2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

%define zope_dir	   %{_libdir}/zope
%define zope_productsdir   %{zope_dir}/Products

%description
%{prod_name} is a tool to help with the creation and validation of web
forms. Form fields are stored as objects in Zope, in a special Form folder.

%description -l pl
%{prod_name} jest narz�dziem pomagaj�cym przy tworzeniu i sprawdzaniu
poprawno�ci formularzy WW. Pola formularza s� zapisywane jako obiekty
w Zope, w specjalnym folderze Form.

%prep
%setup -q -n %{prod_name}

%build
%{python_compile}
%{python_compile_opt}

find . -name \*.py | xargs -r rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}

cp -a . $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}
rm -f $RPM_BUILD_ROOT%{zope_productsdir}/%{prod_name}/*.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{zope_productsdir}/%{prod_name}
