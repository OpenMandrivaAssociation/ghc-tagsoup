%global debug_package %{nil}
%define module tagsoup

Summary:	Parsing and extracting information from (possibly malformed) HTML/XML documents
Name:		ghc-%{module}
Version:	0.12.8
Release:	3
License:	BSD
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(text)
Requires(post,preun):	ghc
Requires(pre):	haskell(text)

%description
TagSoup is a library for parsing HTML/XML. It supports the HTML 5
specification, and can be used to parse either well-formed XML, or unstructured
and malformed HTML from the web. The library also provides useful functions to
extract information from an HTML document, making it ideal for screen-scraping.

Users should start from the "Text.HTML.TagSoup" module.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

