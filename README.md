jkstyles
========

Additional Pygment styles. Especially aimed for use in LaTeX documents
with Minted.

## Installation instructions

Just do

    python setup.py install

If pygments is not installed already, it should download it for you.

## LaTeX & Minted Example

```latex
\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}

\usepackage{minted}

% Use my minted theme
% It fixes issue especially with Fortran
\usemintedstyle{jkdefault}

\newminted{fortran}{frame=lines,numbersep=5pt,gobble=2}

\begin{document}

\begin{fortrancode}

  !Without default style, the underscore would be incorrectly
  !flagged as an error and surrounded by a red box.
  x = 5.0_dp

\end{fortrancode}

\end{document}

```
