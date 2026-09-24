# Save profiling summary to text file, sorted so the expensive things are first
python -m cProfile -s cumtime example.py > profile.txt

# Save to a log file and make a dot graph
# needs: pip install gprof2dot, and graphviz installed for "dot"
python -m cProfile -o output.pstats example.py
gprof2dot -f pstats output.pstats | dot -Tpng -o output.png
