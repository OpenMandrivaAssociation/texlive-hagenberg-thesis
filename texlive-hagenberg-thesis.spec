%global tl_name hagenberg-thesis
%global tl_revision 74272

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Collection of LaTeX classes, style files and example documents for academic m...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hagenberg-thesis
License:	cc-by-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hagenberg-thesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hagenberg-thesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a collection of modern LaTeX classes, style files and example
documents for authoring Bachelor, Master, Diploma, or PhD theses and
related academic manuscripts in English and German. Pre-configured
English and German documents are available. They are easy to use even
for LaTeX beginners, and compatible with LaTeX distributions for
Windows, macOS, and Linux. The document classes are immediately usable
and convenient to customize.

