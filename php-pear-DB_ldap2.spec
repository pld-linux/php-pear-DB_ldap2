# ToDo:
# - pl summary/description
%include	/usr/lib/rpm/macros.php
%define         _class          DB
%define         _subclass       ldap2
%define		_pearname	%{_class}_%{_subclass}
%define		_status		devel
Summary:	%{_pearname} - DB drivers for LDAP v2 and v2 databse
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
# Source0-md5:	2892d7eff09cf547d208204c7c074547
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_ldap2 and DB_ldap3 classes extend DB_common to provide DB compliant
access to LDAP servers with protocol version 2 and 3. The drivers
provide common DB interface as much as possible and support
prepare/execute statements.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%doc %{_pearname}-%{version}/tests/*
%{php_pear_dir}/%{_class}/*.php
