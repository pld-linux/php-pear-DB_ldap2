%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	DB_ldap2
Summary:	%{_pearname} - DB drivers for LDAP v2 and v3 database
Summary(pl.UTF-8):	%{_pearname} - sterowniki DB do bazy danych LDAP v2 i v3
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8724bce80d0de92ac72e296f1e8dfef7
URL:		http://pear.php.net/package/DB_ldap2/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-ldap
Requires:	php-pear
Requires:	php-pear-DB >= 1.7.0
Obsoletes:	php-pear-DB_ldap2-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_ldap2 and DB_ldap3 classes extend DB_common to provide DB compliant
access to LDAP servers with protocol version 2 and 3. The drivers
provide common DB interface as much as possible and support
prepare/execute statements.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasy DB_ldap2 i DB_ldap3 rozszerzają DB_common, aby umożliwić zgodny
z DB dostęp do serwerów LDAP przy użyciu protokołu w wersji 2 i 3.
Sterowniki dostarczają najbardziej ogólny jak to możliwe interfejs DB
oraz obsługują instrukcje prepare/execute.

Ta klasa ma w PEAR status: %{_status}.


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
%{php_pear_dir}/DB/*.php
