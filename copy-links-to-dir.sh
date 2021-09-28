# Link to every note in a folder:
ls | gsed -E 's/(.*).md/[[\1]]\n\n/' > ../other/Founding\ Group.md