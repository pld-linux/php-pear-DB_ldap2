%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	ldap2
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - DB drivers for LDAP v2 and v3 database
Summary(pl):	%{_pearname} - sterowniki DB do bazy danych LDAP v2 i v3
Name:		php-pear-%{_pearname}
Version:	0.4
Release:	2.2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	33e89636936d7b9151e30811a24c04ca
URL:		http://pear.php.net/package/DB_ldap2/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-ldap
Requires:	php-pear
Requires:	php-pear-DB
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_ldap2 and DB_ldap3 classes extend DB_common to provide DB compliant
access to LDAP servers with protocol version 2 and 3. The drivers
provide common DB interface as much as possible and support
prepare/execute statements.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasy DB_ldap2 i DB_ldap3 rozszerzaj± DB_common, aby umo¿liwiæ zgodny
z DB dostêp do serwerów LDAP przy u¿yciu protoko³u w wersji 2 i 3.
Sterowniki dostarczaj± najbardziej ogólny jak to mo¿liwe interfejs DB
oraz obs³uguj± instrukcje prepare/execute.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
