Name:		texlive-cluttex
Version:	60964
Release:	1
Summary:	An automation tool for running LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cluttex
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cluttex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cluttex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is another tool for the automation of LaTeX document
processing, like latexmk or arara. The main feature of this
tool is that it does not clutter your working directory with
.aux or .log or other auxiliary files. It has of course the
usual features of automation tools: It automatically re-runs
(La)TeX for cross-references. MakeIndex, BibTeX, Biber, or
makeglossaries will be executed if a corresponding option is
set. Furthermore, cluttex can watch input files for changes
(using an external program).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/cluttex
%doc %{_texmfdistdir}/texmf-dist/doc/support/cluttex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
