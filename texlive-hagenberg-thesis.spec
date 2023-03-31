Name:		texlive-hagenberg-thesis
Version:	56798
Release:	2
Summary:	A Collection of LaTeX classes, style files, and example documents for academic manuscripts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hagenberg-thesis
License:	cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hagenberg-thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hagenberg-thesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle contains a collection of modern LaTeX classes,
style files, and example documents for authoring Bachelor,
Master, or Diploma theses and related academic manuscripts in
English and German. Includes a comprehensive tutorial (in
German) with detailed instructions and authoring guidelines.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hagenberg-thesis
%doc %{_texmfdistdir}/doc/latex/hagenberg-thesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
